import os
import re
import time
from pathlib import Path

import nbformat
from dotenv import load_dotenv
from nbclient import NotebookClient

# .env laden
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

# Alle Notebooks in HDA und HOOK finden
NOTEBOOKS = sorted(
    [str(p) for p in Path("HOOK").rglob("*.ipynb")]
)

def patch_notebook_credentials(nb):
    """
    Ersetzt input()/getpass()-basierte Credential-Abfragen in Code-Zellen
    durch Environment-Variablen.
    """

    for cell in nb.cells:
        if cell.cell_type != "code":
            continue

        src = cell.source

        # Sicherstellen, dass os importiert ist, falls wir os.environ einsetzen
        if "os.environ[" in src and "import os" not in src:
            src = "import os\n" + src

        # Username patterns
        src = re.sub(
            r'DESP_USERNAME\s*=\s*input\([^\n]*\)',
            'DESP_USERNAME = os.environ["DESTINE_SERVICE_USER"]',
            src
        )
        src = re.sub(
            r'desp_username\s*=\s*input\([^\n]*\)',
            'desp_username = os.environ["DESTINE_SERVICE_USER"]',
            src
        )

        # Password patterns: getpass(...)
        src = re.sub(
            r'DESP_PASSWORD\s*=\s*getpass\([^\n]*\)',
            'DESP_PASSWORD = os.environ["DESTINE_SERVICE_PASSWORD"]',
            src
        )
        src = re.sub(
            r'desp_password\s*=\s*getpass\([^\n]*\)',
            'desp_password = os.environ["DESTINE_SERVICE_PASSWORD"]',
            src
        )

        # Password patterns: getpass.getpass(...)
        src = re.sub(
            r'DESP_PASSWORD\s*=\s*getpass\.getpass\([^\n]*\)',
            'DESP_PASSWORD = os.environ["DESTINE_SERVICE_PASSWORD"]',
            src
        )
        src = re.sub(
            r'desp_password\s*=\s*getpass\.getpass\([^\n]*\)',
            'desp_password = os.environ["DESTINE_SERVICE_PASSWORD"]',
            src
        )

        # Falls os noch nicht importiert ist, aber wir jetzt os.environ eingefügt haben
        if 'os.environ["DESTINE_SERVICE_' in src and "import os" not in src:
            src = "import os\n" + src

        cell.source = src

    return nb


def execute_notebook(path: str):
    print("\n" + "=" * 80)
    print(f"STARTING NOTEBOOK: {path}")
    print("=" * 80)

    start_time = time.time()

    with open(path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    nb = patch_notebook_credentials(nb)

    client = NotebookClient(
        nb,
        timeout=7200,
        kernel_name="python3",
        allow_errors=False,
    )

    client.execute()

    duration = time.time() - start_time
    print(f"SUCCESS: {path}")
    print(f"DURATION: {duration:.1f} s")


def test_notebooks():
    username = os.getenv("DESTINE_SERVICE_USER")
    password = os.getenv("DESTINE_SERVICE_PASSWORD")

    if not username:
        raise RuntimeError("DESTINE_SERVICE_USER not found in .env or environment")
    if not password:
        raise RuntimeError("DESTINE_SERVICE_PASSWORD not found in .env or environment")

    print("Credentials found:")
    print(f" - DESTINE_SERVICE_USER: {username}")
    print(f" - DESTINE_SERVICE_PASSWORD set: {password is not None}")

    if not NOTEBOOKS:
        raise RuntimeError("No notebooks found in HDA/ or HOOK/")

    print(f"\nFound {len(NOTEBOOKS)} notebooks:")
    for nb in NOTEBOOKS:
        print(f" - {nb}")

    failed = []

    for notebook in NOTEBOOKS:
        try:
            execute_notebook(notebook)
        except Exception as e:
            print(f"FAILED: {notebook}")
            print(f"ERROR: {e}")
            failed.append((notebook, str(e)))

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total notebooks: {len(NOTEBOOKS)}")
    print(f"Passed: {len(NOTEBOOKS) - len(failed)}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFailed notebooks:")
        for nb, err in failed:
            print(f" - {nb}: {err}")
        raise RuntimeError(f"{len(failed)} notebook(s) failed")


if __name__ == "__main__":
    test_notebooks()
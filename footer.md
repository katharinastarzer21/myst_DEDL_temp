% This defines the footer of the site, and is not parsed as a regular "page"
% We point to it with the following in `myst.yml`:
% site:
% parts:
% footer: footer.md

% Here we use `grid` to add a basic grid structure to the HTML,
% but the formatting column sizes are defined manually in css/footer.css
% see the `grid-template-columns` line.
:::::{grid} 3 3 5 5
:class: outer-grid col-screen

<!-- Project description -->

::::{div}

```{image} img/logo_bar.png
:width: 100000px
:align: left
```

Destination Earth Data Lake Laboratory
::::

<!-- Spacer between project description and links columns -->
::::{div .footer}

::::{grid} 2 2 4

:::{div}
<!-- Erste Spalte leer -->
:::

:::{div}
<!-- Zweite Spalte leer -->
:::

:::{div}
- [About](https://destination-earth.eu/)
- [Github](https://github.com/destination-earth)
:::

::::

::::

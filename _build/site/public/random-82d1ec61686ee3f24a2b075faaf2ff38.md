:::{raw} html

<div class="flex flex-wrap gap-2 mb-6">
  <button class="px-3 py-1 rounded bg-gray-200 hover:bg-gray-300" data-tag="all">Alle</button>
  <button class="px-3 py-1 rounded bg-gray-200 hover:bg-gray-300" data-tag="climate">🌦 Climate</button>
  <button class="px-3 py-1 rounded bg-gray-200 hover:bg-gray-300" data-tag="ml">🤖 ML</button>
  <button class="px-3 py-1 rounded bg-gray-200 hover:bg-gray-300" data-tag="hydro">💧 Hydrology</button>
</div>

<div id="gallery" class="space-y-4">
  <div class="p-4 border border-gray-300 rounded shadow-sm" data-tags="climate ml">
    <strong>Notebook 1:</strong> Climate + ML
  </div>
  <div class="p-4 border border-gray-300 rounded shadow-sm" data-tags="ml">
    <strong>Notebook 2:</strong> Machine Learning
  </div>
  <div class="p-4 border border-gray-300 rounded shadow-sm" data-tags="hydro">
    <strong>Notebook 3:</strong> Hydrology
  </div>
  <div class="p-4 border border-gray-300 rounded shadow-sm" data-tags="climate">
    <strong>Notebook 4:</strong> Climate Only
  </div>
</div>

<script src="static/filter.js"></script>

:::



```{raw} html

<!-- Filter buttons -->

<div id="tag-filters" style="margin-bottom: 1rem;">

&nbsp; <button class="filter-btn" data-filter="all">All</button>

&nbsp; <button class="filter-btn" data-filter="STAC">STAC</button>

&nbsp; <button class="filter-btn" data-filter="Digital Twin">Digital Twin</button>

&nbsp; <button class="filter-btn" data-filter="Authentication">Authentication</button>

</div>



<style>

&nbsp; .filter-btn {

&nbsp;   background-color: #e6f0fa;

&nbsp;   border: none;

&nbsp;   padding: 6px 12px;

&nbsp;   margin: 4px;

&nbsp;   border-radius: 6px;

&nbsp;   cursor: pointer;

&nbsp;   font-size: 0.85em;

&nbsp; }



&nbsp; .filter-btn:hover {

&nbsp;   background-color: #cddff1;

&nbsp; }

</style>



<script>

document.addEventListener('DOMContentLoaded', function () {

&nbsp; const buttons = document.querySelectorAll('.filter-btn');

&nbsp; const cards = document.querySelectorAll('.notebook-card, div\[data-tags]');



&nbsp; buttons.forEach(button => {

&nbsp;   button.addEventListener('click', () => {

&nbsp;     const filter = button.getAttribute('data-filter');



&nbsp;     cards.forEach(card => {

&nbsp;       const tags = (card.getAttribute('data-tags') || "").split(" ");

&nbsp;       if (filter === 'all' || tags.includes(filter)) {

&nbsp;         card.style.display = 'flex';

&nbsp;       } else {

&nbsp;         card.style.display = 'none';

&nbsp;       }

&nbsp;     });

&nbsp;   });

&nbsp; });

});

</script>







<div style="display: flex; flex-direction: column; gap: 20px; max-width: 800px;">

<div style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>HDA PySTAC-Client Introduction</strong><br>
      This notebook shows the basic use of DestinE Data Lake Harmonised Data Access using pystac-client.
      <div style="margin: 6px 0;">
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">STAC</span>
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">Authentication</span>
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">Access Token</span>
      </div>
      <a href="production/HDA/PySTAC/HDA-PyStac-Client.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Extreme DT Data Availability</strong><br>
      his notebook shows how to check the data availablility for the Weather-Induced Extremes Digital Twin (Extremes DT) using the ECMWF Aviso package.
      <div style="margin: 6px 0;">
        <span class="tag">pyaviso</span>
        <span class="tag">Digital Twin</span>
      </div>
      <a href="production/HDA/DestinE\_Digital\_Twins/ExtremeDT-dataAvailability.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Weather-Induced Extremes - Data Access using DEDL HDA</strong><br>
      This notebook shows the basic use of DestinE Data Lake Harmonised Data Access using pystac-client.
      <div style="margin: 6px 0;">
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">Digital Twin</span>
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">ECMWF</span>
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">Earthkit</span>
      </div>
      <a href="production/HDA/DestinE\_Digital\_Twins/DEDL-HDA-EO.ECMWF.DAT.DT\_EXTREMES.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>HDA Climate DT Parameter Plotter - Tutorial</strong><br>
      This notebook shows how to 
      <div style="margin: 6px 0;">
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">Digital Twin</span>
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">ECMWF</span>
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">Earthkit</span>
      </div>
      <a href="production/HDA/DestinE\_Digital\_Twins/ClimateDT-ParameterPlotter.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Climate Change Adaptation</strong><br>
      Destination Earth - Climate Change Adaptation Digital Twin Series Plot- Data Access using DEDL HDA
      <div style="margin: 6px 0;">
         <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">Digital Twin</span>
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">ECMWF</span>
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">Authentification</span>
      </div>
      <a href="production/HDA/DestinE\_Digital\_Twins/DEDL-HDA-EO.ECMWF.DAT.DT\_CLIMATE-Series.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<div class="notebook-card" data-tags="Dask Pakistan Flood 2022 GFM" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 80px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service – Dask 101</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">Dask</span>
        <span class="tag">Cluster</span>
        <span class="tag">Array</span>
      </div>
      <a href="STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>



</div>


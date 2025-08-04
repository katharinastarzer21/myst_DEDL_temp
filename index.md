# DEDL Notebook Gallery

::::{tab-set}
:::{tab-item} Introduction
:sync: tab1

<!--
```{card} Card title
:header: The _Header_
:footer: Footer
Card content

![EUMETSAT Logo](img/EUMETSAT-logo.png)
hallo
```
-->


<img style="float:left; width:5%" src="./img/EUMETSAT-icon.png"/>  
<br>

Destination Earth Data Lake Laboratory, which contains additional information for working with DestinE Data Lake services:
- [Harmonised Data Access](https://github.com/destination-earth/DestinE-DataLake-Lab/tree/main/HDA) (Juypter notebooks examples + Python Tools)
- [STACK service](https://github.com/destination-earth/DestinE-DataLake-Lab/tree/main/STACK) (Juypter Notebook examples on how to use DASK for near data processing)
- [HOOK service](https://github.com/destination-earth/DestinE-DataLake-Lab/tree/main/HOOK) (Juypter Notebook examples on how to use HOOK for workflows)


Further information available in DestinE Data Lake documentation: https://destine-data-lake-docs.data.destination-earth.eu/en/latest/index.html


>**Additional ressources:**
>- DestinE Data Portfolio: https://hda.data.destination-earth.eu/ui/catalog
>- DataLake Priority services: https://hda.data.destination-earth.eu/ui/services 
>- HDA SWAGGER UI: https://hda.data.destination-earth.eu/docs/

:::
:::{tab-item} Overview
:sync: tab2

## Notebook Filter

<button data-filter-tag="HDA">Nur HDA</button>
<button data-filter-tag="Core API">Nur Core API</button>
<button data-filter-tag="all">Alle</button>

<div class="notebook-card" data-tags="HDA Core API" style="display: flex;">Notebook 1: HDA</div>
<div class="notebook-card" data-tags="DataCube" style="display: flex;">Notebook 2: DataCube</div>

<a href="#" onclick="
  event.preventDefault();
  Array.from(document.querySelectorAll('.notebook-card')).forEach(card => {
    const tags = card.dataset.tags || '';
    card.style.display = tags.includes('HDA') ? 'flex' : 'none';
  });
">Nur HDA anzeigen</a>



<div style="display: flex; flex-direction: column; gap: 20px; max-width: 800px;">

<!-- HDA Tutorial -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>HDA Tutorial</strong><br>
      This notebook demonstrates the first steps using the Harmonised Data access API.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">Core API</span>
      </div>
      <a href="production/HDA/REST/HDA-REST-full-version.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- HDA Tutorial - quick start -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>HDA Tutorial - Quick start</strong><br>
      This notebook demonstrates how to use the HDA (Harmonized Data Access) API by sending a few HTTP requests to the API, using Python code.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">HTTP requests</span>
      </div>
      <a href="production/HDA/REST/HDA-REST-quick-start.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- HDA Tutorial - Queryables -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>HDA Tutorial - Queryables</strong><br>
      This notebook demonstrates how to use the queryables API to filter C3S and DestinE digital twin collections by leveraging variable terms that dynamically adjust based on user selections.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">C3S</span><span class="tag">Digital twin</span><span class="tag">Authentification</span>
      </div>
      <a href="production/HDA/REST/HDA-REST-Queryables.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>



<!-- HDA PySTAC-Client Introduction -->
<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>PySTAC-Client Introduction</strong><br>
      This notebook shows the basic use of DestinE Data Lake Harmonised Data Access using pystac-client.
      <div style="margin: 6px 0;">
        <span class="tag">HDA</span><span class="tag">Authentication</span><span class="tag">STAC</span>
        <span class="tag">Access Token</span>
      </div>
      <a href="production/HDA/PySTAC/HDA-PyStac-Client.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<!-- Extreme DT Data Availability -->
<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Extreme DT Data Availability</strong><br>
      This notebook shows how to check the data availablility for the Weather-Induced Extremes Digital Twin (Extremes DT) using the ECMWF Aviso package.
      <div style="margin: 6px 0;">
        <span class="tag">HDA</span><span class="tag">pyaviso</span>
        <span class="tag">Digital Twin</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/ExtremeDT-dataAvailability.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Weather-Induced Extremes -->
<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Weather-Induced Extremes</strong><br>
      This notebook demonstrates how to access and download sea ice coverage data from the Weather-Induced Extremes Digital Twin using the DestinE Data Lake Harmonised Data Access (DEDL HDA) API, including authentication, filtering, polling, and visualizing the result on a map.
      <div style="margin: 6px 0;">
        <span class="tag">HDA</span><span class="tag">ECMWF</span><span class="tag">Earthkit</span>
        <span class="tag">Digital Twin</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/DEDL-HDA-EO.ECMWF.DAT.DT_EXTREMES.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>




<!-- HDA Climate DT Parameter Plotter - Tutorial -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Climate DT Parameter Plotter - Tutorial</strong><br>
      This notebook provides an interactive workflow to select, query, download, and visualize Climate Digital Twin parameters from the DestinE Data Lake using the DEDL HDA API.
      <div style="margin: 6px 0;">
<span class="tag">HDA</span><span class="tag">Digital Twin</span><span class="tag">ECMWF</span><span class="tag">Earthkit</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/ClimateDT-ParameterPlotter.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- HDA Extreme DT Parameter Plotter - Tutorial -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Extreme DT Parameter Plotter - Tutorial</strong><br>
      This notebook shows how to select, request, and download Climate Digital Twin Extremes data from the DestinE Data Lake (DEDL HDA), including user-defined parameter, scenario, date, and level selection, followed by secure authentication, API querying, and visualization using EarthKit.
      <div style="margin: 6px 0;">
<span class="tag">HDA</span><span class="tag">Digital Twin</span><span class="tag">ECMWF</span><span class="tag">Earthkit</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/ClimateDT-ParameterPlotter.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Climate Change Adaptation Digital Twin Series-->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Climate Change Adaptation Digital Twin Series</strong><br>
      This notebook authenticates a user with DestinE services, constructs and submits data requests to the DEDL HDA API for Climate Digital Twin projections, polls for availability, downloads GRIB data for multiple years, and visualizes it using EarthKit.
      <div style="margin: 6px 0;">
<span class="tag">HDA</span><span class="tag">Digital Twin</span><span class="tag">ECMWF</span><span class="tag">Authentification</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/DEDL-HDA-EO.ECMWF.DAT.DT_CLIMATE-Series.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Weather-Induced Extremes Digital Twin Series -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Weather-Induced Extremes Digital Twin Series</strong><br>
      This notebook authenticates with the DestinE API, queries ECMWF Extremes Digital Twin forecast data for a user-selected date within the last 14 days, downloads it, and visualizes wind gust and sea-level pressure fields using EarthKit.
      <div style="margin: 6px 0;">
<span class="tag">HDA</span><span class="tag">Digital Twin</span><span class="tag">ECMWF</span><span class="tag">Authentification</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/DEDL-HDA-EO.ECMWF.DAT.DT_EXTREMES-Series.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Climate Change Adaptation -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Climate Change Adaptation</strong><br>
      This notebook authenticates with the DestinE API, queries ECMWF Climate Digital Twin adaptation data based on ScenarioMIP parameters, downloads the selected forecast data using a robust retry mechanism, and visualizes it using EarthKit.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">Digital Twin</span><span class="tag">ECMWF</span><span class="tag">Authentification</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/DEDL-HDA-EO.ECMWF.DAT.DT_CLIMATE.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- ERA5 hourly data on single levels from 1940 to present -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>ERA5 hourly data on single levels from 1940 to present</strong><br>
      This notebook shows how to authenticate with the DestinE API, queries and downloads ERA5 single-level reanalysis data using the DEDL HDA service, and visualizes the result with EarthKit.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">ECMWF</span>
      </div>
      <a href="production/HDA/CDS_data/DEDL-HDA-EO.ECMWF.DAT.REANALYSIS_ERA5_SINGLE_LEVELS.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- EODAG - A quick start with DEDL -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/eodag_logo_160.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>EODAG - A quick start with DEDL</strong><br>
      This notebook provides a quickstart guide for using the EODAG Python API and CLI to search, discover, and download DEDL data.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">EODAG</span>
      </div>
      <a href="production/HDA/EODAG/HDA-EODAG-quick-start.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- EODAG - DestinE Data Lake Provider -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/eodag_logo_160.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>EODAG - DestinE Data Lake Provider</strong><br>
      This notebook demonstrates how to use the DEDL provider in EODAG.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">EODAG</span>
      </div>
      <a href="production/HDA/EODAG/HDA-EODAG-full-version.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- AVHRR Level 1B Metop Global - Data Access -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>AVHRR Level 1B Metop Global - Data Access</strong><br>
      This notebook demonstrates how to search and access Metop data using HDA and how to read, process and visualize it using satpy.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">Metop</span><span class="tag">satpy</span><span class="tag">AVHRR</span>
      </div>
      <a href="production/HDA/EUM_data/DEDL-HDA-EO.EUM.DAT.METOP.AVHRRL1.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- OLCI Level 1B Reduced Resolution - Sentinel-3 -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>OLCI Level 1B Reduced Resolution - Sentinel-3</strong><br>
      This notebook demonstrates how to search and access Sentinel-3 data using HDA and how to read and visualize it using satpy.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">OLCI</span><span class="tag">satpy</span><span class="tag">Sentinel-3</span>
      </div>
      <a href="production/HDA/EUM_data/DEDL-HDA-EO.EUM.DAT.SENTINEL-3.OL_1_ERR___.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>



<!-- Using HDA to find and download data for Urban Area Monitoring with Sentinel-1 Data -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Using HDA to find and download data for Urban Area Monitoring with Sentinel-1 Data</strong><br>
      This notebook demonstrates a simple example of how you can access data from DEDL using HDA and what you can do with it using an example with Sentinel-1 data.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">Thresholding techniques</span><span class="tag">Sentinel-1</span>
      </div>
      <a href="production/HDA/Fresh_Data_Pool/DEDL-HDA-EO.ESA.DAT.SENTINEL-1.L1_GRD.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- How to use HDA to find and download data for conducting monitoring of Śniadrwy lake -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>How to use HDA to find and download data for conducting monitoring of Śniadrwy lake</strong><br>
      This notebook demonstrates a simple example of how you can access data from DEDL using HDA and what you can do with it using an example with Sentinel-1 data.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">Thresholding techniques</span><span class="tag">Sentinel-2</span>
      </div>
      <a href="production/HDA/Fresh_Data_Pool/DEDL-HDA-EO.ESA.DAT.SENTINEL-2.MSI.L2A.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>



<!-- Access to Hook services -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Access to Hook services</strong><br>
      This Notebook demonstrates the retrieval of a token appropriate for interaction with the OnDemand Processing API (Hook API) and listing of available Hooks (Processors) using the retrieved token.
      <div style="margin: 6px 0;">
         <span class="tag">Hook</span><span class="tag">Authentification</span><span class="tag">Token</span>
      </div>
      <a href="production/HOOK/DEDL-Hook_access.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Hook Tutorial - Data Harvest -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Hook Tutorial - Data Harvest</strong><br>
      This notebook demonstrates how to use the Hook service.
      <div style="margin: 6px 0;">
         <span class="tag">Hook</span><span class="tag">Authentification</span><span class="tag">Workflow</span><span class="tag">Storage</span>
      </div>
      <a href="production/HOOK/Tutorial.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- STACK service - Dask 101 -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/dask.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service - Dask 101</strong><br>
     This notebook introduces Dask's core APIs and demonstrates how to use them for scalable, parallel, and distributed data processing, culminating in deploying and interacting with a Dask cluster on the DestinE Data Lake STACK service.
      <div style="margin: 6px 0;">
         <span class="tag">STACK</span><span class="tag">Dask</span><span class="tag">Cluster</span>
      </div>
      <a href="production/STACK/STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- STACK service - Python Client Dask -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/dask.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service - Python Client Dask</strong><br>
     This notebook demonstrates how to use the DEDL Stack Python client to authenticate, manage, and execute parallel, multi-cloud Dask computations on distributed datasets stored across Central Site and LUMI bridge.
      <div style="margin: 6px 0;">
         <span class="tag">STACK</span><span class="tag">Dask</span><span class="tag">GFM</span>
      </div>
      <a href="production/STACK/STACK-Python-Client-Dask.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>



<!-- STACK Service Dask -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/dask.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK Service Dask</strong><br>
     This notebook introduces authentication and multi-cluster management using the DEDL Stack client with OIDC, enabling users to securely spawn, monitor, and scale Dask clusters across Central and LUMI locations within the DestinE Data Lake.
<div style="margin: 6px 0;">
         <span class="tag">STACK</span><span class="tag">Dask</span><span class="tag">GFM</span>
      </div>
      <a href="production/STACK/DEDL_StackService_Dask.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- ExtremeDT Weather Data Cubes -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>ExtremeDT Weather Data Cubes</strong><br>
      This notebook demonstrates how to access, explore, and visualize weather forecast data from the ExtremeDT data cubes using xarray and matplotlib, including spatial plots, time series analysis, and interactive dashboard preparation.
      <div style="margin: 6px 0;">
         <span class="tag">STACK</span><span class="tag">DataCube</span><span class="tag">Digital Twin</span>
      </div>
      <a href="production/STACK/ExtremeDT-DataCube.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Interactive Dashboard for ExtremeDT Weather Forecast Data with xcube -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/xcube.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Interactive Dashboard for ExtremeDT Weather Forecast Data with xcube</strong><br>
      This notebook guides users through accessing ExtremeDT weather data cubes, filtering them by region, converting units, and visualizing the results in an interactive dashboard using the xcube viewer.
      <div style="margin: 6px 0;">
         <span class="tag">STACK</span><span class="tag">DataCube</span><span class="tag">Digital Twin</span>
      </div>
      <a href="production/STACK/ExtremeDT-DataCube-xViewer.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


:::

:::{tab-item} HDA
:sync: tab3

<div style="display: flex; flex-direction: column; gap: 20px; max-width: 800px;">


<!-- HDA Tutorial -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>HDA Tutorial</strong><br>
      This notebook demonstrates the first steps using the Harmonised Data access API.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">Core API</span>
      </div>
      <a href="production/HDA/REST/HDA-REST-full-version.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- HDA Tutorial - quick start -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>HDA Tutorial - Quick start</strong><br>
      This notebook demonstrates how to use the HDA (Harmonized Data Access) API by sending a few HTTP requests to the API, using Python code.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">HTTP requests</span>
      </div>
      <a href="production/HDA/REST/HDA-REST-quick-start.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- HDA Tutorial - Queryables -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>HDA Tutorial - Queryables</strong><br>
      This notebook demonstrates how to use the queryables API to filter C3S and DestinE digital twin collections by leveraging variable terms that dynamically adjust based on user selections.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">C3S</span><span class="tag">Digital twin</span><span class="tag">Authentification</span>
      </div>
      <a href="production/HDA/REST/HDA-REST-Queryables.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>



<!-- HDA PySTAC-Client Introduction -->
<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>PySTAC-Client Introduction</strong><br>
      This notebook shows the basic use of DestinE Data Lake Harmonised Data Access using pystac-client.
      <div style="margin: 6px 0;">
        <span class="tag">HDA</span><span class="tag">Authentication</span><span class="tag">STAC</span>
        <span class="tag">Access Token</span>
      </div>
      <a href="production/HDA/PySTAC/HDA-PyStac-Client.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

<!-- Extreme DT Data Availability -->
<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Extreme DT Data Availability</strong><br>
      This notebook shows how to check the data availablility for the Weather-Induced Extremes Digital Twin (Extremes DT) using the ECMWF Aviso package.
      <div style="margin: 6px 0;">
        <span class="tag">HDA</span><span class="tag">pyaviso</span>
        <span class="tag">Digital Twin</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/ExtremeDT-dataAvailability.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Weather-Induced Extremes -->
<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Weather-Induced Extremes</strong><br>
      This notebook demonstrates how to access and download sea ice coverage data from the Weather-Induced Extremes Digital Twin using the DestinE Data Lake Harmonised Data Access (DEDL HDA) API, including authentication, filtering, polling, and visualizing the result on a map.
      <div style="margin: 6px 0;">
        <span class="tag">HDA</span><span class="tag">ECMWF</span><span class="tag">Earthkit</span>
        <span class="tag">Digital Twin</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/DEDL-HDA-EO.ECMWF.DAT.DT_EXTREMES.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>




<!-- HDA Climate DT Parameter Plotter - Tutorial -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Climate DT Parameter Plotter - Tutorial</strong><br>
      This notebook provides an interactive workflow to select, query, download, and visualize Climate Digital Twin parameters from the DestinE Data Lake using the DEDL HDA API.
      <div style="margin: 6px 0;">
<span class="tag">HDA</span><span class="tag">Digital Twin</span><span class="tag">ECMWF</span><span class="tag">Earthkit</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/ClimateDT-ParameterPlotter.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- HDA Extreme DT Parameter Plotter - Tutorial -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Extreme DT Parameter Plotter - Tutorial</strong><br>
      This notebook shows how to select, request, and download Climate Digital Twin Extremes data from the DestinE Data Lake (DEDL HDA), including user-defined parameter, scenario, date, and level selection, followed by secure authentication, API querying, and visualization using EarthKit.
      <div style="margin: 6px 0;">
<span class="tag">HDA</span><span class="tag">Digital Twin</span><span class="tag">ECMWF</span><span class="tag">Earthkit</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/ClimateDT-ParameterPlotter.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Climate Change Adaptation Digital Twin Series-->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Climate Change Adaptation Digital Twin Series</strong><br>
      This notebook authenticates a user with DestinE services, constructs and submits data requests to the DEDL HDA API for Climate Digital Twin projections, polls for availability, downloads GRIB data for multiple years, and visualizes it using EarthKit.
      <div style="margin: 6px 0;">
<span class="tag">HDA</span><span class="tag">Digital Twin</span><span class="tag">ECMWF</span><span class="tag">Authentification</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/DEDL-HDA-EO.ECMWF.DAT.DT_CLIMATE-Series.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Weather-Induced Extremes Digital Twin Series -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Weather-Induced Extremes Digital Twin Series</strong><br>
      This notebook authenticates with the DestinE API, queries ECMWF Extremes Digital Twin forecast data for a user-selected date within the last 14 days, downloads it, and visualizes wind gust and sea-level pressure fields using EarthKit.
      <div style="margin: 6px 0;">
<span class="tag">HDA</span><span class="tag">Digital Twin</span><span class="tag">ECMWF</span><span class="tag">Authentification</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/DEDL-HDA-EO.ECMWF.DAT.DT_EXTREMES-Series.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Climate Change Adaptation -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/ECMWF.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Climate Change Adaptation</strong><br>
      This notebook authenticates with the DestinE API, queries ECMWF Climate Digital Twin adaptation data based on ScenarioMIP parameters, downloads the selected forecast data using a robust retry mechanism, and visualizes it using EarthKit.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">Digital Twin</span><span class="tag">ECMWF</span><span class="tag">Authentification</span>
      </div>
      <a href="production/HDA/DestinE_Digital_Twins/DEDL-HDA-EO.ECMWF.DAT.DT_CLIMATE.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- ERA5 hourly data on single levels from 1940 to present -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>ERA5 hourly data on single levels from 1940 to present</strong><br>
      This notebook shows how to authenticate with the DestinE API, queries and downloads ERA5 single-level reanalysis data using the DEDL HDA service, and visualizes the result with EarthKit.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">ECMWF</span>
      </div>
      <a href="production/HDA/CDS_data/DEDL-HDA-EO.ECMWF.DAT.REANALYSIS_ERA5_SINGLE_LEVELS.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- EODAG - A quick start with DEDL -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/eodag_logo_160.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>EODAG - A quick start with DEDL</strong><br>
      This notebook provides a quickstart guide for using the EODAG Python API and CLI to search, discover, and download DEDL data.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">EODAG</span>
      </div>
      <a href="production/HDA/EODAG/HDA-EODAG-quick-start.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- EODAG - DestinE Data Lake Provider -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/eodag_logo_160.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>EODAG - DestinE Data Lake Provider</strong><br>
      This notebook demonstrates how to use the DEDL provider in EODAG.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">EODAG</span>
      </div>
      <a href="production/HDA/EODAG/HDA-EODAG-full-version.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- AVHRR Level 1B Metop Global - Data Access -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>AVHRR Level 1B Metop Global - Data Access</strong><br>
      This notebook demonstrates how to search and access Metop data using HDA and how to read, process and visualize it using satpy.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">Metop</span><span class="tag">satpy</span><span class="tag">AVHRR</span>
      </div>
      <a href="production/HDA/EUM_data/DEDL-HDA-EO.EUM.DAT.METOP.AVHRRL1.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- OLCI Level 1B Reduced Resolution - Sentinel-3 -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>OLCI Level 1B Reduced Resolution - Sentinel-3</strong><br>
      This notebook demonstrates how to search and access Sentinel-3 data using HDA and how to read and visualize it using satpy.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">OLCI</span><span class="tag">satpy</span><span class="tag">Sentinel-3</span>
      </div>
      <a href="production/HDA/EUM_data/DEDL-HDA-EO.EUM.DAT.SENTINEL-3.OL_1_ERR___.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>



<!-- Using HDA to find and download data for Urban Area Monitoring with Sentinel-1 Data -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Using HDA to find and download data for Urban Area Monitoring with Sentinel-1 Data</strong><br>
      This notebook demonstrates a simple example of how you can access data from DEDL using HDA and what you can do with it using an example with Sentinel-1 data.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">Thresholding techniques</span><span class="tag">Sentinel-1</span>
      </div>
      <a href="production/HDA/Fresh_Data_Pool/DEDL-HDA-EO.ESA.DAT.SENTINEL-1.L1_GRD.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- How to use HDA to find and download data for conducting monitoring of Śniadrwy lake -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>How to use HDA to find and download data for conducting monitoring of Śniadrwy lake</strong><br>
      This notebook demonstrates a simple example of how you can access data from DEDL using HDA and what you can do with it using an example with Sentinel-1 data.
      <div style="margin: 6px 0;">
         <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">Thresholding techniques</span><span class="tag">Sentinel-2</span>
      </div>
      <a href="production/HDA/Fresh_Data_Pool/DEDL-HDA-EO.ESA.DAT.SENTINEL-2.MSI.L2A.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

:::

:::{tab-item} HOOK
:sync: tab4

<div style="display: flex; flex-direction: column; gap: 20px; max-width: 800px;">

<!-- Access to Hook services -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Access to Hook services</strong><br>
      This Notebook demonstrates the retrieval of a token appropriate for interaction with the OnDemand Processing API (Hook API) and listing of available Hooks (Processors) using the retrieved token.
      <div style="margin: 6px 0;">
         <span class="tag">Hook</span><span class="tag">Authentification</span><span class="tag">Token</span>
      </div>
      <a href="production/HOOK/DEDL-Hook_access.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Hook Tutorial - Data Harvest -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Hook Tutorial - Data Harvest</strong><br>
      This notebook demonstrates how to use the Hook service.
      <div style="margin: 6px 0;">
         <span class="tag">Hook</span><span class="tag">Authentification</span><span class="tag">Workflow</span><span class="tag">Storage</span>
      </div>
      <a href="production/HOOK/Tutorial.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


:::

:::{tab-item} STACK
:sync: tab5

<div style="display: flex; flex-direction: column; gap: 20px; max-width: 800px;">

<!-- STACK service - Dask 101 -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/dask.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service - Dask 101</strong><br>
     This notebook introduces Dask's core APIs and demonstrates how to use them for scalable, parallel, and distributed data processing, culminating in deploying and interacting with a Dask cluster on the DestinE Data Lake STACK service.
      <div style="margin: 6px 0;">
         <span class="tag">STACK</span><span class="tag">Dask</span><span class="tag">Cluster</span>
      </div>
      <a href="production/STACK/STACK-Dask-101.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- STACK service - Python Client Dask -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/dask.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK service - Python Client Dask</strong><br>
     This notebook demonstrates how to use the DEDL Stack Python client to authenticate, manage, and execute parallel, multi-cloud Dask computations on distributed datasets stored across Central Site and LUMI bridge.
      <div style="margin: 6px 0;">
         <span class="tag">STACK</span><span class="tag">Dask</span><span class="tag">GFM</span>
      </div>
      <a href="production/STACK/STACK-Python-Client-Dask.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>



<!-- STACK Service Dask -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/dask.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>STACK Service Dask</strong><br>
     This notebook introduces authentication and multi-cluster management using the DEDL Stack client with OIDC, enabling users to securely spawn, monitor, and scale Dask clusters across Central and LUMI locations within the DestinE Data Lake.
<div style="margin: 6px 0;">
         <span class="tag">STACK</span><span class="tag">Dask</span><span class="tag">GFM</span>
      </div>
      <a href="production/STACK/DEDL_StackService_Dask.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- ExtremeDT Weather Data Cubes -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>ExtremeDT Weather Data Cubes</strong><br>
      This notebook demonstrates how to access, explore, and visualize weather forecast data from the ExtremeDT data cubes using xarray and matplotlib, including spatial plots, time series analysis, and interactive dashboard preparation.
      <div style="margin: 6px 0;">
         <span class="tag">STACK</span><span class="tag">DataCube</span><span class="tag">Digital Twin</span>
      </div>
      <a href="production/STACK/ExtremeDT-DataCube.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


<!-- Interactive Dashboard for ExtremeDT Weather Forecast Data with xcube -->

<div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/xcube.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>Interactive Dashboard for ExtremeDT Weather Forecast Data with xcube</strong><br>
      This notebook guides users through accessing ExtremeDT weather data cubes, filtering them by region, converting units, and visualizing the results in an interactive dashboard using the xcube viewer.
      <div style="margin: 6px 0;">
         <span class="tag">STACK</span><span class="tag">DataCube</span><span class="tag">Digital Twin</span>
      </div>
      <a href="production/STACK/ExtremeDT-DataCube-xViewer.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>
:::
::::
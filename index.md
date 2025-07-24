<!-- Include gallery fragment -->
{% include gallery_fragment.html %}

<!-- NOTEBOOK GALLERY -->
<div style="display: flex; flex-direction: column; gap: 20px; max-width: 800px;">

  <!-- BOX 1 -->
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

  <!-- BOX 2 -->
  <div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>ExtremeDT – Data Cube</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span class="tag">DataCube</span>
        <span class="tag">Digital Twin</span>
      </div>
      <a href="ExtremeDT-DataCube.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

  <!-- BOX 3 -->
  <div class="notebook-card" data-tags="DataCube Digital Twin" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>ExtremeDT – xViewer Dashboard</strong><br>
      Create a dashboard based on Data Cube from Weather and Geophysical Extremes DT.
      <div style="margin: 6px 0;">
        <span class="tag">DataCube</span>
        <span class="tag">Digital Twin</span>
      </div>
      <a href="ExtremeDT-DataCube-xViewer.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>


  <!-- BOX 5 -->
  <div style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
    <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
      <img src="img/EUMETSAT-logo.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
    </div>
    <div style="flex: 1;">
      <strong>DestinE Data Lake – Stack Service Dask</strong><br>
      Demonstrates how to use Dask with the DEDL StackService for scalable data processing.
      <div style="margin: 6px 0;">
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">Dask</span>
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">Authentication</span>
        <span style="display:inline-block; background-color:#e6f0fa; border-radius:10px; padding:3px 10px; margin:2px; font-size: 0.75em;">Cluster</span>
      </div>
      <a href="DEDL_StackService_Dask.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
    </div>
  </div>

</div>

<!-- FILTER SCRIPT -->
<script>
function filterNotebooks(tag) {
  document.querySelectorAll('.notebook-card').forEach(card => {
    const tags = card.getAttribute('data-tags') || '';
    card.style.display = (tag === 'all' || tags.includes(tag)) ? 'flex' : 'none';
  });
}
</script>

<style>
  .tag {
    display: inline-block;
    background-color: #e6f0fa;
    border-radius: 10px;
    padding: 3px 10px;
    margin: 2px;
    font-size: 0.75em;
  }
</style>

# Notebook-Galerie

<!-- Tag-Filter Buttons -->
<div id="tag-filters">
  <button onclick="filterBoxes('alle')">Alle</button>
  <button onclick="filterBoxes('datenanalyse')">Datenanalyse</button>
  <button onclick="filterBoxes('statistik')">Statistik</button>
</div>

<!-- Notebook-Boxes -->
<div id="gallery">
  <div class="box" data-tags="datenanalyse statistik">
    <a href="production/HDA/PySTAC/HDA-PyStac-Client.ipynb"><strong>HDA-PyStac-Client</strong></a><br>
    datenanalyse, statistik
  </div>
  <div class="box" data-tags="datenanalyse statistik">
    <a href="production/HDA/DestinE_Digital_Twins/ExtremeDT-dataAvailability.ipynb"><strong>ExtremeDT-dataAvailability</strong></a><br>
    datenanalyse, statistik
  </div>
</div>

<style>
.box {
  border: 1px solid #ddd;
  padding: 10px;
  margin: 10px;
  display: inline-block;
  width: 220px;
  vertical-align: top;
}
#tag-filters button {
  margin: 4px;
  padding: 6px 12px;
}
</style>

<script>
function filterBoxes(tag) {
  document.querySelectorAll('.box').forEach(box => {
    if(tag === 'alle' || box.dataset.tags.includes(tag)){
      box.style.display = 'inline-block';
    }else{
      box.style.display = 'none';
    }
  });
}
</script>
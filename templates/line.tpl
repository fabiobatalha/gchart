% if importjs:
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
% endif
<script type="text/javascript">
    google.load("visualization", "1", {packages:["corechart"]});

    var visualization;

    function draw() {
      drawVisualization();
    }

    function drawVisualization() {
      visualization = new google.visualization.LineChart(document.getElementById('chart'));
      new google.visualization.Query('http://localhost:6543/general/lines/data?code=scl').send(queryCallback);
    }

    function queryCallback(response) {
      visualization.draw(response.getDataTable());
    }
    
    google.setOnLoadCallback(draw);

</script>
<div id="chart"></div>

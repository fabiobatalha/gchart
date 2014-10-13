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
      visualization = new google.visualization.PieChart(document.getElementById('chart'));
      new google.visualization.Query('https://spreadsheets.google.com/tq?key=pCQbetd-CptHnwJEfo8tALA').send(queryCallback);
    }

    function queryCallback(response) {
      visualization.draw(response.getDataTable());
    }
    
    google.setOnLoadCallback(draw);

</script>
<div id="chart"></div>

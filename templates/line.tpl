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
      var container = document.getElementById('visualization_div');
      visualization = new google.visualization.LineChart(container);
      new google.visualization.Query('http://localhost:6543/general/lines/data?code=scl&reqId=1281812').send(queryCallback);
    }

    function queryCallback(response) {
      visualization.draw(response.getDataTable(), ${options});
    }

    
    google.setOnLoadCallback(draw);

</script>
<div id="visualization_div"></div>

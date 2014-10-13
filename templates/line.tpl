% if importjs:
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
% endif
<script type="text/javascript">
  google.load("visualization", "1", {packages:["corechart"]});
  google.setOnLoadCallback(drawChart);
  function drawChart() {

    ${options}

    var json_linechart = new google.visualization.LineChart(document.getElementById('chart'));
    var json_linechart_data = new google.visualization.DataTable(${jsondata});
    json_linechart.draw(json_linechart_data, options);

  }
</script>
<div id="chart"></div>
<div id="chart1"></div>
<div id="toolbar"></div>
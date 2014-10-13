% if importjs:
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
% endif
<script type="text/javascript">
  google.load("visualization", "1", {packages:["corechart"]});
  google.setOnLoadCallback(drawChart);
  function drawChart() {

    ${options}

    var json_chart = new google.visualization.LineChart(document.getElementById('chart'));
    var json_chart_data = new google.visualization.DataTable(${jsondata});
    json_chart.draw(json_chart_data, options);

  }
</script>
<div id="chart"></div>
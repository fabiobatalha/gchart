% if importjs:
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
% endif
<script type="text/javascript">
  google.load("visualization", "1", {packages:["corechart"]});
  google.setOnLoadCallback(drawChart);
  function drawChart() {
    ${jscode}

    ${options}

    var jscode_table = new google.visualization.LineChart(document.getElementById('chart'));
    jscode_table.draw(${id}, options);
  }
</script>
<div id="chart"></div>
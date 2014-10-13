% if importjs:
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
% endif
<script type="text/javascript">
  google.load("visualization", "1", {packages:["table"]});
  google.setOnLoadCallback(drawTable);
  function drawTable() {

    ${options}

    var json_chart = new google.visualization.Table(document.getElementById('table'));
    var json_chart_data = new google.visualization.DataTable(${jsondata});
    json_chart.draw(json_chart_data, options);

  }
</script>
<div id="table"></div>
% if importjs:
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
% endif
<script type="text/javascript">
    google.load("visualization", "1", {packages:["corechart"]});
    google.setOnLoadCallback(drawVisualization-${id});
    % if jsondatasource=='given':
        function drawVisualization-${id}() {
          ${options}
          var visualization = new google.visualization.PieChart(document.getElementById('chart-${id}'));
          var data = new google.visualization.DataTable(${jsondata});
          visualization.draw(data, options);
        }
    % elif jsondatasource=='url':
        function drawVisualization-${id}() {
          query = new google.visualization.Query('${jsondata}');
          query.send(queryCallback);
        }
        function queryCallback(response) {
          ${options}
          visualization = new google.visualization.PieChart(document.getElementById('chart-${id}'));
          visualization.draw(response.getDataTable(), options);
        }
    % endif

</script>
<div id="chart-${id}"></div>
% if importjs:
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
% endif
<script type="text/javascript">
    google.load("visualization", "1", {packages:["corechart"]});
    google.setOnLoadCallback(drawVisualization);

    % if jsondatasource=='given':
        function drawVisualization() {
        ${options}
        var visualization = new google.visualization.LineChart(document.getElementById('chart'));
        var data = new google.visualization.DataTable(${jsondata});
        visualization.draw(data, options);

        }
    % elif jsondatasource=='url':
        function drawVisualization() {
          visualization = new google.visualization.LineChart(document.getElementById('chart'));
          new google.visualization.Query('${jsondata}').send(queryCallback);
        }
        function queryCallback(response) {
          visualization.draw(response.getDataTable(), options);
        }
    % endif

</script>
<div id="chart"></div>
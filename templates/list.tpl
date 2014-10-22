% if importjs:
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
% endif
<script type="text/javascript">
    google.load("visualization", "1", {packages:["table"]});
    google.setOnLoadCallback(drawVisualization);

    ${options}

    % if jsondatasource=='given':
        function drawVisualization() {
        
        var visualization = new google.visualization.Table(document.getElementById('chart-${id}'));
        var data = new google.visualization.DataTable(${jsondata});
        visualization.draw(data, options);

        }
    % elif jsondatasource=='url':
        function drawVisualization() {
          query = new google.visualization.Query('${jsondata}');
          query.send(queryCallback);
        }
        function queryCallback(response) {
          visualization = new google.visualization.Table(document.getElementById('chart-${id}'));
          visualization.draw(response.getDataTable(), options);
        }
    % endif

</script>
<div id="chart-${id}"></div>
% if importjs:
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
% endif
<script type="text/javascript">
    google.load("visualization", "1", {packages:["table"]});
    google.setOnLoadCallback(drawVisualization);

    ${options}

    % if jsondatasource=='given':
        function drawVisualization() {
        
        var visualization = new google.visualization.Table(document.getElementById('table'));
        var data = new google.visualization.DataTable(${jsondata});
        visualization.draw(data, options);

        }
    % elif jsondatasource=='url':
        function drawVisualization() {
          drawToolbar();
          query = new google.visualization.Query('${jsondata}');
          query.send(queryCallback);
        }
        function queryCallback(response) {
          visualization = new google.visualization.Table(document.getElementById('table'));
          visualization.draw(response.getDataTable(), options);
        }

        function drawToolbar() {
          var components = [
              {type: 'html', datasource: '${jsondata}'},
              {type: 'csv', datasource: '${jsondata}'}
          ];
          google.visualization.drawToolbar(document.getElementById('toolbar'), components);
        };
    % endif

</script>
<div id="table"></div>
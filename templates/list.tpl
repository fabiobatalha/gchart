% if importjs:
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
% endif
<script type="text/javascript">
  google.load("visualization", "1", {packages:["table"]});
  google.setOnLoadCallback(drawTable);
  function drawTable() {
    ${jscode}

    ${options}

    var jscode_table = new google.visualization.Table(document.getElementById('table'));
    jscode_table.draw(${id}, options);
  }
</script>
<div id="table"></div>
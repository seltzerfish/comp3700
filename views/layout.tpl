<!DOCTYPE html>
<html lang="en">
<head>

  <!-- Basic Page Needs
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <meta charset="utf-8">
  <title>{{title}}</title>
  <meta name="description" content="">
  <meta name="author" content="">

  <!-- Mobile Specific Metas
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- FONT
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link href="//fonts.googleapis.com/css?family=Raleway:400,300,600" rel="stylesheet" type="text/css">

  <!-- CSS
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link rel="stylesheet" href="/static/css/normalize.css">
  <link rel="stylesheet" href="/static/css/skeleton.css">

  <!-- Favicon
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link rel="icon" type="image/png" href="/static/images/favicon.png">

</head>
<body>
  % if "username" in sess or title == "Login":
    % if "username" in sess:
    <div style="text-align: right; margin: 3%; margin-bottom: -10%">
      <h5>{{sess["username"]}} 
      %if sess["permissions"] == "MANAGER":
      &#9733; <!-- add a star -->
      %end
    </h5>
       <h6><a style="color: red" href="/logout">Logout</a></h6>
    </div>
    % end
  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    {{!base}}

  %else:
  <div class="container">
    <div class="row">
      <div class="twelve column" style="margin-top: 15%">
        <h4 style="text-align: center">You are not logged in</h4>
        <a href="/login" style="text-align: center; margin-top: 10%"><h5>Click here to log in</h2></a>
      </div>
    </div>
  </div>

<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
</body>
</html>

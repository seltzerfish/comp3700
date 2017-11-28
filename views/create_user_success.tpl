% rebase("layout.tpl", title="Store App - New User")
% if "permissions" in sess and sess["permissions"] == "MANAGER":
<div class="container">
  <div class="row" style="text-align: center; margin-top: 25%">
    <h4>User <b>{{user}}</b> successfully created.</h4>
    <h5>Temporary password is set to <b>{{pw}}</b></h5>
  </div>
  </div>
  % else:
  % include('wrong_permissions.tpl')
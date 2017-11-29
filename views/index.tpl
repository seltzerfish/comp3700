% rebase("layout.tpl", title="Store App")

<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 15%">
      <h4 style="text-align: center">Store App</h4>
      <p style="text-align: center; font-weight: 200">Welcome to the store app. Click a button to get started.</p>
    </div>
  </div>
  
  % if "permissions" in sess and sess["permissions"] == "MANAGER":
  <div class="row" style="text-align: center; margin-top: 5%">
    <div class="four columns">
      <a class="button button-primary" href="/orders">Checkout</a>
    </div>
    <div class="four columns">
      <a class="button button-primary" href="/add/product">Add a new product</a>
    </div>
    <div class="four columns">
      <a class="button button-primary" href="/products">Update existing product</a>
    </div>
  </div>
  <div class="row" style="margin-top: 5%; text-align: center">
    <div class="six columns">
      <a class="button button-primary" href="/create_user">Create A New User</a>
    </div>
    <div class="six columns">
      <a class="button button-primary" href="/store_report">Sales Report</a>
    </div>
  </div>
  % else:
  <div class="row" style="text-align: center; margin-top: 5%">
    <div class="twelve columns">
      <a class="button button-primary" href="/orders">Checkout</a>
    </div>
  </div>
  %end
</div>

% rebase("layout.tpl", title="Store App")

<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 15%">
      <h4 style="text-align: center">Store App</h4>
      <p style="text-align: center; font-weight: 200">Welcome to the store app. Click a button to get started.</p>
    </div>
  </div>
  <div class="row" style="text-align: center; margin-top: 5%">
    % if "permissions" in sess and sess["permissions"] == "MANAGER":
    <div class="four columns">
      <a class="button button-primary" href="/orders">Checkout</a>
    </div>
    <div class="four columns">
      <a class="button button-primary" href="/add/product">Add a new product</a>
    </div>
    <div class="four columns">
      <a class="button button-primary" href="/products">Update existing product</a>
    </div>
    % else:
      <div class="twelve columns">
      <a class="button button-primary" href="/orders">Checkout</a>
    </div>
    %end
  </div>
</div>

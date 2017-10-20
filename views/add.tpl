%rebase layout title="Store App - Add"

<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 10%">
      <h4 style="text-align: center">Add New Product</h4>
    </div>
  </div>
  <form action="/" method="POST">
    <fieldset>
      <div class="row", style="margin-top: 5%">
        <div class="six columns">
          <label for="nameInput">Product Name</label>
          <input class="u-full-width" type="text" placeholder="apple" name="nameInput">
        </div>
        <div class="three columns">
          <label for="quantityInput">Quantity</label>
          <input class="u-full-width" type="number" placeholder="3" name="quantityInput">
        </div>
        <div class="three columns">
          <label for="priceInput">Price (without '$')</label>
          <input class="u-full-width" type="text" placeholder="1.50" name="priceInput">
        </div>
      </div>
      <div class="row", style="margin-top: 5%">
        <div class="six columns">
          <label for="providerInput">Provider</label>
          <input class="u-full-width" type="text" placeholder="Fruits, inc." name="providerInput">
        </div>
        <div class="six columns">
          <label for="providerContactInput">Provider Telephone Number</label>
          <input class="u-full-width" type="tel" placeholder="555-555-5555" name="providerContactInput">
        </div>
      </div>
      <a class="button" href="/", style="margin: 3%; margin-left: 0%">Cancel</a>
      <input class="button-primary" type="submit" value="Submit">

    </fieldset>
  </form>
</div>
% rebase("layout.tpl", title="Store App - Update")

<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 10%">
      <h4 style="text-align: center">Update product: {{item_data[1]}}</h4>
    </div>
  </div>
  <form action="/update/{{item_data[0]}}" method="POST">
    <fieldset>
      <div class="row", style="margin-top: 5%">
        <div class="six columns">
          <label for="nameInput">Product Name</label>
          <input class="u-full-width" type="text" value="{{item_data[1]}}" name="nameInput">
        </div>
        <div class="three columns">
          <label for="quantityInput">Quantity</label>
          <input class="u-full-width" type="number" value="{{item_data[2]}}" name="quantityInput">
        </div>
        <div class="three columns">
          <label for="priceInput">Price (without '$')</label>
          <input class="u-full-width" type="text" value="{{item_data[3]}}" name="priceInput">
        </div>
      </div>
      <div class="row", style="margin-top: 5%">
        <div class="six columns">
          <label for="providerInput">Provider</label>
          <input class="u-full-width" type="text" value="{{item_data[4]}}" name="providerInput">
        </div>
        <div class="six columns">
          <label for="providerContactInput">Provider Telephone Number</label>
          <input class="u-full-width" type="tel" value="{{item_data[5]}}" name="providerContactInput">
        </div>
      </div>
      <a class="button" href="/", style="margin: 3%; margin-left: 0%">Cancel</a>
      <input class="button-primary" type="submit" value="Update">

    </fieldset>
  </form>
</div>

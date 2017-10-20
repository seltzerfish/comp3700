%rebase layout title="Store App"
<!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 15%">
      <h4 style="text-align: center">Update Product</h4>
      <p style="text-align: center; font-weight: 200">Find an item to modify</p>
    </div>
  </div>
  <dir class="row">

  </dir>
  <div class="row", style="text-align: center; margin-top: 5%">
    <table class="u-full-width">
      <thead>
        <tr>
          <th>Name</th>
          <th>ID</th>
          <th>Quantity</th>
          <th>Price</th>
          <th>Provider</th>
          <th>Provider Phone #</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody style='font-weight: 300'>
        %for i in range(0, len(table)):
        <tr>
          %for j in range(0, len(table[i])):
            <td>{{'$' if j == 3 else ''}}{{table[i][j]}}</td>
          %end
          <td><a class="button" href="update/{{table[i][1]}}">Update</a></td>
          <td><a class="button button-primary" href="delete/{{table[i][1]}}" style="background-color: #e54b4b; border-color: #e54b4b; ">Delete</a></td>
        </tr>
        %end
      </tbody>
    </table>
  </div>
</div>


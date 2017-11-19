% rebase("layout.tpl", title="Update Profile")

<div class="container">
  <div class="row">
    <div class="twelve columns" style="margin-top: 4%; margin-bottom: 5%">
      <h3 style="text-align: center">Update Profile</h3>
    </div>
  </div>
  <div class = "row">
    <div class="four columns">
      <h5 style="text-align: center"></h5>
    </div>
    <div class="four columns">
      <h5 style="text-align: center">Change Password</h5>
    </div>
  </div>
  <form action="/update_profile/self" method="POST" style="margin-left: 35%">
    <fieldset>
      <div class="row", style="margin-top: 5%">
        <div class="six columns">
          <label for="current_password">Current Password</label>
          <input class="u-full-width" id="current_password" type="password"  name="current_password">
        </div>
      </div>
      <div class="row">
        <div class="six columns">
          <label for="new_password">New Password</label>
          <input class="u-full-width" id="new_password" type="password"  name="new_password">
        </div>
      </div>
      <input class="button-primary" style="margin: 3%; margin-left: 0%" type="submit" value="Update">
    </fieldset>
  </form>
</div>

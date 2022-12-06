function startSession(e) {
  e.preventDefault();

  uid = localStorage.getItem("uid");
  var formData = {};
  var uri = "/signup";

  if (uid != null) {
    formData["uid"] = uid;
    uri = "/login";
  }

  $("#feedback").html('<div class="spinner-border" role="status">/div>');
  $.ajax({
    method: "POST",
    url: API_URL + uri,
    data: JSON.stringify(formData),
    dataType: "json",
    contentType: "Application/json",
    success: function (data) {
      user = data.user;
      localStorage.setItem("uid", user.uid);
      localStorage.setItem("User", JSON.stringify(data.user));
      window.location.replace("/infiniteGallery.html");
    },
    error: function (request) {
      $("#feedback").html(
        '<div class="alert alert-danger" role="alert">Invalid values.</div>'
      );
    },
  });
}

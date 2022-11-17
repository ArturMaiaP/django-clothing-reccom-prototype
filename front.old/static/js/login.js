function loginSubmit(e) {
  e.preventDefault();
  var formData= {
      email: $('#email').val(),
      password: $('#password').val(),
  }
  $('#feedback').html('<div class="spinner-border" role="status"><span class="sr-only">Loading...</span></div>');
  $.ajax({
    method: "POST",
    url: API_URL + "/login",
    data: JSON.stringify(formData),
    dataType: "json",
    contentType: "Application/json",
    success: function (data) {
      localStorage.setItem("User", JSON.stringify(data.user));
      window.location.replace('/infiniteGallery.html');
    },
    error: function (request) {
      $('#feedback').html('<div class="alert alert-danger" role="alert">Invalid Email or Password.</div>');
    },
  });
}

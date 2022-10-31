function loginSubmit(e) {
  e.preventDefault();
  var formData= {
      email: $('#email').val(),
      password: $('#password').val(),
  }
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
      alert(request.responseText);
    },
  });
}

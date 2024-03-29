function registerSubmit(e) {
    e.preventDefault();
    var formData= {
        name: $('#name').val(),
        email: $('#email').val(),
        password: $('#password').val(),
    }
    $.ajax({
      method: "POST",
      url: API_URL + "/signup",
      data: JSON.stringify(formData),
      dataType: "json",
      contentType: "Application/json",
      success: function (data) {
        window.location.replace('/login.html');
      },
      error: function (request) {
        alert(request.responseText);
      },
    });
  }
  
var counter=0;
function chat(e) {
  e.preventDefault();
  var formData = {
    id: chatId,
    text: $("#message").val(),
  };
  $.ajax({
    method: "POST",
    url: API_URL + "/chat",
    headers: {
      Authorization: "Bearer " + user.token,
    },
    data: JSON.stringify(formData),
    dataType: "json",
    contentType: "Application/json",
    success: function (data) {
      console.log(data);
    },
    error: function (request) {
      if(request.status == 401){
        localStorage.removeItem("User");
        window.location.replace("/login.html");
      }
    },
  });
}

function chatInit() {
  $.ajax({
    method: "POST",
    url: API_URL + "/chat/init",
    headers: {
      Authorization: "Bearer " + user.token,
    },
    dataType: "json",
    contentType: "Application/json",
    success: function (data) {
      chatId = data.id;
      sessionStorage.setItem("Chat", data.id);
    },
    error: function (request) {
      if(request.status == 401){
        localStorage.removeItem("User");
        window.location.replace("/login.html");
      }
    },
  });
}

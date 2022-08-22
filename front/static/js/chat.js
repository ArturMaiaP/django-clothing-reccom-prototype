var counter = 0;
function chat(e) {
  e.preventDefault();
  const message = $("#message").val();
  if(!message.trim()){
    return;
  }
  insertChat(true, message);
  var formData = {
    id: chatId,
    text: message,
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
      for(const action of data.actions){
        switch(action.action){
          case 'answer':
            insertChat(false, action.text);
            break;
          case 'recommend':
            // TODO call recommend api
            break;
        }
      }
      $("#message").val('');
    },
    error: function (request) {
      if (request.status == 401) {
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
      if (request.status == 401) {
        localStorage.removeItem("User");
        window.location.replace("/login.html");
      }
    },
  });
}

function insertChat(me, text) {
  var date = new Date();

  $("#chat-target")
    .append(
      `<div class="col-12">
        <div class="${me ? "msj-rta" : "msj"} macro">
          <div class="text ${me ? "text-r" : "text-l"}">
            <p>${text}</p>
            <p><small>${date.toLocaleDateString()}</small></p>
        </div>
      </div>`
    )
    .scrollTop($("#chat-target").prop("scrollHeight"));
}

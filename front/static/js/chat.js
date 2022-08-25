var counter = 0;
function chat(e) {
  e.preventDefault();
  const message = $("#message").val();
  if (!message.trim()) {
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
      for (const action of data.actions) {
        switch (action.action) {
          case "recommend":
            getBest();
          case "answer":
            insertChat(false, action.text);
            break;
        }
      }
      $("#message").val("");
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

function getBest() {
  $.ajax({
    method: "GET",
    url: API_URL + "/recommend/best",
    headers: {
      Authorization: "Bearer " + user.token,
    },
    dataType: "json",
    contentType: "Application/json",
    success: function (data) {
      if (!data.message) {
        insertRecomm(data.img);
      }
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
            <p><small>${date.toLocaleString()}</small></p>
        </div>
      </div>`
    )
    .scrollTop($("#chat-target").prop("scrollHeight"));
}

function insertRecomm(product) {
  var date = new Date();
  $("#chat-target")
    .append(
      `<div class="col-12">
        <div class="msj macro">
          <div class="text text-l">
            <div class="row">
              <a class="d-flex justify-content-center" data-bs-toggle="modal" data-bs-target="#chat${product.id}">
                <img src="/static/${product.name}" class="img-fluid">
              </a>
              <div id="chat${product.id}" class="modal fade">
                <div class="modal-dialog modal-lg" role="content">
                  <div class="modal-content">
                    <span data-bs-dismiss="modal" class="close text-right">×</span>
                    <img class="imgZoom align-self-center" src="/static/${product.name}">
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="btn-group">
                <input type="radio" class="btn-check" name="chat-btn${product.id}" id="chat-like${product.id}" autocomplete="off">
                <label class="btn btn-success" for="chat-like${product.id}" onclick="like('${product.name}');"><span class="fa fa-thumbs-up"></span></label>
                <input type="radio" class="btn-check" name="chat-btn${product.id}" id="chat-dislike${product.id}" autocomplete="off">
                <label class="btn btn-danger" for="chat-dislike${product.id}" onclick="dislike('${product.name}');"><span class="fa fa-thumbs-down"></span></label>
              </div>
            </div>
            <p><small>${date.toLocaleString()}</small></p>
        </div>
      </div>`
    )
    .scrollTop($("#chat-target").prop("scrollHeight"));
}

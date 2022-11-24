var counter = 0;
var group = 0;
function getRecommendation(target, fromChat = false) {
  if(group >= 15){
    $('#infiniteDivEnd').html("You reached the end. Please, choose a final skirt.");
  } else {
    $('#feedback').html('<div class="spinner-border" role="status"></div>');
    $.ajax({
      method: "GET",
      url: API_URL + "/recommend" + (chatId ? "?id=" + chatId : ""),
      headers: {
        Authorization: "Bearer " + user.token,
      },
      success: function (data) {
        $('#feedback').html('');
        group++;
        var html = `<div class="row group" id="group-${group}">`;
        for (const i of data.img_list) {
          counter++;
          html += `
              <div class="d-flex col-sm-3 column-padding">
                <div class="card col-12">
                  <div class="card-body">
                    <div class="row">
                      <a class="d-flex justify-content-center imgIn" data-bs-toggle="modal" data-bs-target="#modal${counter}">
                        <img class="img-fluid align-middle " src= "https://static.andrebezerra.com/${i}">
                      </a>
                      <div id="modal${counter}" class="modal zoom fade">
                        <div class="modal-dialog modal-lg" role="content">
                          <div class="modal-content">
                            <span data-bs-dismiss="modal" class="close text-right">&times;</span>
                            <img class="imgZoom align-self-center" src="https://static.andrebezerra.com/${i}" >
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="btn-group">
                        <input type="radio" class="btn-check" name="btn${counter}" id="like${counter}" autocomplete="off">
                        <label class="btn btn-success" for="like${counter}" onclick="like('${i}');"><span class="fa fa-thumbs-up"></span></label>
                        <input type="radio" class="btn-check" name="btn${counter}" id="finish${counter}" autocomplete="off">
                        <label class="btn btn-success" for="finish${counter}" onclick="ask_finish('${i}', '#finish${counter}');"><span class="fa fa-cart-shopping"></span></label>
                        <input type="radio" class="btn-check" name="btn${counter}" id="dislike${counter}" autocomplete="off">
                        <label class="btn btn-danger" for="dislike${counter}" onclick="dislike('${i}');"><span class="fa fa-thumbs-down"></span></label>
                      </div>
                    </div>
                  </div>
                </div>
              </div>`;
        }
        html += "</div>";
        $(target).append(html);
        if (fromChat) {
          $(".group.active").removeClass("active");
          $(`#group-${group}`).get(0).scrollIntoView();
          $(`#group-${group}`).addClass("active");
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
}

function preference(type, name) {
  var formData = {
    product: name,
  };
  $.ajax({
    method: "POST",
    url: API_URL + type,
    headers: {
      Authorization: "Bearer " + user.token,
    },
    data: JSON.stringify(formData),
    dataType: "json",
    contentType: "Application/json",
    success: function (data) {
      console.log(type + " - " + name);
    },
    error: function (request) {
      if (request.status == 401) {
        localStorage.removeItem("User");
        window.location.replace("/login.html");
      }
    },
  });
}
function ask_finish(name, id){
  finalSkirt = name;
  finalSkirtId = id;
  $('#finish-prompt').modal('show');
}
function finish(path) {
  if(finalSkirt == null){
    return false;
  }
  var formData = {
    product: finalSkirt,
  };
  $.ajax({
    method: "POST",
    url: API_URL + "/finish",
    headers: {
      Authorization: "Bearer " + user.token,
    },
    data: JSON.stringify(formData),
    dataType: "json",
    contentType: "Application/json",
    success: function (data) {
      window.location.replace(path);
    },
    error: function (request) {
      if (request.status == 401) {
        localStorage.removeItem("User");
        window.location.replace("/login.html");
      }
    },
  });
}
function closeModal(){
  if(finalSkirtId != null){
    $(finalSkirtId).prop('checked', false);
  }
  $('#finish-prompt').modal('hide');
}
function like(name) {
  return preference("/like", name);
}
function dislike(name) {
  return preference("/dislike", name);
}

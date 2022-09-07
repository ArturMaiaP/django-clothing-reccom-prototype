var counter = 0;
var group = 0;
function getRecommendation(target, scrollTo = false) {
  $.ajax({
    method: "GET",
    url: API_URL + "/recommend",
    headers: {
      Authorization: "Bearer " + user.token,
    },
    success: function (data) {
      group++;
      var html = `<div class="row group" id="group-${group}">`;
      for (const i of data.img_list) {
          counter++;
          html+=`
            <div class="d-flex col-sm-3 column-padding">
              <div class="card col-12">
                <div class="card-body">
                  <div class="row">
                    <a class="d-flex justify-content-center imgIn" data-bs-toggle="modal" data-bs-target="#modal${counter}">
                      <img class="img-fluid align-middle " src= "/static/${i}">
                    </a>
                    <div id="modal${counter}" class="modal fade">
                      <div class="modal-dialog modal-lg" role="content">
                        <div class="modal-content">
                          <span data-bs-dismiss="modal" class="close text-right">&times;</span>
                          <img class="imgZoom align-self-center" src="/static/${i}" >
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="btn-group">
                      <input type="radio" class="btn-check" name="btn${counter}" id="like${counter}" autocomplete="off">
                      <label class="btn btn-success" for="like${counter}" onclick="like('${i}');"><span class="fa fa-thumbs-up"></span></label>
                      <input type="radio" class="btn-check" name="btn${counter}" id="dislike${counter}" autocomplete="off">
                      <label class="btn btn-danger" for="dislike${counter}" onclick="dislike('${i}');"><span class="fa fa-thumbs-down"></span></label>
                    </div>
                  </div>
                </div>
              </div>
            </div>`
      }
      html+="</div>";
      $(target).append(html);
      if(scrollTo){
        $('.group.active').removeClass("active");
        $(`#group-${group}`).get(0).scrollIntoView();
        $(`#group-${group}`).addClass("active");
      }
    },
    error: function (request) {
      if(request.status == 401){
        localStorage.removeItem("User");
        window.location.replace("/login.html");
      }
    },
  });
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
      alert(request.responseText);
    },
  });
}

function like(name) {
  return preference("/like", name);
}
function dislike(name) {
  return preference("/dislike", name);
}

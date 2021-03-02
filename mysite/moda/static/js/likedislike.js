
var listRel = [];
var listIrre = [];

function addRelevant(path){
    if(listRel.includes(path)){ }
    else{
        if(listIrre.includes(path)){
            var id = listIrre.indexOf(path);
            listIrre.splice(id,1);
            listRel.push(path);
        }
        else{
            listRel.push(path);
        }
    }
}

function addIrrelevant(path){
    if(listIrre.includes(path)){}
    else{
        if(listRel.includes(path)){
            var id = listRel.indexOf(path);
            listRel.splice(id,1);
            listIrre.push(path);
        }
        else{
            listIrre.push(path);
        }
    }
}
function sendList() {
    $("#sendList").click(function () {
        $.ajax({
            method: 'POST',
            url: "smart",
            data: {'listRel[]': listRel, 'listIrrel[]': listIrre},
            success: function (request) {
                alert(request);
            },
            error: function (request) {
                alert(request.responseText);
            }
        })
    });
}

// javascript 코드

setTimeout('location.reload()',600000);

var url = new URL(location.href);
var temp = url.searchParams.get("select");

$('#' + temp).css('background-color', 'rgba(214, 214, 214, 0.3)');
$('#' + temp).css('border-radius', '6px');

check_new();
check_reply();

function check_new(){
    $.ajax({
        url:"/admin/checknew",
        type:"GET",
        success: function(result){
            if(result == "true"){
                $('.new-alarm').css('display', 'flex');
            }
        },
        error: function (request, status, error) {
            alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
        }
    })
}

function check_reply(){
    $.ajax({
        url:"/admin/checkreply",
        type:"GET",
        success: function(result){
            if(result == "true"){
                $('.new-reply').css('display', 'flex');
            }
        },
        error: function (request, status, error) {
            alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
        }
    })
}

// Button
function change_list(value){
    location.href="/admin/request_list?select=" + value + "&page=1&sort=base"
}

// Review
function show_review(){
    location.href="/admin/request_list?select=review";
}

// Log out
function logout(){
    location.href="/login";
}

// Logo
function move_to_main(){
    location.href="/";
}
// javascript 코드

var url = new URL(location.href);
var temp = url.searchParams.get("select");

$('#' + temp).css('background-color', 'rgba(214, 214, 214, 0.3)');
$('#' + temp).css('border-radius', '6px');

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
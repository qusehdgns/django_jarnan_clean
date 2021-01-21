// javascript 코드

$('.base-logout-unit').hide();

$.ajax({
    url: '/loginCheck',
    type: 'GET',
    success: function(result){
        if(result == 'true'){
            $('#base-login-button').hide();
            $('.base-logout-unit').show();
        }
    }
});

// Logo
function move_to_main(){
    location.href="/";
}
//////////

// 로그인 버튼
function move_to_login() {
    location.href = "/login";
}
//////////

// 로그아웃 버튼
function logout(){
    $.ajax({
        url: '/logout',
        type: 'GET',
        success: function(result){
            location.href="/";
        }
    });
}
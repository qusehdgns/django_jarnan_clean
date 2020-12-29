// javascript 코드

// 예약하기 버튼
function move_to_request() {
    location.href = "/request";
}
//////////

// 로그인 버튼
function move_to_login() {
    location.href = "/login";
}
//////////

// 로그아웃 버튼
function logout() {
    $.ajax({
        url : "/logout",
        type : "GET",
        success: function (result) {
            location.href="/";
        },
        error: function (request, status, error) {
            alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
        }
    });
}
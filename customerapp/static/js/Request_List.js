// javascript 코드

// 별점 저장
var scope = 5;
$('.star').find("a[value='5']").addClass("on").prevAll("a").addClass("on");

// 예약하기 버튼
function move_to_request() {
    location.href = "/request";
}
//////////

// 로그아웃 버튼
function move_to_login() {
    location.href = "/login";
}
//////////

// 테이블 선택 시
function select_request(object) {
    scope = 5;
    $('.star').find("a[value='5']").addClass("on").prevAll("a").addClass("on");
    $('.input_password').hide();
    $('.input_review').hide();
    $('.password').val("");
    $(object).next().show();
}

// 비밀번호 확인
function check_password(value) {
    var password = $("#" + value).find("input[name=readPassword]").val();

    if (password == "" || password == undefined) {
        alert("비밀번호를 입력해주세요.");
        $("#" + value).find("input[name=readPassword]").focus();
        return;
    }

    var formData = new FormData();
    formData.append('r_num', value);
    formData.append('readPassword', password);

    $.ajax({
        url: "/checkpassword",
        data: formData,
        processData: false,  // 데이터 객체를 문자열로 바꿀지에 대한 값이다. true면 일반문자...
        contentType: false,  // 해당 타입을 true로 하면 일반 text로 구분되어 진다.
        type: 'POST',
        async: false,   // 순차적 진행
        success: function (result) {
            if (result == "fail") {
                alert("비밀번호가 맞지 않습니다.");
                $("#" + value).find("input[name=readPassword]").val("");
                $("#" + value).find("input[name=readPassword]").focus();
            } else {
                $('#' + value).submit();
            }
        },
        error: function (request, status, error) {
            alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
        }
    });
}

// 별점
$('.star a').click(function () {
    $(this).parent().children("a").removeClass("on");
    $(this).addClass("on").prevAll("a").addClass("on");
    scope = $(this).attr("value")
});
//////////

// 리뷰 확인
function create_review(object, value) {
    var textIndex = $(object).prev()
    var reviewValue = textIndex.val();

    if(reviewValue == "" || reviewValue == undefined){
        alert("내용을 입력해주세요.");
        textIndex.focus();
        return;
    } else {
        $.ajax({
            url: "/review",
            type: "GET",
            data: { "r_num": value, "scope" : scope, "value" : reviewValue },
            success: function () {
                location.reload();
            },
            error: function (request, status, error) {
                alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
            }
        });
    }
}
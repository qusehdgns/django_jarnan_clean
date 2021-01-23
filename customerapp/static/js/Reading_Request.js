// javascript 코드

// 돌아가기 버튼
function move_to_request_list(){
    location.href = "/request_list";
}
//////////

// 평수 계산
var requestSize = $('#requestSize').text()
var othervalue = requestSize * 3.305785;

$('#requestSizeM').text(othervalue.toFixed(2));
//////////

// 댓글 수정 초기화 함수
function refresh_reply(object){
    $('.update_relpy').hide();
    $('.base_reply').css('display', 'flex');

    var reply = object.prev().children().next().find('span').text();
    object.prev().find("input:text").val(reply);
}

// 댓글 수정 버튼
function comment_update(object){
    var div = $(object).parent();

    refresh_reply(div);

    div.prev().children().next().hide();
    div.prev().children().next().next().css('display', 'flex');

    div.hide();
    div.next().css('display', 'flex');
}
//////////

// 댓글 삭제 버튼
function comment_delete(object){
    var id = $(object).parent().parent().find("input:hidden").val();
    
    if(confirm("해당 댓글을 정말 삭제하시겠습니까?")){
        $.ajax({
            url : '/deleteclientreply',
            type : "GET",
            data : { "id" : id },
            success : function(result){
                if(result == "success"){
                    location.reload();
                }
            },
            error: function (request, status, error) {
                alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
            }
        });
    }
}
//////////

// 댓글 확인 버튼
function update_submit(object){
    var div = $(object).parent().prev();

    var id = div.parent().find("input:hidden").val();

    var comment = div.prev().find("input:text").val();
    
    var formData = new FormData();
    formData.append('id', id);
    formData.append('comment', comment);

    $.ajax({
        url : "/updatereply",
        data : formData,
        processData: false,  // 데이터 객체를 문자열로 바꿀지에 대한 값이다. true면 일반문자...
        contentType: false,  // 해당 타입을 true로 하면 일반 text로 구분되어 진다.
        type: 'POST',
        async: false,   // 순차적 진행
        success : function(){
            location.reload();
        },
        error: function (request, status, error) {
            alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
        }
    });
}
//////////

// 댓글 취소 버튼
function update_cancel(){
    $('.update_relpy').hide();
    $('.base_reply').css('display', 'flex');
}
//////////

// 댓글달기 버튼
function request_reply(){
    var comment = $('#comment').val();
    
    if(comment == "" || comment == undefined){
        alert("댓글을 입력해주세요.");
        $('#comment').focus();
        return;
    }

    var r_num = $('#r_num').val();

    var formData = new FormData();
    formData.append('r_num', r_num);
    formData.append('comment', comment);

    $.ajax({
        url : "/clientreply",
        data : formData,
        processData: false,  // 데이터 객체를 문자열로 바꿀지에 대한 값이다. true면 일반문자...
        contentType: false,  // 해당 타입을 true로 하면 일반 text로 구분되어 진다.
        type: 'POST',
        async: false,   // 순차적 진행
        success : function(){
            location.reload();
        },
        error: function (request, status, error) {
            alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
        }
    });
}
//////////
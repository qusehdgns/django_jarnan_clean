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

// 댓글달기 버튼
function request_reply(){
    var comment = $('#comment').val();
    
    if(comment == "" || comment == undefined){
        alert("댓글을 입력해주세요.");
        $('#comment').focus();
        return;
    }

    var r_num = $('#r_num').val();
    
}
//////////
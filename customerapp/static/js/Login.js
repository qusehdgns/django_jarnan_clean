// javascript 코드

// 전화번호
$("#clientPhone").keydown(function(key) {
    if (key.keyCode == 13) {
        $("#login-action").click();
    }
});

$('#clientPhone').on('keyup', function (event) {
    var value = $(this).val();
    var addValue = [];
    value = value.replace(/[^0-9]/g, '');
    value = value.replace(/-/gi, '');

    if (value.length >= 3) {
        if (value.substring(0, 2) == '02') { // 서울 번호를 체크하기 위한 조건
            addValue.push(value.substring(0, 2));
            if (value.length >= 3) {
                var endKey = (value.length >= 10 ? 6 : 5); // 00-000-000, 00-0000-0000 처리 
                addValue.push(value.substring(2, endKey));
                if (value.length >= 6) {
                    if (value.length >= 10) { // 10자리 이상 입력 방지
                        value = value.substring(0, 10);
                    }
                    addValue.push(value.substring(endKey, value.length));
                }
            }
        } else {
            addValue.push(value.substring(0, 3));
            if (value.length >= 4) {
                var endKey = (value.length >= 11 ? 7 : 6); // 000-000-0000, 000-0000-0000 처리 
                addValue.push(value.substring(3, endKey));
                if (value.length >= 7) {
                    if (value.length >= 11) { // 11자리 이상 입력 방지
                        value = value.substring(0, 11);
                    }
                    addValue.push(value.substring(endKey, value.length));
                }
            }
        }
        $(this).val(addValue.join('-'));
    } else{
        $(this).val(value);
    }
});
//////////

// move to main 버튼
function move_to_main(){
    location.href = "/";
}

// login 버튼
function do_login(){
    var clientName = $('#clientName').val();
    var clientPhone = $('#clientPhone').val();

    if(clientName == "" || clientName == undefined){
        alert("이름을 입력해주세요.");
        $('#clientName').focus();
    } else if(clientPhone == "" || clientPhone == undefined){
        alert("전화번호를 입력해주세요.");
        $('#clientPhone').focus();
    } else{
        $('#login-form').submit();
    }
}
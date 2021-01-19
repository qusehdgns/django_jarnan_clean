// javascript 코드

// 삭제 버튼
function delete_review(object) {
    if (confirm("정말 해당 리뷰를 삭제하시겠습니까?")) {
        var id = $(object).parent().find("input:hidden").val();
        
        $.ajax({
            url: "/admin/deletereview",
            type: "GET",
            data: { "id": id },
            success: function () {
                location.reload();
            },
            error: function (request, status, error) {
                alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
            }
        });
    }
}
//////////
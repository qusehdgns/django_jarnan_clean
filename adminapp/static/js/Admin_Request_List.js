// javascript 코드

var url = new URL(location.href);
var select = url.searchParams.get("select");
var page = url.searchParams.get("page");
if (page == null) {
    page = 1;
}

// endDate
function check_endDate(){
    var endDate = $('#endDate');
    var startDate = $('#startDate').val();
    endDate.attr("min", startDate);
}
//////////

// 검색 버튼
function search_request() {
    var selectClean = new Array();

    $("input:checkbox[name=selectClean]:checked").each(function () {
        selectClean.push($(this).val());
    })

    var selectConstruct = new Array();

    $("input:checkbox[name=selectConstruct]:checked").each(function () {
        selectConstruct.push($(this).val());
    })

    var startDate = $('#startDate').val();
    var endDate = $('#endDate').val();

    if (selectClean.length == 0 &&
        selectConstruct.length == 0 &&
        startDate == "" && endDate == "") {
        return;
    }

    var newForm = $('<form></form>');

    newForm.attr("method", "POST");
    newForm.attr("action", "/admin/request_list?select=" + select + "&page=1");

    if (selectClean.length != 0) {
        newForm.append($('<input/>', { type: 'hidden', name: 'selectClean', value: selectClean }));
    }

    if (selectConstruct.length != 0){
        newForm.append($('<input/>', { type: 'hidden', name: 'selectConstruct', value: selectConstruct }));
    }

    if (startDate != ""){
        newForm.append($('<input/>', { type: 'hidden', name: 'startDate', value: startDate }));
    }

    if (endDate != ""){
        newForm.append($('<input/>', { type: 'hidden', name: 'endDate', value: endDate }));
    }

    newForm.appendTo('body');
    // submit form 
    newForm.submit();

}
//////////

// 게시물 선택
function select_request(object) {
    var r_num = $(object).find("input:hidden").val();

    location.href = "/admin/request_check?select=" + select + "&page=" + page + "&r_num=" + r_num;
}
//////////

// << 버튼
function page_start() {
    location.href = "/admin/request_list?select=" + select + "&page=1";
}
//////////

// < 버튼
function page_before() {
    location.href = "/admin/request_list?select=" + select + "&page=" + (Number(page) - 1);
}
//////////

// > 버튼
function page_next() {
    location.href = "/admin/request_list?select=" + select + "&page=" + (Number(page) + 1);
}
//////////

// >> 버튼
function page_end() {
    var endpage = $('#endPage').val();
    location.href = "/admin/request_list?select=" + select + "&page=" + endpage;
}
//////////
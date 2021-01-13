// javascript 코드

var url = new URL(location.href);
var select = url.searchParams.get("select");
var page = url.searchParams.get("page");
if(page == null){
    page = 1;
}

// 검색 버튼
function search_request(){
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

    var formData = new FormData();
    formData.append('selectClean', selectClean);
    formData.append('selectConstruct', selectConstruct);

}
//////////

// 게시물 선택
function select_request(object) {
    var r_num = $(object).find("input:hidden").val();

    location.href = "/admin/request_check?select=" + select + "&page=" + page + "&r_num=" + r_num;
}
//////////

// << 버튼
function page_start(){
    location.href = "/admin/request_list?select=" + select + "&page=1";
}
//////////

// < 버튼
function page_before(){
    location.href = "/admin/request_list?select=" + select + "&page=" + (Number(page) - 1);
}
//////////

// > 버튼
function page_next(){
    location.href = "/admin/request_list?select=" + select + "&page=" + (Number(page) + 1);
}
//////////

// >> 버튼
function page_end(){
    var endpage = $('#endPage').val();
    location.href = "/admin/request_list?select=" + select + "&page=" + endpage;
}
//////////
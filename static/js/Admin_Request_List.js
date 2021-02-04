// javascript 코드

var url = new URL(location.href);
var select = url.searchParams.get("select");
var page = url.searchParams.get("page");
var sort = url.searchParams.get("sort");
if (page == null) {
    page = 1;
}

// endDate
if ($('#startDate').val() != "") {
    check_endDate();
}

function check_endDate() {
    var endDate = $('#endDate');
    var startDate = $('#startDate').val();
    endDate.attr("min", startDate);
}
//////////

// 라디오 버튼 체크
$('input:radio[name=selectLevel]').click(function () {
    var val = $(this).data('storedValue');
    if (val) {
        $(this).prop('checked', !val);
        $(this).data('storedValue', !val);
    }
    else {
        $(this).data('storedValue', true);
        $("input[type=radio]:not(:checked)").data("storedValue", false);
    }
})

// 검색 버튼
function search_request(sort) {
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

    var selectLevel = $('input:radio[name=selectLevel]:checked').val();

    if (selectClean.length == 0 &&
        selectConstruct.length == 0 &&
        startDate == "" && endDate == "" &&
        selectLevel == undefined) {
        return;
    }

    if(startDate.length > 10){
        alert("날짜 형식을 확인해주세요.");
        $('#startDate').focus();
        return;
    } else if(endDate.length > 10){
        alert("날짜 형식을 확인해주세요.");
        $('#endDate').focus();
        return;
    }

    var newForm = $('<form></form>');

    newForm.attr("method", "POST");
    newForm.attr("action", "/admin/request_list?select=" + select + "&page=1&sort=" + sort);

    if (selectClean.length != 0) {
        newForm.append($('<input/>', { type: 'hidden', name: 'selectClean', value: selectClean }));
    }

    if (selectConstruct.length != 0) {
        newForm.append($('<input/>', { type: 'hidden', name: 'selectConstruct', value: selectConstruct }));
    }

    if (startDate != "") {
        newForm.append($('<input/>', { type: 'hidden', name: 'startDate', value: startDate }));
    }

    if (endDate != "") {
        newForm.append($('<input/>', { type: 'hidden', name: 'endDate', value: endDate }));
    }

    if (selectLevel != undefined) {
        newForm.append($('<input/>', { type: 'hidden', name: 'selectLevel', value: selectLevel }));
    }

    newForm.appendTo('body');
    // submit form 
    newForm.submit();

}
//////////

// 초기화 버튼
function reset_search() {
    location.href = "/admin/request_list?select=" + select + "&page=1&sort=base";
}
//////////

// Sorting
function select_sorting(object) {
    var select_sort = $(object).find("input:hidden").val();

    if (select_sort != sort) {
        if ($('#filter_check').val() == "true") {
            search_request(select_sort)
        } else {
            location.href = "/admin/request_list?select=" + select + "&page=1&sort=" + select_sort;
        }
    }
}

// 게시물 선택
function select_request(object) {
    var r_num = $(object).find("input:hidden").val();

    location.href = "/admin/request_check?select=" + select + "&page=" + page + "&sort=" + sort + "&r_num=" + r_num;
}
//////////

// << 버튼
function page_start() {
    location.href = "/admin/request_list?select=" + select + "&page=1&sort=" + sort;
}
//////////

// < 버튼
function page_before() {
    location.href = "/admin/request_list?select=" + select + "&page=" + (Number(page) - 1) + "&sort=" + sort;
}
//////////

// > 버튼
function page_next() {
    location.href = "/admin/request_list?select=" + select + "&page=" + (Number(page) + 1) + "&sort=" + sort;
}
//////////

// >> 버튼
function page_end() {
    var endpage = $('#endPage').val();
    location.href = "/admin/request_list?select=" + select + "&page=" + endpage + "&sort=" + sort;
}
//////////
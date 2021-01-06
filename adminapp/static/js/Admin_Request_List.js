// javascript 코드

function select_request(object) {
    var url = new URL(location.href);
    var select = url.searchParams.get("select");

    var r_num = $(object).find("input:hidden").val();

    location.href = "/admin/request_check?select=" + select + "&r_num=" + r_num;
}
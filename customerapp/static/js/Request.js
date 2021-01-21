// javascript 코드

// 전화번호
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
    } else {
        $(this).val(value);
    }
});
//////////

// 요청 주소
var area0 = ["시/도 선택", "서울특별시", "인천광역시", "대전광역시", "광주광역시", "대구광역시", "울산광역시", "부산광역시", "경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주도"];
var area1 = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"];
var area2 = ["계양구", "남구", "남동구", "동구", "부평구", "서구", "연수구", "중구", "강화군", "옹진군"];
var area3 = ["대덕구", "동구", "서구", "유성구", "중구"];
var area4 = ["광산구", "남구", "동구", "북구", "서구"];
var area5 = ["남구", "달서구", "동구", "북구", "서구", "수성구", "중구", "달성군"];
var area6 = ["남구", "동구", "북구", "중구", "울주군"];
var area7 = ["강서구", "금정구", "남구", "동구", "동래구", "부산진구", "북구", "사상구", "사하구", "서구", "수영구", "연제구", "영도구", "중구", "해운대구", "기장군"];
var area8 = ["고양시", "과천시", "광명시", "광주시", "구리시", "군포시", "김포시", "남양주시", "동두천시", "부천시", "성남시", "수원시", "시흥시", "안산시", "안성시", "안양시", "양주시", "오산시", "용인시", "의왕시", "의정부시", "이천시", "파주시", "평택시", "포천시", "하남시", "화성시", "가평군", "양평군", "여주군", "연천군"];
var area9 = ["강릉시", "동해시", "삼척시", "속초시", "원주시", "춘천시", "태백시", "고성군", "양구군", "양양군", "영월군", "인제군", "정선군", "철원군", "평창군", "홍천군", "화천군", "횡성군"];
var area10 = ["제천시", "청주시", "충주시", "괴산군", "단양군", "보은군", "영동군", "옥천군", "음성군", "증평군", "진천군", "청원군"];
var area11 = ["계룡시", "공주시", "논산시", "보령시", "서산시", "아산시", "천안시", "금산군", "당진군", "부여군", "서천군", "연기군", "예산군", "청양군", "태안군", "홍성군"];
var area12 = ["군산시", "김제시", "남원시", "익산시", "전주시", "정읍시", "고창군", "무주군", "부안군", "순창군", "완주군", "임실군", "장수군", "진안군"];
var area13 = ["광양시", "나주시", "목포시", "순천시", "여수시", "강진군", "고흥군", "곡성군", "구례군", "담양군", "무안군", "보성군", "신안군", "영광군", "영암군", "완도군", "장성군", "장흥군", "진도군", "함평군", "해남군", "화순군"];
var area14 = ["경산시", "경주시", "구미시", "김천시", "문경시", "상주시", "안동시", "영주시", "영천시", "포항시", "고령군", "군위군", "봉화군", "성주군", "영덕군", "영양군", "예천군", "울릉군", "울진군", "의성군", "청도군", "청송군", "칠곡군"];
var area15 = ["거제시", "김해시", "마산시", "밀양시", "사천시", "양산시", "진주시", "진해시", "창원시", "통영시", "거창군", "고성군", "남해군", "산청군", "의령군", "창녕군", "하동군", "함안군", "함양군", "합천군"];
var area16 = ["서귀포시", "제주시", "남제주군", "북제주군"];

$("select[name=firstAddress]").each(function () {
    var firstAddress = $(this);
    $.each(eval(area0), function () {
        firstAddress.append("<option value='" + this + "'>" + this + "</option>");
    });
    $('#secondAddress').append("<option value=''>구/군 선택</option>");
});

$("select[name=firstAddress]").change(function () {
    var area = "area" + $("option", $(this)).index($("option:selected", $(this))); // 선택지역의 구군 Array
    var secondAddress = $('#secondAddress');// 선택영역 군구 객체
    $("option", secondAddress).remove(); // 구군 초기화

    if (area == "area0")
        secondAddress.append("<option value=''>구/군 선택</option>");
    else {
        $.each(eval(area), function () {
            secondAddress.append("<option value='" + this + "'>" + this + "</option>");
        });
    }
});
//////////

// 평수 및 크기
$('#requestSize').on('keyup', function (event) {
    var value = $(this).val();
    value = value.replace(/[^\.0-9]/g, '');

    $(this).val(value);

    var othervalue = value * 3.305785;

    $('#requestSizeM').val(othervalue.toFixed(2));
});

$('#requestSizeM').on('keyup', function (event) {
    var value = $(this).val();
    value = value.replace(/[^\.0-9]/g, '');

    $(this).val(value);

    var othervalue = value * 0.3025;

    $('#requestSize').val(othervalue.toFixed(2));
});
//////////

// 요청 날짜 기본값 설정
var date = new Date();
var year = date.getFullYear();
var month = new String(date.getMonth() + 1);
var day = new String(date.getDate() + 1);

if (month.length == 1) {
    month = "0" + month;
}
if (day.length == 1) {
    day = "0" + day;
}

var today = year + "-" + month + "-" + day;


$("#requestDate").attr("min", today);

$("#requestDate").val(today);
//////////

// checkbox 선택
function label_click_check(object){
    $(object).prev().trigger('click');
}

// 확인 버튼
function submit_action() {
    var clientName = $('#clientName').val();

    if (clientName == "" || clientName == undefined) {
        alert("예약자 성함을 입력해주세요.");
        $('#clientName').focus();
        return;
    }

    var clientPhone = $('#clientPhone').val();

    if (clientPhone == "" || clientPhone == undefined) {
        alert("예약자 전화번호을 입력해주세요.");
        $('#clientPhone').focus();
        return;
    } else if(clientPhone.length < 11){
        alert("예약자 전화번호을 올바르게 입력해주세요.");
        $('#clientPhone').focus();
        return;
    }

    var firstAddress = $('#firstAddress option:selected').val();

    if (firstAddress == "시/도 선택" || firstAddress == undefined) {
        alert("주소를 정확히 입력해주세요.");
        $('#firstAddress').focus();
        return;
    }

    var secondAddress = $('#secondAddress option:selected').val();

    if (secondAddress == "" || secondAddress == undefined) {
        alert("주소를 정확히 입력해주세요.");
        $('#secondAddress').focus();
        return;
    }

    var requestAddress = firstAddress + " " + secondAddress;

    var requestSize = $('#requestSize').val();

    if(requestSize == "" || requestSize == undefined){
        alert("크기를 입력해주세요.");
        $('#requestSize').focus();
        return;
    }

    var requestSizeM = $('#requestSizeM').val();

    if(requestSize == "NaN" || requestSizeM == "NaN"){
        alert("크기를 올바르게 입력해주세요.");
        $('#requestSize').focus();
        return;
    }

    var requestDate = $('#requestDate').val();

    var requestLevel = $('input:radio[name=requestLevel]:checked').val();

    var requestClean = new Array();

    $("input:checkbox[name=requestClean]:checked").each(function () {
        requestClean.push($(this).val());
    })

    if (requestClean.length == 0) {
        alert("청소 항목을 선택해주세요.");
        return;
    }

    var requestConstruct = new Array();

    $("input:checkbox[name=requestConstruct]:checked").each(function () {
        requestConstruct.push($(this).val());
    })

    if (requestConstruct.length == 0) {
        alert("시공 항목을 선택해주세요.");
        return;
    }

    var requestMemo = $('#requestMemo').val();

    var readPassword = $('#readPassword').val();

    if (readPassword.length < 4) {
        alert("비밀번호를 4자 이상으로 설정해주세요.");
        $('#readPassword').focus();
        return;
    }

    var showLevel = "클래식";

    if(requestLevel != "false"){
        showLevel = "프리미엄";
    }

    var result = "예약자 : " + clientName
        + "\n전화번호 : " + clientPhone
        + "\n주소 : " + requestAddress
        + "\n크기 : " + requestSize + " 평 / " + requestSizeM + " m^2"
        + "\n날짜 : " + requestDate
        + "\n단계 : " + showLevel
        + "\n청소 항목 : " + requestClean
        + "\n시공 항목 : " + requestConstruct;

    if (requestMemo != "" && requestMemo != undefined) {
        result += "\n요청 사항 : " + requestMemo;
    }

    if (!confirm(result)) {
        return;
    }

    var formData = new FormData();
    formData.append('clientName', clientName);
    formData.append('clientPhone', clientPhone);
    formData.append('requestAddress', requestAddress);
    formData.append('requestSize', requestSize);
    formData.append('requestDate', requestDate);
    formData.append('requestLevel', requestLevel);
    formData.append('requestClean', requestClean);
    formData.append('requestConstruct', requestConstruct);
    formData.append('requestMemo', requestMemo);
    formData.append('readPassword', readPassword);

    $.ajax({
        url: "/client_request",
        data: formData,  //위에서 선언한 fromdata
        processData: false,  // 데이터 객체를 문자열로 바꿀지에 대한 값이다. true면 일반문자...
        contentType: false,  // 해당 타입을 true로 하면 일반 text로 구분되어 진다.
        type: 'POST',
        async: false,   // 순차적 진행
        success : function(result){
            alert(result);
            location.href = "/request_list";
        },
        error: function (request, status, error) {
            alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
        }
    });
}
//////////


// 취소 버튼
function move_to_main() {
    location.href = "/";
}
//////////
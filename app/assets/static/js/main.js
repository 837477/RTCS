function ajax(url, _type, document) {
    var result;
    $.ajax({
        contentType: 'application/json',
        type: _type,
        url: url,
        async: false,
        data: document,
        datatype: "json",
        success: function(data){
            result = data
        },
        error:function(res){
            result = null;
        }
    });
    return result;
}


function today() {
    let today = new Date();   

    let year = today.getFullYear(); // 년도
    let month = today.getMonth() + 1;  // 월
    let date = today.getDate();  // 날짜
    let day = today.getDay();  // 요일

    return year + "." + month + "." + date;
}

$(document).ready(function(){
    // patients
    text = '<span class="icon"><i class="mdi mdi-finance"></i></span> COVID-19 Real-Time Patients Status ('+ today() + ')';
    document.getElementById('patients').innerHTML = text;
    
    data = ajax("/api/v1/patients/status", "GET", null);
    document.getElementById('국내 확진자').innerHTML = data['국내 확진자']['value'];
    document.getElementById('전국 추가 확진자').innerHTML = data['전국 추가 확진']['value'];
    document.getElementById('국내 치료중').innerHTML = data['국내 치료중']['value'];
    document.getElementById('국내 사망자').innerHTML = data['전국 사망']['value'];
    document.getElementById('서울시 확진자').innerHTML = data['서울시 확진자']['value'];
    document.getElementById('서울시 추가 확진자').innerHTML = data['서울시 추가 확진']['value'];
    document.getElementById('서울시 치료중').innerHTML = data['서울시 치료중']['value'];
    document.getElementById('서울시 사망자').innerHTML = data['서울시 사망']['value'];


    // vaccine
    data = ajax("/api/v1/vaccine/status", "GET", null);
    text = '<span class="icon"><i class="mdi mdi-finance"></i></span> COVID-19 Real-Time Vaccine Status ('+ data['접종일']['value'] + ')';
    document.getElementById('vaccine').innerHTML = text;

    document.getElementById('1차 접종자 누계').innerHTML = data['1차접종 누계']['value'];
    document.getElementById('1차 접종률').innerHTML = data['1차접종률(%)']['value'] + " %";
    document.getElementById('2차 접종자 누계').innerHTML = data['2차접종 누계']['value'];
    document.getElementById('2차 접종률').innerHTML = data['2차접종률(%)']['value'] + " %";

});
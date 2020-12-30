$(function () {
    // Geolocation API에 액세스할 수 있는지를 확인
    if (navigator.geolocation) {
        //위치 정보를 얻기
        navigator.geolocation.getCurrentPosition(function (pos) {
            // var latitude = pos.coords.latitude;
            // var longitude = pos.coords.longitude;
            $('#latitude').val(pos.coords.latitude);     // 위도
            $('#longitude').val(pos.coords.longitude); // 경도
        });
    } else {
        alert("이 브라우저에서는 Geolocation이 지원되지 않습니다.")
    }
});
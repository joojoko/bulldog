var map = new kakao.maps.Map(document.getElementById('map'), { // 지도를 표시할 div
    center: new kakao.maps.LatLng(36.2683, 127.6358), // 지도의 중심좌표
    level: 14 // 지도의 확대 레벨
});
var clusterer = new kakao.maps.MarkerClusterer({
    map: map, // 마커들을 클러스터로 관리하고 표시할 지도 객체
    averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정
    minLevel: 10 // 클러스터 할 최소 지도 레벨
});
// 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption);
var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(37.4923615, 127.02928809999999), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };
// var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
// 마커가 표시될 위치입니다
$.get("file:///D:/Pycharm_pro/Django_Web/media/location/location.json", function (data) {
    // 데이터에서 좌표 값을 가지고 마커를 표시합니다
    // 마커 클러스터러로 관리할 마커 객체는 생성할 때 지도 객체를 설정하지 않습니다
    var markers = $(data.location).map(function (i, position) {
        return new kakao.maps.Marker({
            position: new kakao.maps.LatLng(location.latitude, location.longitude)
        });
    });
    clusterer.addMarkers(markers);
});
//     var markerPosition = new kakao.maps.LatLng(37.4923615, 127.02928809999999);
// // 마커를 생성합니다
//     var marker = new kakao.maps.Marker({
//         position: markerPosition
//     });
// 마커가 지도 위에 표시되도록 설정합니다
//     markers.setMap(map);
// 아래 코드는 지도 위의 마커를 제거하는 코드입니다
// marker.setMap(null);
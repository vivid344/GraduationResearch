/**
 * Created by Miyoshi on 2017/10/15.
 */

var map;
var marker = [];
var infoWindow = [];
var currentInfoWindow = null;
var view;

function init() {
    map = new google.maps.Map(document.getElementById('map'), { // #mapの初期化
        center: { // 地図の中心を指定
            lat: 41.77627, // 緯度
            lng: 140.7283694 // 経度
        },
        zoom: 13 // 地図のズームを指定
    });

    var url = "/api/set_up/";
    setmarker(url);
}

function search() {
    marker.forEach(function (marker, idx) {
        marker.setMap(null);
    });
    var url;
    var price = parseInt($('#price').val());
    var category = $('#category').val();
    var birth = parseInt($('#birth').val());
    var old_shop = parseInt($('#old-shop').val());
    var only = parseInt($('#only').val());
    var popular = parseInt($('#popular').val());

    var tmp_url = "/api/recommend/?format=json&price=";
    var add_value = "&birth=" + birth + "&old_shop=" + old_shop + "&only=" + only + "&popular=" + popular;

    if (category == "指定なし") {
        category = "";
    }

    if (isNaN(price)) {
        price = "";
    }
    url = tmp_url + price + "&category=" + category + add_value;
    setmarker(url);
}

function setmarker(url) {
    if(url == '/api/set_up/') {
        $("#load").css('display', 'block');
        $("#background").css('display', 'block');
    }

    $.ajax({
        url: url,
        type: "GET",
        async: true,
    }).done(function (data, textStatus, jqXHR) {
        $("#load").css('display', 'none');
        $("#background").css('display', 'none');
        getshopdata = data;
        if (typeof getshopdata == "string") {
            getshopdata = JSON.parse(getshopdata);
        }

        for (var i = 0; i < getshopdata.length; i++) {

            markerLatLng = new google.maps.LatLng({
                lat: parseFloat(getshopdata[i].lat),
                lng: parseFloat(getshopdata[i].lng)
            }); // 緯度経度のデータ作成

            marker[i] = new google.maps.Marker({ // マーカーの追加
                position: markerLatLng, // マーカーを立てる位置を指定
                map: map, // マーカーを立てる地図を指定
            });


            infoWindow[i] = new google.maps.InfoWindow({ // 吹き出しの追加
                content: '<div class="sample">' + getshopdata[i].shopname + '</div>' // 吹き出しに表示する内容
            });
            recommend(getshopdata);
            markerEvent(i, getshopdata[i].id); // マーカーにクリックイベントを追加

        }
    }).fail(function (jqXHR, textStatus, errorThrown) {
    });
}
function recommend(json) {
    $("#result1").empty();
    $("#result2").empty();
    view = true;
    var len = json.length;

    for (var i = 0; i < len; i++) {//左右の振り分けを行う
        if (i % 2 == 0) {
            $("#result1").append('<div style="height:25%;box-sizing:border-box; border-bottom: 1px solid #CCCCCC;padding-top: 1.5em"><img src="' + json[i].url + '" height="100px">' +
                "<div style='text-align: left;margin-left: 1em'>" + json[i].shopname + "</div>" +
                "<div style='text-align: left;margin-left: 1em;font-size: 120%'>" + json[i].name + "</div>" +
                "<div style='text-align: right;margin-right: 1em;'>" + '効用:' + json[i].utility + '　　価格:' + json[i].price + "円</div></div>");
        } else {
            $("#result2").append('<div style="height:25%;box-sizing:border-box; border-bottom: 1px solid #CCCCCC;padding-top: 1.5em"><img src="' + json[i].url + '" height="100px">' +
                "<div style='text-align: left;margin-left: 1em'>" + json[i].shopname + "</div>" +
                "<div style='text-align: left;margin-left: 1em;font-size: 120%'>" + json[i].name + "</div>" +
                "<div style='text-align: right;margin-right: 1em;'>" + '効用:' + json[i].utility + '　　価格:' + json[i].price + "円</div></div>");
        }
    }
}


//以下は使ってない
function setfood(url, x) {
    $("#foodlist").empty();
    $.ajax({
        url: url,
        type: "GET",
        async: false,
        timeout: 10000,
    }).done(function (data, textStatus, jqXHR) {
        getmenudata = data;
    }).fail(function (jqXHR, textStatus, errorThrown) {
    });

    var i;

    var price = parseInt($('#price').val());
    var flg = 0;
    for (i = 0; i < getmenudata.length; i++) {
        if (getmenudata[i].price != 0) {
            if (isNaN(price)) {
                flg = 1;
                $("#foodlist").append("<tr><td class='mdl-data-table__cell--non-numeric' style='white-space: pre-wrap'>" + getmenudata[i].name + "</td><td>" + getmenudata[i].price + "</td></tr>");
            } else if (getmenudata[i].price <= price) {
                flg = 1;
                $("#foodlist").append("<tr><td class='mdl-data-table__cell--non-numeric' style='white-space: pre-wrap'>" + getmenudata[i].name + "</td><td>" + getmenudata[i].price + "</td></tr>");
            }
        }
    }

    if (flg == 0)
        $("#foodlist").append("<tr><td class='mdl-data-table__cell--non-numeric' style='white-space: pre-wrap' colspan='2'>該当する商品はありません</td></tr>")
}

function markerEvent(i, id) {
    marker[i].addListener('click', function () { // マーカーをクリックしたとき
        if (currentInfoWindow)
            currentInfoWindow.close();
        infoWindow[i].open(map, marker[i]); // 吹き出しの表示
        currentInfoWindow = infoWindow[i];
        // var url;
        // url = "/Food/Foods/?shop=" + id;
        // setfood(url, i);
    });
}
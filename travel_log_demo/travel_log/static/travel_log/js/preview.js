$(document).ready(function () {

    var hidden_ratings = $("div[name*=hidden_rating_]");
    var rating_divs = $("div[name^=rating]");

    for (var i = 0; i < rating_divs.length; i++) {
        $(rating_divs[i]).raty({ number: 10,
            readOnly: true,
            score: parseInt(hidden_ratings[i].innerHTML)
        });
    }


    function initialize(x) {
        var mapOptions = {
            center: new google.maps.LatLng(x, 150.644),
            zoom: 8
        };
        var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);
    }
    google.maps.event.addDomListener(window, 'load', initialize(-34.397));
});
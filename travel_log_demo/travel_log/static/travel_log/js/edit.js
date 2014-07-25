/**
 * Created by abhishekanurag on 7/24/14.
 */
$(document).ready(function () {

    //Raty Integration
    var hidden_ratings = $("div[name*=hidden_rating_]");
    var rating_divs = $("div[name^=rating]");

    for (var i = 0; i < rating_divs.length; i++) {
        $(rating_divs[i]).raty({ number: 10,
            score: parseInt(hidden_ratings[i].innerHTML)
        });
    }
    //Raty integration end

    //Fix map div height
    var left_ht = $("#details").height();
    if (left_ht > 300) {
        $("#map-canvas").height(left_ht);
    }


    //Google maps integration
    function mapInitialize() {
        var mapOptions = {
            center: new google.maps.LatLng(0, 0),
            zoom: 3
        };
        var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);


        function placeMarker(location) {
            var marker = new google.maps.Marker({
                position: location,
                map: map
            });

            map.setCenter(location);
        }


        var lat_divs = $("div[name*=hidden_lat_]");
        var lng_divs = $("div[name*=hidden_lng_]");
        var path_coords = [];
        var lat, lng, location;
        for (var i = 0; i < lat_divs.length; i++) {
            lat = parseFloat(lat_divs[i].innerHTML);
            lng = parseFloat(lng_divs[i].innerHTML);
            location = new google.maps.LatLng(lat, lng);
            placeMarker(location);
            path_coords.push(location);
        }

        var path = new google.maps.Polyline({
            path: path_coords,
            geodesic: true,
            strokeColor: '#FF0000',
            strokeOpacity: 1.0,
            strokeWeight: 2
        });
        path.setMap(map);
    }

    google.maps.event.addDomListener(window, 'load', mapInitialize());

    //Google maps Integration end

    //Tie delete
    var delete_buttons = $("button[name*=delete_dest_]");

    for (var i = 0; i < delete_buttons.length; i++) {
        button = delete_buttons[i];
        $(button).click(function () {
            var name_str = "#dest_" + i;
            alert(name_str);
            $(name_str).remove();
            //$(button).remove();

        })
    }

});
$(document).ready(function () {

    //Raty Integration
    var trip_containers = $("div[name*=trip_container_]");
    for(var trip=0; trip<trip_containers.length; trip++){
        var trip_container_selector = "div[name=trip_container_"+trip+"]";
        var hidden_ratings = $(trip_container_selector).find("div[name*=hidden_rating_]");
        var rating_divs = $(trip_container_selector).find("div[name^=rating]");

        for (var i = 0; i < rating_divs.length; i++) {
            $(rating_divs[i]).raty({ number: 10,
                readOnly: true,
                score: parseInt(hidden_ratings[i].innerHTML)
            });
        }
    }


    //Raty integration end


    //Google maps integration
    function mapInitialize(i) {
        var mapOptions = {
            center: new google.maps.LatLng(0, 0),
            zoom: 3
        };
        var map = new google.maps.Map(document.getElementById("map-canvas_"+i),
            mapOptions);


        function placeMarker(location) {
            var marker = new google.maps.Marker({
                position: location,
                map: map
            });

            map.setCenter(location);
        }

        var trip_container_selector = "div[name=trip_container_"+i+"]";
        var lat_divs = $(trip_container_selector).find("div[name*=hidden_lat_]");
        var lng_divs = $(trip_container_selector).find("div[name*=hidden_lng_]");
        var path_coords = [];
        var lat, lng, location;
        var bounds = new google.maps.LatLngBounds ();
        for (var i = 0; i < lat_divs.length; i++) {
            lat = parseFloat(lat_divs[i].innerHTML);
            lng = parseFloat(lng_divs[i].innerHTML);
            location = new google.maps.LatLng(lat, lng);
            bounds.extend (location);
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
        map.fitBounds(bounds);

    }

    for(var trip=0; trip<trip_containers.length; trip++){
        google.maps.event.addDomListener(window, 'load', mapInitialize(trip));
    }


    //Google maps Integration end
});
$(document).ready(function () {

    //Raty Integration
    var hidden_ratings = $("div[name*=hidden_rating_]");
    var rating_divs = $("div[name^=rating]");

    for (var i = 0; i < rating_divs.length; i++) {
        $(rating_divs[i]).raty({ number: 10,
            readOnly: true,
            score: parseInt(hidden_ratings[i].innerHTML)
        });
    }
    //Raty integration end

    //Put current URL in FB share
    $(".fb-like").attr('data-href',window.location);


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


        function placeMarker(location, dest_number, tooltip) {
            var icon_url = "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=" + dest_number + "|F7685C|000000"
            var marker_img = new google.maps.MarkerImage(icon_url,
                new google.maps.Size(21, 34),
                new google.maps.Point(0, 0),
                new google.maps.Point(10, 34));
            var infowindow = new google.maps.InfoWindow({
                content: tooltip,
            });
            var marker = new google.maps.Marker({
                position: location,
                map: map,
                icon: marker_img
            });
            google.maps.event.addListener(marker, 'mouseover', function () {
                infowindow.open(map, marker);
            });
            google.maps.event.addListener(marker, 'mouseout', function () {
                infowindow.close();
            });
        }


        var lat_divs = $("div[name*=hidden_lat_]");
        var lng_divs = $("div[name*=hidden_lng_]");
        var name_heads = $("h4[name^=dest_name_]");
        var path_coords = [];
        var lat, lng, location;
        var bounds = new google.maps.LatLngBounds();
        for (var i = 0; i < lat_divs.length; i++) {
            lat = parseFloat(lat_divs[i].innerHTML);
            lng = parseFloat(lng_divs[i].innerHTML);
            location = new google.maps.LatLng(lat, lng);
            bounds.extend(location);
            placeMarker(location, i + 1, '<div class="map-tooltip">'+name_heads[i].innerHTML+'</div>');
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

    google.maps.event.addDomListener(window, 'load', mapInitialize());

    //Google maps Integration end
});
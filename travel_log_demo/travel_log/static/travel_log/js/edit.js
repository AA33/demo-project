/**
 * Created by abhishekanurag on 7/24/14.
 */
$(document).ready(function () {

    //Raty Integration
    var hidden_ratings = $("div[name*=hidden_rating_]");
    var rating_divs = $("div[name^=rating]");
    var rating_edits = $("input[name^=rating_edit_]");

    for (var i = 0; i < rating_divs.length; i++) {
        $(rating_divs[i]).raty({ number: 10,
            score: parseInt(hidden_ratings[i].innerHTML),
            click: function (score, evt) {
                var select = "#" + this.id + "_edit";
                $(select).val(score);
            }
        });
    }
    //Raty integration end

    //Fix map div height
    var left_ht = $("#details").height();
    if (left_ht > 300) {
        $("#map-canvas").height(left_ht);
    }


    //Set default dates
    Date.prototype.toDateInputValue = (function () {
        var local = new Date(this);
        local.setMinutes(this.getMinutes() - this.getTimezoneOffset());
        return local.toJSON().slice(0, 10);
    });
    var sdate = $("#start_date").get(0).innerHTML;
    var lasti = sdate.lastIndexOf(",");
    sdate = sdate.substring(0, lasti);
    var sDate_obj = new Date(sdate);
    $("#start_date_edit").val(sDate_obj.toDateInputValue());

    sdate = $("#end_date").get(0).innerHTML;
    lasti = sdate.lastIndexOf(",");
    sdate = sdate.substring(0, lasti);
    sDate_obj = new Date(sdate);
    $("#end_date_edit").val(sDate_obj.toDateInputValue());
    //Done


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

        //Adding destinations
        function addDest(event) {
            var dests = $("li[id^=dest]");
            var clone_dest = $(dests[dests.length - 1]).clone();
            var idx = parseInt(clone_dest.get(0).id.substring(clone_dest.get(0).id.lastIndexOf("_") + 1)) + 1;
            clone_dest.id = "dest_" + idx;
            var clone_children = $(clone_dest).children();

            clone_children[0].id = "destination_name_edit_" + idx;
            $(clone_children[0]).val("");
            clone_children[1].name = "rating_" + idx;
            //$(clone_children[1]).raty("score", 5);
            clone_children[2].name = "rating_" + idx + "_edit";
            clone_children[2].val = 5;
            clone_children[3].name = "hidden_rating_" + idx;
            $(clone_children[3]).html("5");
            clone_children[4].name = "hidden_lat_" + idx;
            $(clone_children[4]).html(event.latLng.lat());
            clone_children[5].name = "hidden_lng_" + idx;
            $(clone_children[5]).html(event.latLng.lng());
            clone_children[6].name = "destination_desc_edit_" + idx;
            $(clone_children[6]).html("");

            $(clone_dest).appendTo("#destinations");
            $(clone_dest).append('<br><br>');

        }
        //End
    }

    google.maps.event.addDomListener(window, 'load', mapInitialize());
    //Google maps Integration end



});
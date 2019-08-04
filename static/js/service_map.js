/*$(document).ready(function(){


			//create a map
			mapboxgl.accessToken = 'pk.eyJ1IjoibXNhbWlyIiwiYSI6ImNqdGphZWVkZDBzd3M0YWtpM2Y0bzhhNG4ifQ.CIn3tX2_VC_N0hMh1lzAGg';
			const map = new mapboxgl.Map({
			  container: 'map1',
			  style: 'mapbox://styles/msamir/cjtkion1e2tux1fnrxdhvs5lc',
			  center: [3.424100, 36.780000],
			  zoom: 9.0
			});


			
			var endpint = "/services/get_data/"
			
			$.ajax({
				method : "GET",
				url : endpint,
				success: function(geojson){


				geojson.features.forEach(function(marker) {
		        var el = document.createElement('div');
		        el.className = 'marker';
		        el.style.backgroundImage = "url(/static/images/" + marker.properties.type +".png";
		        el.style.width = '40px';
		        el.style.height = '55px';
		     
			    // create the popup
			    var popup = new mapboxgl.Popup({ offset: 25 })
			    .setHTML('<h1> ' +marker.properties.type+ '</h1> <br><button type="submit" class="btn btn-primary">Ajouter</button>');
			     
			     
			    // add marker to map
			    new mapboxgl.Marker(el)
			    .setLngLat(marker.geometry.coordinates).setPopup(popup)
			    .addTo(map);
			      });

				}
			});  



			//Geo Coder (search)
			var acctok = map.addControl(new MapboxGeocoder({
			accessToken: mapboxgl.accessToken
			}));


			//get user location using button
			var uloc = map.addControl(new mapboxgl.GeolocateControl({
			    positionOptions: {
			        enableHighAccuracy: true
			    },
			    trackUserLocation: true
			}));

			//zoom in and zoom out using button
			var nav = new mapboxgl.NavigationControl();
			var cont = map.addControl(nav, 'top-right');


})
     */
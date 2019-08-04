 

 $(document).ready(function(){
      
         mapboxgl.accessToken = 'pk.eyJ1IjoibXNhbWlyIiwiYSI6ImNqdGphZWVkZDBzd3M0YWtpM2Y0bzhhNG4ifQ.CIn3tX2_VC_N0hMh1lzAGg';
      const map = new mapboxgl.Map({
        container: 'map1',
        style: 'mapbox://styles/msamir/cjtkion1e2tux1fnrxdhvs5lc',
        center: [3.424100, 36.780000],
        zoom: 9.0,
      });
      

      //Geo Coder (search)
      var acctok = map.addControl(new MapboxGeocoder({
      accessToken: mapboxgl.accessToken
      }));

      //zoom in and zoom out using button
      var nav = new mapboxgl.NavigationControl();
      var cont = map.addControl(nav, 'top-right');
      
      var marker = new mapboxgl.Marker();

      //get user location
      var getcoor = document.getElementById('getcoordinates');
      var marker = new mapboxgl.Marker();
      
      function RespondClick() {
        marker.remove(); 
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(position => { 
            document.getElementById('lang').value=position.coords.longitude;
            document.getElementById('lat').value= position.coords.latitude;
            // add marker to map
            

            marker  = new mapboxgl.Marker({
              draggable: false
              })
              .setLngLat([position.coords.longitude, position.coords.latitude])
              .addTo(map);


            map.flyTo({center: [position.coords.longitude, position.coords.latitude], zoom: 11});
              // 
            });
        }
      }
      getcoor.addEventListener("click", RespondClick);


      


      // set a marker on user location on map click
      map.on('click', function(e) {
        marker.remove();

        if ("geolocation" in navigator) { 
            navigator.geolocation.getCurrentPosition(position => { 
              document.getElementById('lang').value=e.lngLat.lng;
              document.getElementById('lat').value= e.lngLat.lat;
              
              // add marker to map
              marker  = new mapboxgl.Marker({
                draggable: false
                })
                .setLngLat([e.lngLat.lng, e.lngLat.lat])
                .addTo(map);


            });   
        };
         
      });


/*
      function onDragEnd() {

         var lngLat = marker.getLngLat();

         document.getElementById('lang').value= lngLat.lng;
         document.getElementById('lat').value= lngLat.lat;
         window.alert("hiiii");
         marker.on('dragend', onDragEnd);
         


      
      //get user location using button
      var u = new mapboxgl.GeolocateControl({
          positionOptions: {
              enableHighAccuracy: true
          },
          trackUserLocation: true
      });
      var uloc = map.addControl(u);

      

   





      // set a marker on user location on map click
      uloc.on('click', function(e) {
        marker.remove();

        if ("geolocation" in navigator) { 
            navigator.geolocation.getCurrentPosition(position => { 
                document.getElementById('lang').value=e.lngLat.lng;
                document.getElementById('lat').value= e.lngLat.lat;
                


                // add marker to map
                marker  = new mapboxgl.Marker({
              draggable: true
              })
              .setLngLat([e.lngLat.lng, e.lngLat.lat])
              .addTo(map);


            });   
        
           

          };
         
        });
         

      

      
         function onDragEnd() {

         var lngLat = marker.getLngLat();

         document.getElementById('lang').value= lngLat.lng;
         document.getElementById('lat').value= lngLat.lat;
         window.alert("hiiii");
         }
         
      marker.on('click', onDragEnd);



         

*/
    })
     
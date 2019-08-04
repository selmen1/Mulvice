/*$( document ).ready(function() {
	//create a map
mapboxgl.accessToken = 'pk.eyJ1IjoibXNhbWlyIiwiYSI6ImNqdGphZWVkZDBzd3M0YWtpM2Y0bzhhNG4ifQ.CIn3tX2_VC_N0hMh1lzAGg';
const map = new mapboxgl.Map({
  container: 'all-serv-map',
  style: 'mapbox://styles/msamir/cjtkion1e2tux1fnrxdhvs5lc',
  center: [3.424100, 36.780000],
  zoom: 9.0
});



// Add geolocate control to the map.
map.addControl(new mapboxgl.GeolocateControl({
positionOptions: {
enableHighAccuracy: true
},
trackUserLocation: true
}));

//zoom in and zoom out using button
var nav = new mapboxgl.NavigationControl();
var cont = map.addControl(nav, 'top-right');
	


var el = document.createElement('div');
el.className = 'mar';
el.style.backgroundImage = 'url(https://servicefinder.wyzi-directory-theme.com/wp-content/uploads/2016/12/mapicon-paint.png)';

el.style.width = '40px';
el.style.height = '55px';

	
var marker = new mapboxgl.Marker(el,{
	color: '#bfecae',
	draggable: true})
  .setLngLat([3.304100, 36.750000])
  .addTo(map);



function onDragEnd() {
	//getting Longitude and Latitude
var lngLat = marker.getLngLat();
coordinates.style.display = 'block';
}
	
marker.on('dragend', onDragEnd);

	
	

});*/
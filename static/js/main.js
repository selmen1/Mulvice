$( document ).ready(function() {
        $('#show-side-nav').on('click', function(){
           $('#side-nav-id').toggleClass('active');
           $('#show-side-nav').hide();
           $('.fade-bg').toggleClass('active');

        });
        $('#hide-side-nav').on('click', function(){
           $('#side-nav-id').toggleClass('active');
           $('#show-side-nav').show();
           $('.fade-bg').toggleClass('active');
        });   
        $('.fade-bg').on('click', function(){
           $('#side-nav-id').toggleClass('active');
           $('#show-side-nav').show();
           $('.fade-bg').toggleClass('active');
        });
	
	
        
        
       

          $('#cat-multiselect').multiselect();
          $('#tag-multiselect').multiselect();
	
	
    
        $('#map-search-adv-icon').on('click', function(){
					$('#map-search-adv').toggle();
					$('#map-search-adv-icon').toggleClass('turn');
				});
	
	 $("#map-search-adv-icon").click(function () {
        $("#map-search-heading").fadeOut(function () {
            $("#map-search-heading").text(($("#map-search-heading").text() == 'Recherche Simple') ? 'Recherche Avancée' : 'Recherche Simple').fadeIn();
        })
    })
        
	
});
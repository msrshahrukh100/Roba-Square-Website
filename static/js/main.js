$(function(){

    var d = new Date();
    $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 30, // Creates a dropdown of 15 years to control year
    min: [1980,3,20],
    max: [d.getFullYear(),7,14],
  });
  $('select').material_select();
    $('.scrollspy').scrollSpy();
        
	$('.slider').slider();
	 $('.parallax').parallax();

     $('.dropdown-button1').dropdown({
      inDuration: 300,
      outDuration: 225,
      constrain_width: true, // Does not change width of dropdown to that of the activator
      hover: true, // Activate on hover
      gutter: 0, // Spacing from edge
      belowOrigin: false, // Displays dropdown below the button
      alignment: 'left' // Displays dropdown with edge aligned to the left of button
    }
  );
    
 $('.dropdown-button2').dropdown({
      inDuration: 300,
      outDuration: 225,
      constrain_width: true, // Does not change width of dropdown to that of the activator
      hover: true, // Activate on hover
      gutter: 135, // Spacing from edge
      belowOrigin: false, // Displays dropdown below the button
      alignment: 'left' // Displays dropdown with edge aligned to the left of button
    }
  );

 $('.addtocart').on('click', function(){

  var link = $(this).attr('data-href')
  $.ajax({
    url : link,
    type : 'GET',
    success : function(data){
      Materialize.toast(data['msg'], 4000)
      if (data['count']) {
      $('#cartcount').text(data['count'])
      } 
    }

  });

 });

});
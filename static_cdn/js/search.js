$(function(){

	$('.autocomplete').keyup(function(){

		$('.dropdown-content.autocomplete-content').html("")

		var query = $('.autocomplete').val()
		
		if (query != ""){

		var data = {'query':query}
		$.ajax({
			url : '/shop/search/' ,
			type : 'POST',
			dataType : 'json',
			data : data,
			contentType: 'application/x-www-form-urlencoded;charset=utf-8',
			success : function(data){
				var category = data['categoryitems']
				$.each(category, function(index,value){
					$('.dropdown-content.autocomplete-content').append("<a href='"+value['url']+"'><li><b><img src='"+value['imageurl']+"' class='right circle'>"+value['category']+"</b></li></a>");
				});
				$('.dropdown-content.autocomplete-content').append("<li class='divider'></li>");
				var products = data['productitems'];
				$.each(products, function(index,value){
					$('.dropdown-content.autocomplete-content').append("<a href='"+value['url']+"'><li><img src='"+value['imageurl']+"' class='right circle'>"+value['name']+"</li></a>");
				});

			}
		})

		} //for the if
		else
		{
			$('.dropdown-content.autocomplete-content').html("")
		}		
	});


	$('.autocomplete.searchfriends').keyup(function(){
		$('.dropdown-content.autocomplete-content.people-dropdown').html("")
		var query = $('.autocomplete.searchfriends').val()
		console.log(query)
		if (query != "")
		{
			var data = {'query':query}
			$.ajax({
				url : '/social/search/',
				type : 'POST',
				dataType : 'json',
				data : data,
				contentType: 'application/x-www-form-urlencoded;charset=utf-8',
				success : function(data){
					console.log(data)
					var people = data['searchusers']
					$.each(people, function(index,value){
					$('.dropdown-content.autocomplete-content.people-dropdown').append("<a href='"+value['url']+"'><li><img src='"+value['imageurl']+"' class='left circle'><b>"+value['name']+"</b>&nbsp<span class='grey-text right'>"+value['about']+"<span></li></a>");
				});
				}

			})
		}
		else
		{
			$('.dropdown-content.autocomplete-content.people-dropdown').html("")
		}

	});



});
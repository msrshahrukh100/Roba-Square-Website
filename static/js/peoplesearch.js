$(function(){


$('.autocomplete.searchfriends').keyup(function(){
		$('.dropdown-content.autocomplete-content.people-dropdown').html("")
		var query = $('.autocomplete.searchfriends').val()

		
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
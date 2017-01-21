	var previouslength = -1;
	function my_notification_callback(data) {
			$('#nl').html("");

		 for (var i=0; i < data.unread_list.length; i++) {
		        msg = data.unread_list[i];
		        obj = JSON.parse(msg['data']);
		        console.log(obj)
		        text = "<li class='collection-item avatar'><a href="+obj.url+"><img src="+obj.imageurl+" class='circle'><b>"+msg['actor']+"</b> "+msg['verb']+"<br><span id='ts' title="+msg['timestamp']+"></span></a></li>"
		        $('#nl').append(text);
		        $('span#ts').timesince();
		    }
		    $('#nl').append("<li class='collection-item'><a href='/social/myprofile/'><b>View All</b></a></li>")

		   if(data.unread_list.length != 0 && data.unread_list.length != previouslength){
			var audio = new Audio('/static/audio/notification.mp3');
			audio.play();
			Materialize.toast('New Notifications', 3000, 'rounded')
			previouslength = data.unread_list.length;
		   }
	}

function readall() {
	$.ajax({
		url : '/social/readallnotifications',
		type : 'GET',
		success : function(data) {

		}
	})
}

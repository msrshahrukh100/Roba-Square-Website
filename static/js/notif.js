	function my_notification_callback(data) {

		 for (var i=0; i < data.unread_list.length; i++) {
		        msg = data.unread_list[i];
		        console.log(msg['verb']);
		        console.log(msg['data']);
		        text = "<li><b>"+msg['actor']+"</b> "+msg['verb']+"</li>"
		        $('#nl').html(text);
    }
	}


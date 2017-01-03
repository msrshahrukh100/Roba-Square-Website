
def get_user_name(user) :
	if user.is_anonymous() :
		return ""
	if user.first_name and user.last_name :
		return user.first_name + " " + user.last_name
	return user.username

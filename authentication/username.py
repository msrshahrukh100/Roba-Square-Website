
def get_user_name(user) :
	if user.is_anonymous() :
		return ""
	if user.first_name and user.last_name :
		return user.get_full_name()
	return user.username

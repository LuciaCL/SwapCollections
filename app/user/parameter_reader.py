from app.user.user_view import UserView


def parse_user_from_request(request):
	content = request.get_json()
	user = UserView()
	user.user_name = content.get('user_name')
	user.first_name = content.get('first_name')
	user.last_name = content.get('last_name')
	user.email = content.get('email')
	user.password = content.get("password")
	user.re_password = content.get("re_password")
	return user


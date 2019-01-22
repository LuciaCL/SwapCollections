from app.user.password_utils import hash_password
from app.user.user import User


class UserView:

	def __init__(self, user_name='', first_name='', last_name='', email='', password='', re_password=''):
		self.user_name = user_name
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.re_password = re_password

	def to_user(self):
		return User(self.user_name, self.first_name, self.last_name, self.email, hash_password(self.password))

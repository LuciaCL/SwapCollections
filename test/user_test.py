import unittest
from app.user.user_handler import *
from app.user.user import *
from test.mongo_utils import *


class UserTests(unittest.TestCase):

	def test_insert_user(self):
		user1 = User('Pepito', 'laralito', 'algo', 'david@blabla.com', 'pass1')
		_id = post_user(user1)
		# self.assertEqual(type(_id), 'string')

	def test_update_user(self):
		# Given
		user_in_db = User('Pepito', 'laralito', 'algo', 'da@blabla.com', 'pass2')
		user_id = insert_user(user_in_db)
		# When
		user2 = User('Pepito', 'laralito', 'algo', 'da@blabla.com', 'password')
		update_user(user_id, user2)
		# Then
		updated_user = search_by_id(user_id)
		self.assertNotEqual(user_in_db.password, str(updated_user['password']))


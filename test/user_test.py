import unittest
from app.user.user_handler import *
from utils.mongo_utils import *


class UserTests(unittest.TestCase):

	def test_insert_user(self):
		self.test_validations()
		user1 = User('Pepito', 'laralito', 'algo', 'david@blabla.com', 'pass1')
		_id = post_user(user1)

	def test_update_user(self):
		# Given
		user_in_db = User('Pepito', 'laralito', 'algo', 'da@blabla.com', 'pass2')
		user_id = insert_user(user_in_db)
		# When
		update_user(user_id, {"password": "password"})
		# Then
		updated_user = search_by_id(user_id)
		self.assertNotEqual(user_in_db.password, str(updated_user['password']))

	def test_delete_user(self):
		# Given
		user_in_db = User('Pepito', 'laraliito', 'algo', 'da@blabla', 'pass3')
		user_id = insert_user(user_in_db)
		# When
		delete_user(user_id)
		# Then
		self.assertEqual(None, search_by_id(user_id))

	def test_validations(self):
		# Given user
		user1 = User(None, 'laralito', 'algo', 'david@blabl', 'pass1')
		# When  pass all validation
		validation = validations_user(user1)
		# Then  continue
		
		self.assertFalse(validation, 'email error')
from passlib.hash import bcrypt


def password_match(password, re_password):
	return password == re_password


def hash_password(password):
	return bcrypt.hash(password)

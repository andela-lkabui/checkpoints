import os
import unittest
import sqlite3

from sqlalchemy import create_engine

from models import init_db

directory = os.path.dirname(os.path.dirname(__file__))
test_db = os.path.join(directory, 'test.db')
prod_url = os.environ.get('DATABASE_URL')
os.environ['DATABASE_URL'] = 'sqlite:///' + test_db

import api
# from app import app

class TestBucketlistAPI(unittest.TestCase):
	
	def setUp(self):
		print '==================================Kwa setup!!'
		# import ipdb; ipdb.set_trace()
		self.app = api.app
		self.app.config.update(DATABASE_URL=os.environ.get('DATABASE_URL'))
		self.app.config['TESTING'] = True
		sqlite3.connect(test_db)
		init_db()

		# init(r'sqlite:///' + self.test_db)
		self.client = self.app.test_client()
	def tearDown(self):
		# os.close(self.test_db)
		os.environ['DATABASE_URL'] = prod_url
		os.remove(test_db)
        # os.unlink(app.config['DATABASE_URL'])

	def test_registration(self):
		response = self.client.post('/user/registration', data={'username':'test_user', 'password':'12345'})
		self.assertTrue('User successfully registered!' in response.data)

if __name__ == '__main__':
	unittest.main()
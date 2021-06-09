from flask import url_for 
from flask_testing import TestCase
import requests_mock 
from app import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db"
        )
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        
class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker: 
            mocker.get('http://number_api:5001/get_number', json = {'number': 15})
            mocker.get('http://colour_api:5002/colour', text = 'black')
            mocker.post('http://prize_api:5003/prize/{number}/{colour}', text = 'you got the prize £50')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            #self.assertIn(b'On Friday(2022-06-03) you will becomone a millionaire, lucky you!!', response.data)



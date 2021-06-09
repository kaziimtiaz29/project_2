from flask import url_for 
from flask_testing import TestCase
import requests_mock 
from app import app
from unittest.mock import patch 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_prize(self):
        # number= 15
        # colour='black'
        response = self.client.post(url_for('prize_gen'),data = json['num']=15,json['col']='black',
        follow_redirects=True
        )

        self.assertEqual(response.data.decode(),"£50")
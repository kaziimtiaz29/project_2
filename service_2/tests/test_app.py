from flask import url_for 
from flask_testing import TestCase
import requests_mock 
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_number(self):
        for i in range(20):
            response = self.client.get(url_for('lucky_number'))
            self.assertIn(response.json['number'], range(14,17))
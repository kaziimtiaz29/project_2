from flask import url_for 
from flask_testing import TestCase
import requests_mock 
from app import app
import re

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_day(self):
        for _ in range(5):
            response = self.client.get(url_for('colour_'))
            self.assertEqual(response.status_code, 200)
            #self.assertIn(response.jsonify(["black","blue","violet"])
from django.test import TestCase
from django.contrib.auth import get_user_model

from model_app import models

class TestUserModels(TestCase):
    def test_first_test(self):
        self.assertTrue(1,1)
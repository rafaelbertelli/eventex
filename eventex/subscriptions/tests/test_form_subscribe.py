from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeForm(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))

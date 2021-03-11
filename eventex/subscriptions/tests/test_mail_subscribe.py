from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        self.defined_email = 'rafaelbertelli@yahoo.com.br'
        data = dict(name='Rafael Borges', cpf='12365478912',
                    email=self.defined_email, phone='11-9-4262-0998')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = self.defined_email
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        """Must be a list of recipients"""
        expect = [self.defined_email]
        self.assertEqual(expect, self.email.to)
        self.assertTrue(isinstance(self.email.to, list))

    def test_subscription_email_body(self):
        contents = 'Nome', 'CPF', 'E-mail', 'Telefone'
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

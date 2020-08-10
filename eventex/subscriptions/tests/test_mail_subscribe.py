from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Rafael Borges', cpf='12365478912',
                    email='rafaelbertelli89@gmail.com', phone='11-9-4262-0998')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        """Must be a list of recipients"""
        expect = ['rafaelbertelli89@gmail.com']
        self.assertEqual(expect, self.email.to)
        self.assertTrue(isinstance(self.email.to, list))

    def test_subscription_email_body(self):
        contents = 'Nome', 'CPF', 'E-mail', 'Telefone'

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

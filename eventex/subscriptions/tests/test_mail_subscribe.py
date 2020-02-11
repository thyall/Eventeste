from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Thyall Dgreville', cpf='123456789',
                    email="thyall@dgreville.net", phone='987654321')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'thyall@dgreville.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):

        contents = ['Thyall Dgreville', '123456789', 'thyall@dgreville.net','987654321']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

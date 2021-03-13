from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF only accept digits"""
        form = self.make_validated_form(cpf='ABCD12312312')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf='1212')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def make_validated_form(self, **kwargs):
        valid_data = dict(
            name="Rafael", cpf='12345678912', email='rafael@protonmail.com', phone='1144221133')
        data = dict(valid_data, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

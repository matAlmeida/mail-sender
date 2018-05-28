import unittest
from context import html_template, mail, secrets


class TestMail(unittest.TestCase):

    def test_create_mail(self):
        template = html_template.HTMLTemplate(
            '../example-files/template.html')
        sender = {
            'smtp': 'smtp.gmail.com:587',
            'name': 'Matheus Almeida',
            'mail': secrets.email['account'],
            'password': secrets.email['password']
        }

        email = mail.Mail(template, sender)

        self.assertIsNotNone(email, 'Email created')

    def test_send_mail(self):
        template = html_template.HTMLTemplate(
            '../example-files/template2.html')
        sender = {
            'smtp': 'smtp.gmail.com:587',
            'name': 'Matheus Almeida',
            'mail': secrets.email['account'],
            'password': secrets.email['password']
        }

        email = mail.Mail(template, sender)

        recipient = [
            'yuev@dfg6.kozow.com'
        ]
        subject = "Meu teste"
        values = {
            'first_name': 'Matheus',
            'company_name': 'Minha Empresa'
        }
        attachment = '../example-files/template.html'

        wasSent = email.send_mail(recipient, subject, values, attachment)

        self.assertTrue(wasSent)


if __name__ == '__main__':
    unittest.main(verbosity=2)

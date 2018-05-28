import unittest
from context import html_template


class TestHTMLTemplate(unittest.TestCase):

    def test_get_variables(self):
        template = html_template.HTMLTemplate(
            '../example-files/template.html')

        self.assertEqual(template.get_variables(), [
                         'first_name', 'company_name', 'send_date'])

    def test_get_variables2(self):
        template = html_template.HTMLTemplate(
            '../example-files/template2.html')

        self.assertEqual(template.get_variables(), [
                         'first_name', 'company_name'])

    def test_new_mail(self):
        template = html_template.HTMLTemplate(
            '../example-files/template.html')

        self.assertEqual(
            template.new_mail(
                {'first_name': 'Foo', 'company_name': 'Bar', 'send_date': '27/05/2018'}),
            """<p> <br/> Foo <br/> Bar <br/> 27/05/2018</p>"""
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)

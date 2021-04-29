from io import StringIO
from django.core.management import call_command
from django.test import TestCase


class TestParser(TestCase):
    def test_parser_output(self):
        out = StringIO()
        call_command('parser', stdout=out)
        self.assertIn('Success', out.getvalue())
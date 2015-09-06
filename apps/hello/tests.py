from django.test import TestCase

# Create your tests here.


class SomeTests(TestCase):
    def test_math(self):
        "should be true"
        assert(2 + 2 == 4)

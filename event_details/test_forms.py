from django.test import TestCase
from .forms import RaceCommentForm


class TestRaceCommentForm(TestCase):

    def test_form_is_valid(self):
        """
        Test to see that the form validation is True if data was provided
        """
        form = RaceCommentForm({
            'comment': 'Test comment under event'
        })
        self.assertTrue(
            form.is_valid(), msg="Data provided, but form invalid"
            )

    def test_form_is_invalid(self):
        """
        Test to see that the form validation is False if no data was provided
        """
        form = RaceCommentForm({
            'comment': ''
        })
        self.assertFalse(
            form.is_valid(), msg="No data provided, but form valid"
            )

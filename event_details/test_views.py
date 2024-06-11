from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import RaceCommentForm
from .models import RaceEventDetail, RaceEvent, RaceEventComment


class TestDetailViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="myUsername",
            password="myPassword",
            email="test@test.com",
        )
        self.event = RaceEvent(
            start_date="2024-06-12",
            location="testing",
            event_name="testing environ"
            )
        self.event.save()

        self.event_details = RaceEventDetail(
            race=RaceEvent(pk=1),
            event_info="test event",
            circuit_name="test circuit"
            )
        self.event_details.save()

        self.comment = RaceEventComment(
            event=RaceEventDetail(pk=1),
            author=self.user,
            comment="test comment"
        )

    def test_comment_textarea_visibility(self):

        response = self.client.get(reverse("event_details", args=[1]))
        """Test that the comment form text area is not visible"""
        self.assertNotIn(
            b'<textarea',
            response.content,
            msg="textarea is visible even though user is logged out"
            )

        self.client.login(
            username="myUsername", password="myPassword")

        """Test that the comment form text area is visible"""
        response = self.client.get(reverse("event_details", args=[1]))
        self.assertIn(
            b'<textarea',
            response.content,
            msg="textarea is not visible even though user is logged in"
            )

    def test_delete_comment_unathorized_user(self):
        """
        Check that a logged out user gets redirected
        if they try to delete a comment through url input.
        """
        response = self.client.get(reverse("comment_delete", args=[1, 1]))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/?next=/event/1/delete_comment/1", response.url)

    def test_edit_comment_unathorized_user(self):
        """
        Check that a logged out user gets redirected to log in
        if they try to edit a comment through url input.
        """
        response = self.client.get(reverse("comment_edit", args=[1, 1]))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/?next=/event/1/edit_comment/1", response.url)

    def test_approve_comment_unathorized_user(self):
        """
        Check that a logged in non superuser gets redirected to not an admin
        if they try to approve a comment through url input.
        """
        self.client.login(
        username="myUsername", password="myPassword")
        response = self.client.get(reverse("comment_approve", args=[1, 1]))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/not_an_admin", response.url)

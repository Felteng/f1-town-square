from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import resolve_url


class MyAccountAdapter(DefaultAccountAdapter):
    """
    Check if there is a previous URL stored from the
    StorePreviousURLMiddleware middleware in the user session.
    After the user completes an account authentication action,
    redirect the user to the stored URL or the default URL.

    If no previous URL is stored then previous_url has a default of None,
    which will redirect the user to the 'home' URL.
    """
    def get_login_redirect_url(self, request):
        previous_url = request.session.pop('previous_url', None)
        if previous_url:
            return previous_url
        else:
            return resolve_url('home')

    def get_logout_redirect_url(self, request):
        previous_url = request.session.pop('previous_url', None)
        if previous_url:
            return previous_url
        else:
            return resolve_url('home')

    def get_signup_redirect_url(self, request):
        previous_url = request.session.pop('previous_url', None)
        if previous_url:
            return previous_url
        else:
            return resolve_url('home')

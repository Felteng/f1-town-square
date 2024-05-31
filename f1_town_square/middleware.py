from django.utils.deprecation import MiddlewareMixin

class StorePreviousURLMiddleware(MiddlewareMixin):
    """
    Create a middleware to store the URL of the page the user
    was on before performing an account authentication action.
    This URL will be saved in the session unless it's an
    account-related page, a favicon request, or a 404 error page.

    For example if the user clicks "login" to be able to comment on
    an event, and then realizes that they don't have an account yet,
    so they click on sign up, upon signup they will be returned back to the event,
    and not to the login page.
    """
    def process_request(self, request):
        if request.path.startswith('/accounts/') or request.path.startswith('/favicon.ico/'):
            return
        else:
            request.session['previous_url'] = request.get_full_path()

    def process_response(self, request, response):
        # Check if the response status is 404 and remove the previous URL if it is
        if response.status_code == 404:
            if 'previous_url' in request.session:
                del request.session['previous_url']
        return response
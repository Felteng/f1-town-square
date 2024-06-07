class StorePreviousURLMiddleware:
    """
    Create a middleware to store the URL of the page the user
    was on before performing an account authentication action.
    This URL will be saved in the session unless it's an
    account-related page, a favicon request, or a 404 error page.

    The reason to check for /favicon.ico/ is because if the user
    manages to land on a page not extended by base.html where the
    favicon does not get loaded, django makes a get request to
    favicon.ico and then that path would otherwise be saved.

    For example if the user clicks "login" to be able to comment on
    an event, and then realizes that they don't have an account yet,
    so they click on sign up, upon signup they will be returned back
    to the event, and not to the login page.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Save the previous URL in session unless it's an account-related page or favicon request
        if not (
            request.path.startswith('/accounts/') or
            request.path.startswith('/favicon.ico/')
        ):
            request.session['previous_url'] = request.get_full_path()

        response = self.get_response(request)

        # Check if the response is 404 to remove the previous URL
        if response.status_code == 404:
            request.session.pop('previous_url', None)
        
        return response

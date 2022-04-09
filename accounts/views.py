from django.contrib.auth.views import LoginView


class LoginUserView(LoginView):
    template_name = 'accounts/registration/login.html'
    redirect_authenticated_user = True

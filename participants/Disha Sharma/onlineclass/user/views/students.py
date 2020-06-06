
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from allauth.account.forms import SignupForm
from ..forms import StudentSignUpForm
from ..models import User

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'student/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')
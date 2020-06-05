from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from ..forms import TeacherSignUpForm
from ..models import User

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'teacher/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import *
from django.contrib import messages
from ..models import User


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('profile')
        else:
            return redirect('profile')
    return render(request, 'index.html')

def search(request):
	if request.method == 'POST':
		srch = request.POST['srh']

		if srch:
			match = User.objects.filter( Q(first_name__icontains=srch) |
											Q(last_name__icontains=srch) )
			if match:
				return render(request,'search.html',{'sr':match})
			else:
				messages.error(request,'no result found')
		else:
			return HttpResponseRedirect('/search/')

	return render(request,'search.html')


@login_required
def profile(request):
    return render(request, 'profile.html')
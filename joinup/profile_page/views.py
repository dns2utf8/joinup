from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def profile_self(request):
    return render(request, 'profile_page/self.html', {
        'page_title': 'Profile ' + request.user.username,
        'user': request.user,
    })
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
# Create your views here.

# local imports
from authapp.forms import ProfileForm

class IndexView(View):
    def get(self, request):
        # return HttpResponse("the view is displaying")
        current_user = request.user
        print('current', current_user)
        ctx = {
            "user": current_user
        }
        return render(request, 'index.html', ctx)
    
class ProfileView(View):
    
    def get(self, request):
        current_user = request.user
        
        form = ProfileForm()
        print('current', form)
        ctx = {
            "user": current_user,
            "form": form
        }
        return render(request, "profile.html", ctx)
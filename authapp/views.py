from math import remainder
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class IndexView(View):
    def get(self, request):
        # return HttpResponse("the view is displaying")
        # user = self.request.
        ctx = {
            # "user": "user"
        }
        return render(request, 'index.html', ctx)
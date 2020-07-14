from django.shortcuts import render
from django.views import View


# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="mainapp/main_page.html")
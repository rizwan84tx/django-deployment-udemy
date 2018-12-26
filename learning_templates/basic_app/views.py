from django.shortcuts import render

# Create your views here.
def index(request):
    user = {'name':"Mohammed Rizwan", 'age':34 }
    return render(request,'basic_app/index.html', user)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

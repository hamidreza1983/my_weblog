from django.shortcuts import render




def home(req):
    return render(req, 'my_weblog/index.html')

def about(req):
    return render(req, 'my_weblog/about.html')

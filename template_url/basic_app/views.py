from django.shortcuts import render

def index(request):
    context_dict = {'text':'hello world!','number':123}
    return render(request,'basic_app/index.html',context= context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url.html')

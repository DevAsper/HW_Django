from django.shortcuts import render

def data_view(request):
    return render(request, 'myapp/data.html')

def test_view(request):
    return render(request, 'myapp/test.html')

def page1_view(request):
    return render(request, 'myapp/page1.html')

def page2_view(request):
    return render(request, 'myapp/page2.html')

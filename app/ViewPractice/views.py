from django.shortcuts import render

# Create your views here.
def multi(request):
    return render(request, 'multi_part.html')

from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'webapp/index.html')
def notFound(request):
  return render(request, 'webapp/404.html')
def contact(request):
  return render(request, 'webapp/contact.html')
def blog(request):
  return render(request, 'webapp/blog-single.html')
def portfolio(request):
  return render(request, 'webapp/portfolio-details.html')
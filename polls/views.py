from django.http import HttpResponse

def index(request):
	return HttpResponse("YOU ARE AT POLLS")
	


# Create your views here.

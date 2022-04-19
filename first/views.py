from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1 style='color:magenta; font-size:250px'>Hello World!</h1>''')

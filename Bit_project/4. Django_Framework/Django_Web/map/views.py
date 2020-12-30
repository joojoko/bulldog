from django.shortcuts import render
from modelpage.views import photo
# Create your views here.
def Realtimemap(request):
        return render(request, 'Real-time map.html', {'email': request.session.get('user')})



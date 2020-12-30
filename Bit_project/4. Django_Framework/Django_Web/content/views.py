from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from account.views import LoginView
from account.decorators import login_required_content
from account.models import Account
from .models import Contact
from .forms import ContactForm
# Create your views here.
def contact_complete(request):
    return render(request, 'contact_complete.html')

@login_required_content
def content(request, *args, **kwargs):
    return render(request, 'content.html', { 'email': request.session.get('user') })

@login_required_content
def contact(request, *args, **kwargs):
    if not request.session.get('user'):
        return redirect('/login')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            account = Account.objects.get(email=user_id)

            contact = Contact()
            contact.title = form.cleaned_data['title']
            contact.contents = form.cleaned_data['contents']
            contact.writer = account
            contact.save()

            return redirect('/contact_complete')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'email': request.session.get('user')})

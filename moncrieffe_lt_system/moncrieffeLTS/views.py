from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from datetime import datetime
#from moncrieffeLTS.forms import SuggestionForm
from moncrieffeLTS.models import User, Media, Topic
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.forms import ModelForm
#from moncrieffeLTS.forms import SuggestionForm,SearchlibForm, newuserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.sessions.models import Session
from random import randint



def index(request):
    itemlist = Media.objects.all()

    indexcontext = {'itemlist': itemlist}
    return render(request, 'moncrieffeLTS/index.html', indexcontext)

def show_book(request, book_title_slug):
    context_dict = {}
    try:
        media = Media.objects.get(slug=book_title_slug)
        #pages = Page.objects.filter(category=category)

        context_dict['media'] = media
    except Media.DoesNotExist:
        context_dict['media'] = None
        #context_dict['category'] = None

    return render(request, 'rango/category.html', context_dict)



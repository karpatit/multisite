from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.

def showsite(request):
    #if (request.user.is_anonymous):
    #    return redirect('/')
    #else:
    current_site = get_current_site(request)
    if str(current_site) == "test1.hitheal.org.il":
        return HttpResponse('site1 reached!')
    elif str(current_site) == 'test2.hitheal.org.il':
        return HttpResponse('site2 reached!')
    elif str(current_site) == 'test3.hitheal.org.il':
        return HttpResponse('site3 reached!')
    else:
        return HttpResponse('site was not reached')

    #return HttpResponse('Failed to show your site...'+current_site)
    return HttpResponse(current_site)

from django.shortcuts import render_to_response
from models import Pelicula
from django.db.models import Q

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(titulo_pelicula__icontains=query)
        )
        results = Pelicula.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("search.html",{"results": results, "query": query})

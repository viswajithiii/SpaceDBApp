from django.shortcuts import render_to_response
from django.template import RequestContext
from space.models import Astronomer, EducationAstronomer, Moon, Planet, Star, Galaxy, Astronaut, SpaceFlight

def home(request):

    return render_to_response ('home.html', {},context_instance = RequestContext(request))

def astronomer(request):

    querydict = {}
    querydict["astronomers"] = Astronomer.objects.all()
    return render_to_response ('astronomer.html', querydict,context_instance = RequestContext(request))

def oneastronomer(request,id):


    querydict = {}
    astro = Astronomer.objects.get(pk=id)
    querydict["astro"] = astro
    querydict["education"] = EducationAstronomer.objects.filter(astronomer__id=id)
    querydict["moon"] = Moon.objects.filter(discoverer__id=id)
    querydict["planet"] = Planet.objects.filter(discoverer__id=id)
    querydict["star"] = Star.objects.filter(discoverer__id=id)
    querydict["galaxy"] = Galaxy.objects.filter(discoverer__id=id)
    return render_to_response ('oneastro.html', querydict,context_instance = RequestContext(request))

def astronaut(request):

    querydict = {}
    querydict["astronauts"] = Astronaut.objects.all()
    return render_to_response ('astronaut.html', querydict, context_instance = RequestContext(request))

def oneastronaut(request,id):


    querydict = {}
    astro = Astronaut.objects.get(pk=id)
    querydict["astro"] = astro
    querydict["education"] = EducationAstronomer.objects.filter(astronomer__id=id)
    querydict["leader"] = SpaceFlight.objects.filter(leader__id=id)
    querydict["member"] = SpaceFlight.objects.filter(members__pk=id)
    return render_to_response ('oneastronaut.html', querydict,context_instance = RequestContext(request))


def planet(request):

    querydict = {}
    querydict["planets"] = Planet.objects.all()
    if "plan" in request.GET:
        spid = int(request.GET["plan"])
        querydict["sp"] = Planet.objects.get(pk=spid)
        querydict["tried"] = True
        querydict["moon"] = Moon.objects.filter(planet__id=spid)
    return render_to_response ('planet.html', querydict,context_instance=RequestContext(request))

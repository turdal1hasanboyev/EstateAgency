from django.shortcuts import render

from apps.user.models import About
from apps.agent.models import Agent
from apps.property.models import Property
from apps.common.models import Service, Testimonials
from apps.blog.models import Blog


def about(request):
    about = About.objects.get(id=1)

    agents = Agent.objects.all().order_by("-id")[:3]

    context = {
        "about": about,
        "agents": agents,
    }

    return render(request, "about.html", context)

def home(request):
    latest_properties = Property.objects.all().order_by("id")[:4]
    banner = Property.objects.all().order_by("id")[:3]
    services = Service.objects.all().order_by("-id")[:3]
    best_agents = Agent.objects.all().order_by("id")[:3]
    testimonials = Testimonials.objects.all().order_by("id")[:2]
    latest_news = Blog.objects.all().order_by("-id")[:4]
     
    context = {
        "banner": banner,
        "services": services,
        "latest_properties": latest_properties,
        "best_agents": best_agents,
        "testimonials": testimonials,
        "latest_news": latest_news,
    }

    return render(request, 'index.html', context)

from django.shortcuts import render

from .models import About
from apps.agent.models import Agent
from apps.property.models import Property
from apps.common.models import Service, Testimonials
from apps.blog.models import Blog


def about(request):
    about = About.objects.get(id=1)

    agents = Agent.objects.all()

    context = {
        "about": about,
        "agents": agents.order_by("-id")[:3],
    }

    return render(request, "about.html", context)

def home(request):
    property = Property.objects.all()
    
    services = Service.objects.all()
    best_agents = Agent.objects.all()
    testimonials = Testimonials.objects.all()
    latest_news = Blog.objects.all()
     
    context = {
        "banner": property.order_by("-id")[:3],
        "services": services.order_by("-id")[:3],
        "latest_properties": property.order_by("id")[:3],
        "best_agents": best_agents.order_by("id")[:3],
        "testimonials": testimonials.order_by("id")[:2],
        "latest_news": latest_news.order_by("-id")[:6],
    }

    return render(request, 'index.html', context)

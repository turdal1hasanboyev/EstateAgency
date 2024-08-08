from django.shortcuts import render, redirect

from apps.agent.models import Agent
from apps.property.models import Property


def agent(request):
    agents = Agent.objects.all().order_by("-id")[:6]

    return render(request, "agents-grid.html", {"agents": agents})

def agent_single(request, slug):
    agent = Agent.objects.get(slug__iexact=slug)

    my_properties = Property.objects.filter(agent=agent.id).order_by("-id")[:6]

    context = {
        "agent": agent,
        "my_properties": my_properties,
    }

    return render(request, "agent-single.html", context)

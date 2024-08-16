from django.shortcuts import render

from apps.agent.models import Agent
from apps.property.models import Property


def agent(request):
    agents = Agent.objects.all()

    return render(request, "agents-grid.html", {"agents": agents.order_by("-id")[:6]})

def agent_single(request, slug):
    agent = Agent.objects.get(slug__iexact=slug)

    my_properties = Property.objects.filter(agent_id=agent.id)

    context = {
        "agent": agent,
        "my_properties": my_properties.order_by("-id"),
    }

    return render(request, "agent-single.html", context)

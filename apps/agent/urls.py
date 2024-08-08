from django.urls import path

from apps.agent.views import agent, agent_single


urlpatterns = [
    path("agent/", agent, name="agent"),
    path("agent-single/<slug:slug>/", agent_single, name="agent-single"),
]

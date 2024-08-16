from django.shortcuts import render, redirect

from apps.property.models import Property, Amenities
from apps.contact.models import AgentContact


def property(request):
    properties = Property.objects.all()

    return render(request, "property-grid.html", {"properties": properties.order_by("id")[:6]})

def property_single(request, slug):
    url = request.META.get('HTTP_REFERER')

    property = Property.objects.get(slug__iexact=slug)

    amenities = Amenities.objects.filter(property_id=property.id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        AgentContact.objects.create(
            agent_id=property.agent.id,
            name=name,
            email=email,
            message=message,
        )

        return redirect(url)

    context = {
        "property": property,
        "amenities": amenities,
    }

    return render(request, "property-single.html", context)

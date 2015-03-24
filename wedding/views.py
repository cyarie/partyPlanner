from django.shortcuts import render
from wedding.models import People
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    last_five_people = People.objects.order_by("name")[:5]
    context = {"last_five_people": last_five_people}
    return render(request, "wedding/index.html", context)
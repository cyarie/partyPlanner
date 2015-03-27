from django.shortcuts import render
from wedding.models import People
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


@login_required()
def index(request):
    people_added = People.objects.filter(created_by=request.user.id).count()
    context = {"people_added": people_added}
    return render(request, "wedding/index.html", context)

@login_required()
def invite_people(request):
    return render(request, "wedding/invite.html")
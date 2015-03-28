from django.shortcuts import render, render_to_response
from wedding.models import People
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from wedding.forms import PeopleForm
from django.forms.models import modelformset_factory
from django.shortcuts import get_object_or_404


@login_required()
def index(request):
    people_added = People.objects.filter(created_by=request.user.id).count()
    context = {"people_added": people_added}
    return render(request, "wedding/index.html", context)


@login_required()
def invitations(request):
    context = RequestContext(request)

    if request.method == "POST":
        form = PeopleForm(request.POST)

        if form.is_valid():
            person = form.save(commit=False)
            person.created_by_id = request.user.id
            person.save()
            return render(request, "wedding/thanks.html")
        else:
            print(form.errors)
    else:
        form = PeopleForm()

    return render_to_response('wedding/invite.html', {'form': form}, context)
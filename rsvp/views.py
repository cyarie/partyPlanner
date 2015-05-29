from django.shortcuts import render, render_to_response
from django.template import RequestContext

from rsvp.forms import RsvpForm

# Index view, will contain the short form and everything
def index(request):
    return render(request, "rsvp/index.html")


def rsvp(request):
    context = RequestContext(request)

    if request.method == "POST":
        form = RsvpForm(request.POST)
        print(request.POST["going"])

        if form.is_valid():
            rsvp_obj = form.save(commit=False)
            if int(request.POST["going"]) == 0:
                rsvp_obj.going = False
            elif int(request.POST["going"]) == 1:
                rsvp_obj.going = True
            rsvp_obj.save()
            return render(request, "rsvp/thanks.html")
        else:
            print(form.errors)
    else:
        form = RsvpForm()

    return render_to_response("rsvp/index.html", {"form": form}, context)

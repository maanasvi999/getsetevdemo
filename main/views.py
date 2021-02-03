from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import EVCategory, EVInformation, EVHighlights, ModelsInfo, EVColorCustom, Subscribers
from .forms import EmailForm
from django.contrib import messages

# Create your views here.

def single_slug(request, single_slug):
    categories = [e.category_slug for e in EVCategory.objects.all()]
    
    if single_slug in categories:
        matching_series = EVInformation.objects.filter(ev_category__category_slug = single_slug)

        series_urls = {}

        for m in matching_series.all():
            part_one = EVInformation.objects.filter(ev_category__ev_category = m.ev_category)
            series_urls[m] = part_one


        return render(request, 
                        "main/evs.html",
                        {"part_ones": series_urls})
    
    evs = [e.ev_slug for e in EVInformation.objects.all()]

    if single_slug in evs:
        this_ev = EVInformation.objects.get(ev_slug = single_slug)
        evs_from_category = EVInformation.objects.filter(ev_category__ev_category = this_ev.ev_category)
        this_ev_idx = list(evs_from_category).index(this_ev)
        ev_models = ModelsInfo.objects.filter(ev_title__ev_title = this_ev.ev_title)
        ev_highlights = EVHighlights.objects.all().filter(ev_title__ev_title = this_ev.ev_title)
        ev_colors = EVColorCustom.objects.filter(ev_title__ev_title = this_ev.ev_title)

        return render(request,
                        "main/evdetails.html",
                        {"ev":this_ev,
                        "sidebar": evs_from_category,
                        "this_ev_idx": this_ev_idx,
                        "ev_models": ev_models,
                        "ev_highs": ev_highlights,
                        "ev_colors": ev_colors})
    
    return HttpResponse(f"{single_slug} does not correspond to anything!")
    

def homepage(request):
    return render(request = request,
                  template_name = "main/home.html",
                  context = {"categories": EVCategory.objects.all})


def get_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            sub = Subscribers()
            sub.email = form.cleaned_data.get('email')
            sub.save()
            messages.info(request, f"You are now subscribed: {sub.email}")
            return redirect('main:homepage')

        else:
            messages.error(request, "Invalid. Try again.")
    form = EmailForm()
    return render(request,'main/success.html', {'form': form})
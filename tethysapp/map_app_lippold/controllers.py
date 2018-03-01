from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {

    }

    return render(request, 'map_app_lippold/home.html', context)


@login_required()
def map_view(request):
    """
    Controller for the app home page.
    """

    context = {
    
    }

    return render(request, 'map_app_lippold/map-view.html', context)



@login_required()
def data_services(request):
    """
    Controller for the app home page.
    """

    context = {
    
    }

    return render(request, 'map_app_lippold/data-services.html', context)



@login_required()
def about(request):
    """
    Controller for the app home page.
    """

    context = {
    
    }

    return render(request, 'map_app_lippold/about.html', context)



@login_required()
def mockups(request):
    """
    Controller for the app home page.
    """

    context = {
    
    }

    return render(request, 'map_app_lippold/mockups.html', context)



@login_required()
def proposal(request):
    """
    Controller for the app home page.
    """

    context = {
    
    }

    return render(request, 'map_app_lippold/proposal.html', context)
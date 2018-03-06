from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import DatePicker
from tethys_sdk.gizmos import TextInput
from tethys_sdk.gizmos import RangeSlider
import tethys


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



@login_required()
def gizmos(request):
    """
    Controller for the app home page.
    """

    date_picker = DatePicker(
        name='date',
        display_text='Date',
        autoclose=True,
        format='MM d, yyyy',
        start_date='2/15/2014',
        start_view='decade',
        today_button=True,
        initial='February 15, 2017'
    )

    text_input = TextInput(display_text='Text',
                           name='inputAmount',
                           placeholder='e.g.: 10.00',
                           prepend='$')

    slider1 = RangeSlider(display_text='Slider 1',
                      name='slider1',
                      min=0,
                      max=100,
                      initial=50,
                      step=1)

    context = {'date_picker': date_picker, 'text_input': text_input, 'slider1':slider1,}

    return render(request, 'map_app_lippold/gizmos.html', context)
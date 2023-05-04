from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from django.contrib import auth
from .models import Shuhuda, Mhanga,Uchunguzi
from django.contrib.auth.decorators import login_required



# Create your views here.

def mahojiano(request):
    return render(request , 'mahojiano.html')

@login_required
def questionnaire_view(request, message):
    username = request.user.username  # Get the authenticated user's username
    # Your other code here
    return render(request, 'form.html', {'username': username, 'message': message})


def submit_form(request):
    if request.method == 'POST':
        # Get data from the form
        jina_kwanza = request.POST.get('firstName')
        jina_pili = request.POST.get('middleName')
        jina_mwisho = request.POST.get('lastName')
        place = request.POST.get('place')
        region = request.POST.get('region')
        shahidi = request.POST.get('shahidi')
        simu = request.POST.get('simu')
        uhusiano = request.POST.get('uhusiano')
        uhusiano_kipindi_kifo = request.POST.get('uhusiano_kipindi_kifo')
        jina_kwanza = request.POST.get('firstName')
        jina_pili = request.POST.get('middleName')
        jina_mwisho = request.POST.get('lastName')
        jinsia = request.POST.get('jinsia')
        ndoa = request.POST.get('ndoa')
        kuzaliwa = request.POST.get('kuzaliwa')
        kufa = request.POST.get('kufa')
        mahali = request.POST.get('mahali')
        maelezo = request.POST.get('maelezo')
        sababu1 = request.POST.get('sababu1')
        sababu2 = request.POST.get('sababu2')
        magonjwa = request.POST.get('magonjwa')
        mengineyo = request.POST.get('mengineyo')
        
        

        # Create objects of both models and save them
        shuhuda = Shuhuda.objects.create(
            jina_kwanza=jina_kwanza,
            jina_pili=jina_pili,
            jina_mwisho=jina_mwisho,
            place=place,
            region=region,
            shahidi=shahidi,
            uhusiano=uhusiano,
            simu=simu,
            Uhusiano_kipindi_kifo=uhusiano_kipindi_kifo
        )

        mhanga = Mhanga.objects.create(
            shuhuda=shuhuda,
            jina_kwanza=jina_kwanza,
            jina_pili=jina_pili,
            jina_mwisho=jina_mwisho,
            jinsia=jinsia,
            ndoa=ndoa,
            kuzaliwa=kuzaliwa,
            kufa=kufa,
            mahali=mahali,
            maelezo=maelezo,
            sababu1=sababu1,
            sababu2=sababu2
        )

        uchunguzi= Uchunguzi.objects.create(
            magonjwa=magonjwa,
            mengineyo=mengineyo
        )

        # Return a success message
        return render(request, 'success.html')

    return render(request, 'report.html')










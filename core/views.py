from django.shortcuts import render
from .models import Projeto, Certificado
from .forms import MensagemForm

def sobre_mim(request):
    tecnologias = ['Python', 'R', 'Google Sheets', 'SQL', 'Excel', 'Tableau', 'Power BI']
    links = {"LinkedIn":"https://www.linkedin.com/in/%C3%A1lvaro-jos%C3%A9-pereira-rodrigues/",
            "GitHub":"https://github.com/alvarojpr"}
    return render(request, 'core/sobre_mim.html', {'tecnologias': tecnologias, 'links':links})

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/projetos.html', {'projetos': projetos})

def certificados(request):
    certificados = Certificado.objects.all()
    return render(request, 'core/certificados.html', {'certificados': certificados})

def fale_comigo(request):
    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/fale_comigo.html', {'form': MensagemForm(), 'sucesso': True})
    else:
        form = MensagemForm()
    return render(request, 'core/fale_comigo.html', {'form': form})

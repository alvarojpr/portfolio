from django.shortcuts import render
from .models import Projeto, Certificado
from .forms import MensagemForm

def sobre_mim(request):
    tecnologias = ['Python', 'R', 'Google Sheets', 'Excel', 'Tableau', 'Power BI']
    return render(request, 'core/sobre_mim.html', {'tecnologias': tecnologias})

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

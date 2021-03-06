from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import InscricaoForm


def inscricao(request):
    inscricao_form = InscricaoForm()
    if request.method == 'POST':
        inscricao_form = InscricaoForm(request.POST, request.FILES)
        if inscricao_form.is_valid():
            inscricao = inscricao_form.save()
            inscricao.save()
            return render_to_response(
                'inscricao_finalizada.html',
            )
    return render_to_response(
        'inscricao.html',
        {'inscricao_form': inscricao_form},
        context_instance=RequestContext(request)
    )

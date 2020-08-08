from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        form.full_clean()
        body = render_to_string(
            'subscriptions/subscription_email.txt', form.cleaned_data)
        mail.send_mail('Confirmação de inscrição',
                       body,
                       'contato@eventex.com.br',
                       ['recipient@gmail.com', form.cleaned_data['email']])

        return HttpResponseRedirect('/inscricao/')

    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)

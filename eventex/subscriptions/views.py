from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = {'form': form}
        return render(request, 'subscriptions/subscription_form.html', context)

    template_name = 'subscriptions/subscription_email.txt'
    subject = 'Confirmação de inscrição'
    sender = settings.DEFAULT_FROM_EMAIL
    context = form.cleaned_data
    recipient = [context['email']]

    _send_email(template_name, subject, sender, context, recipient)
    Subscription.objects.create(**form.cleaned_data)
    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect('/inscricao/')


def _send_email(template_name, subject, sender, context, recipient):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, sender, recipient)

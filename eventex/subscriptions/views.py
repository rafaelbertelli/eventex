from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect
from django.http.response import Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = {'form': form}
        return render(request, 'subscriptions/subscription_form.html', context)

    subscription = form.save()

    template_name = 'subscriptions/subscription_email.txt'
    subject = 'Confirmação de inscrição'
    sender = settings.DEFAULT_FROM_EMAIL
    context = {'subscription': subscription}
    recipient = [subscription.email]

    _send_email(template_name, subject, sender, context, recipient)

    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(
        request,
        'subscriptions/subscription_detail.html',
        {'subscription': subscription})


def _send_email(template_name, subject, sender, context, recipient):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, sender, recipient)

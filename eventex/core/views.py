from eventex.core.models import Speaker
from django.shortcuts import get_object_or_404, render
from eventex.core.models import Speaker


def home(request):
    speakers = Speaker.objects.all()
    context = {'speakers': speakers}
    return render(request, 'index.html', context)


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})

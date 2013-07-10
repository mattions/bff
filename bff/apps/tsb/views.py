# Create your views here.
from django.views.generic import DetailView, ListView
from tsb.models import Sample

class SampleList(ListView):
    model = Sample
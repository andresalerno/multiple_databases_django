from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Green
from green.models import Green
from django.http import HttpResponseRedirect

def viewdata(request):
    data = Green.objects.using('green_db').all()
    return render(request, "view.html", {"data": data})

class Add(CreateView):
  model = Green
  fields = ('title','content','app_name' )
  template_name = 'add.html'
  success_url = '/green/'

  def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.save()
      return HttpResponseRedirect(self.get_success_url())
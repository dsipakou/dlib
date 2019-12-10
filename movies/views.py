from django.shortcuts import render
from django.views.generic import TemplateView


class MoviesView(TemplateView):
    template_name = 'movies/list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
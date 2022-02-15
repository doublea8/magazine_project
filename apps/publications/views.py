from django.http import Http404
from django.views import generic
from django.shortcuts import render

# Create your views here.
from apps.publications.models import Publication, PublicationCategory


class PublicationListView(generic.ListView):
    template_name = 'index.html'
    queryset = Publication.objects.all()
    context_object_name = 'publication_list'


# class PublicationListView(generic.TemplateView):
#     """Представление для всех публикаций"""
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = dict()
#         context['category_list'] = PublicationCategory.objects.all()
#         context['publication_list'] = Publication.objects.all()
#         return context

class PublicationDetailView(generic.DetailView):
    template_name = 'single.html'
    context_object_name = 'publication'
    model = Publication
    slug_field = 'id'
    slug_field = 'pub_pk'

# class PublicationDetailView(generic.TemplateView):
#     """Представление для конкретной публикации"""
#     template_name = "single.html"
#
#     def get_context_data(self, **kwargs):
#         context = dict()
#         publication_pk = kwargs['pk']
#         context['category_list'] = PublicationCategory.objects.all()
#         try:
#             context['publication'] = Publication.objects.get(id=publication_pk)
#         except Publication.DoesNotExist:
#             raise Http404
#         return context










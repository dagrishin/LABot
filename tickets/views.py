from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from tickets.models import Word
from tickets.serializers import WordSerializers


class Words(APIView):
    """Диалог чата, сообщение"""

    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):

        word = Word.objects.filter(user=request.user)
        serializer = WordSerializers(word, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        # print(request.data)
        # word = WordPostSerializers(data=request.data)
        # if word.is_valid():
        #     word.save(user=request.user)
        #     return Response(status=201)
        # else:
        #     return Response(status=400)

        Word.objects.create(user=request.user, word_translation=request.data['word_translation'])
        return Response(status=201)

# from django.views.generic import DeleteView, DetailView, ListView, UpdateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from registration.models import User
# from .models import Word
# from .forms import ValidPk, ValidSlug
# from django.views.generic import FormView
# from django.http import HttpResponseRedirect
# from django.contrib import messages
# from django.utils.translation import gettext_lazy as _
# from django.urls import reverse_lazy
# from django.contrib.messages.views import SuccessMessageMixin
# from django.db.models import Q
# from registration.views import UserAuthActionMixin
#
#
# class WordGetMixin(object):
#
#     def get(self, *args, **kwargs):
#             word_id = kwargs['pk']
#             for word in Word.objects.filter(pk=word_id):
#                 user_id = word.user.id
#             if user_id != self.request.user.id:
#                 messages.success(self.request, _(f'Вы не имеете права редактировать данный контент'))
#                 return HttpResponseRedirect('/')
#             return super().get(self.request, *args, **kwargs)
#
#
# class WordView(UserAuthActionMixin, ListView):
#     """Отображение всех слов"""
#     model = Word
#     template_name = 'words/word_list.html'
#
#
# class WordList(UserAuthActionMixin, ListView):
#     """Отображение слов конткретного пользователя"""
#     model = Word
#     slug = 'user__username__icontains'
#     pk_field = 'user__id'
#     model_form_test = User
#     template_name = 'words/word_list.html'
#
#     def get_queryset(self):
#         query = Q()
#         if 'pk' in self.kwargs:
#             print(self.kwargs)
#             form = ValidPk(self.kwargs)
#             form.fields['pk'].queryset = self.model_form_test.objects
#             if form.is_valid():
#                 print('aaaa')
#                 query = Q((self.pk_field, self.kwargs['pk']))
#         if 'slug' in self.kwargs:
#             form = ValidSlug(self.kwargs)
#             form.fields['slug'].queryset = self.model_form_test.objects
#             if form.is_valid():
#                 query = Q((self.slug, self.kwargs['slug']))
#         print(query)
#         return super().get_queryset().filter(query)
#
#
# class WordCreate(FormView):
#     """Создание слова"""
#     template_name = 'words/formcreate.html'
#     success_url = reverse_lazy('words:WordView')
#
#     def get(self, *args, **kwargs):
#         if not self.request.user.id:
#             messages.success(self.request, _(f'Необходимо войти или зарегестрироваться'))
#             return HttpResponseRedirect('/')
#         if self.request.user.reg_ok == False:
#             return HttpResponseRedirect(reverse_lazy('auth:active'))
#         return super().get(self.request, *args, **kwargs)
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         Word.objects.create(user=self.request.user, word_translation=form.cleaned_data['word_translation'], word_to_learn=form.cleaned_data['word_to_learn'], word_image=form.cleaned_data['word_image'])
#         messages.success(self.request, _(f'Проект сохранен'))
#         return super().form_valid(form)
#
#
# class WordUpdate(SuccessMessageMixin, UserAuthActionMixin, WordGetMixin, LoginRequiredMixin, UpdateView):
#     """Обновление слова"""
#     success_url = reverse_lazy('words:WordView')
#     model = Word
#     template_name = 'words/formcreate.html'
#     fields = ['word_translation', 'word_to_learn', 'word_image']
#     success_message = _('Проукт изменен')
#
#
# class WordDetail(UserAuthActionMixin, WordGetMixin, DetailView):
#     """Класс отображения одного слова"""
#     model = Word
#     template_name = 'words/word_detail.html'
#
#
# class WordDelete(UserAuthActionMixin, WordGetMixin, DeleteView):
#     """Класс удаления слова"""
#     success_url = reverse_lazy('words:WordView')
#     template_name = 'words/word_confirm_delete.html'
#     model = Word
#
#     def get_success_url(self):
#         messages.success(self.request, _('Слово удалено'))
#         return self.success_url.format(**self.object.__dict__)

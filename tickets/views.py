from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from tickets.models import Word
from tickets.serializers import WordSerializer, WordCreateSerializer


class CustomerAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        pk = request.parser_context['kwargs']['pk']
        user = Word.objects.filter(id=pk).first().user_id
        if user == request.user.id:
            return True
        return False


class WordView(APIView):
    """Вывод и создание карточек"""

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        word = Word.objects.filter(user=request.user)
        serializer = WordSerializer(word, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        serialize = WordCreateSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save(user=request.user)
            return Response(status=201)
        return Response(status=400)


class WordDetail(APIView):
    """Показ, редактирование и удаление одной карточки"""

    permission_classes = [permissions.IsAuthenticated, CustomerAccessPermission]

    def get(self, request, pk):
        word = Word.objects.get(user_id=request.user.id, id=pk)
        serializer = WordSerializer(word)
        return Response({"data": serializer.data})

    def put(self, request, pk):
        word_update = Word.objects.filter(id=pk)
        serialize = WordCreateSerializer(data=request.data)
        if serialize.is_valid():
            word_update.update(**serialize.validated_data)
            return Response(status=201)
        return Response(status=400)

    def delete(self, request, pk):
        word_delete = Word.objects.filter(id=pk)
        word_delete.delete()
        return Response(status=204)
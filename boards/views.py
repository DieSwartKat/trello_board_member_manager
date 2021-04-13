from boards.models import *
from boards.serializers import *

import board_manager.settings as settings
from libraries.Client import Client

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView

from rest_framework.response import Response

class BoardViewset(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'board_id']

class MemberViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'fullname', 'member_id', 'boards']

class BoardMemberViewset(viewsets.ModelViewSet):
    queryset = BoardMember.objects.all()
    serializer_class = BoardMemberSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['board', 'member']

class UpdateBoards(APIView):
    permission_classes = [permissions.IsAuthenticated]
    connection = {'trello_api_key': settings.TRELLO_API_KEY, 'trello_api_token': settings.TRELLO_API_TOKEN}
    _connection = Client(connection)._connection
    def get(self, request, format=None):
        boards = self._connection.members.get(settings.TRELLO_MAIN_USERNAME)['idBoards']
        for board in boards:
            answer = self._connection.boards.get(board)
        
            return Response(answer)


from boards.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['name', 'board_id']


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['username', 'fullname', 'member_id', 'boards']


class BoardMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoardMember
        fields = ['board', 'members']
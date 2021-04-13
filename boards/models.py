from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=250)
    board_id = models.CharField(max_length=250)
    def __str__(self):
        return str(self.pk) + " " + self.name + " - " + self.id

class Member(models.Model):
    username = models.CharField(max_length=250)
    fullname = models.CharField(max_length=250)
    member_id = models.CharField(max_length=250)
    def __str__(self):
        return str(self.pk) + " " + self.fullname + " " + self.id

class BoardMember(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    members = models.ForeignKey(Member, on_delete=models.PROTECT)
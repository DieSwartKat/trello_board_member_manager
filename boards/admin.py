from django.contrib import admin

from boards.models import *

# @admin.register(Board)
# class sheetAdmin(admin.ModelAdmin):
#     search_fields = ('name', 'board_id')
#     list_display = ('name', 'board_id')


# @admin.register(Member)
# class memberAdmin(admin.ModelAdmin):
#     search_fields =  ('username', 'fullname', 'member_id', 'boards')
#     list_display =  ('username', 'fullname', 'member_id', 'boards')


# @admin.register(BoardMember)
# class boardmemberAdmin(admin.ModelAdmin):
#     search_fields =  ('board', 'member')
#     list_display =  ('board', 'member')

admin.site.register(Board)
admin.site.register(Member)
admin.site.register(BoardMember)
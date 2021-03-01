from django.contrib import admin
from .models import Post 
#관리자에서 날짜 검색 허용
from datetime import date
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
#WYSWYG 에디터 기능 추가
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post) # used instead of separate register
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('title', "writer",'slug', 'status','create_date')
    list_filter = ("status",
                   ('create_date', DateRangeFilter),
                   ('update_date', DateRangeFilter),
                  )

    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
  
    # If you would like to add a default range filter
    # method pattern "get_rangefilter_{field_name}_default"
    def get_rangefilter_create_date_default(self, request):
        return (date.today, date.today)
            # If you would like to add a default range filter
    # method pattern "get_rangefilter_{field_name}_default"
    def get_rangefilter_update_date_default(self, request):
        return (date.today, date.today)

    # If you would like to change a title range filter
    # method pattern "get_rangefilter_{field_name}_title"
    #def get_rangefilter_created_at_title(self, request, field_path):
    #    return 'custom title'

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)

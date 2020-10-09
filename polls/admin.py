from django.contrib import admin
from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text','pub_date','creation_date','was_published_recently',)
    search_fields = ('question_text',)
    list_filter = ('pub_date',)
    readonly_fields = ('was_published_recently',)

    fieldsets = (
        ('dados da questão',{'fields': ('question_text',)}),
        ('iformações',{'fields': ('pub_date','creation_date','was_published_recently',)}),
    )

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

from django.contrib import admin
from polls.models import Question, Choice
from django.utils import timezone

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    readonly_fields = ('votes','creation_date',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text','pub_date','creation_date','was_published_recently',
    'choice_count','is_public',)
    search_fields = ('question_text',)
    list_filter = ('pub_date',)
    readonly_fields = ('was_published_recently','is_public',)

    fieldsets = (
        ('dados da questão',{'fields': ('question_text',)}),
        ('iformações',{'fields': ('pub_date','creation_date','was_published_recently','is_public',)}),
    )
    inlines = (ChoiceInline,)
    actions = ('action_pub_date_now','action_is_public','action_not_is_public',)

    def choice_count(self, obj):
        return obj.choice_set.count()
    
    choice_count.short_description = 'N° de escolhas'

    def action_pub_date_now(self,request,queryset):
        for question in queryset:
            question.pub_date = timezone.now()
            question.save()
    def action_is_public(self,request,queryset):
        for question in queryset:
            question.is_public = True
            question.save()
    def action_not_is_public(self,request,queryset):
        for question in queryset:
            question.is_public = False
            question.save()

    action_pub_date_now.short_description = 'publicar agora'
    action_is_public.short_description = 'e publico'
    action_not_is_public.short_description = 'e privado'

admin.site.register(Question, QuestionAdmin)


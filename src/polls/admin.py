from django.contrib import admin
from polls.models import Question,Choice
from django.utils.translation.trans_real import inline_re

# Register your models here.
#StackedInline
class ChoiceInline(admin.TabularInline):
    model = Choice 
    extra = 3
    
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_test']}),
        ('Date information', {'fields': ['pub_date' ]}),
    ]
    search_field =['question_test']
    list_display =('question_test','pub_date','was_published_recently')
    inlines = [ChoiceInline]
    list_filter =['pub_date']
admin.site.register(Question,QuestionAdmin)

from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # re-arrange Fields in Admin Form
    # fields = ['pub_date', 'q_text']
    # Split form fields into fieldsets
    fieldsets = [
        (None, {'fields': ['q_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    # Add Choices to Questions Form
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
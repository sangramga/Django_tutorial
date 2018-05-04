from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# help 
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

    # customize change list page in admin form -
    # the one that displays all the questions in the system.
    # By default Django only shows str() of object
    list_display = ('q_text', 'pub_date', 'was_published_recently')

    # add an improvement to the Question change list page:
    # filters using the list_filter.
    list_filter = ['pub_date']

    """
    Adds a search box at the top of the change list.
    search for question_text field. Use as many fields as you’d like
    – although because it uses a LIKE query behind the scenes,
    limiting the number of search fields to a reasonable number.
    """
    search_fields = ['q_text']

    """Number of objects per page of change list Default = 100"""
    list_per_page = 10


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Choice, Question

# Register your models here.

class ChoiceInLine(admin.StackedInLine):
    model = ChoiceInLine
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)

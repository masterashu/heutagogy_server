from django.contrib import admin
from evaluation.models import Test1, Question, Option
# Register your models here.


class OptionsInline(admin.TabularInline):
    model = Option


@admin.register(Question)
class QuestionInline(admin.ModelAdmin):
    inlines = [
        OptionsInline,
    ]
    question = 'text'


@admin.register(Test1)
class Test1Inline(admin.ModelAdmin):
    pass

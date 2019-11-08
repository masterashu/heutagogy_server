from django.contrib import admin
from django import forms
from evaluation.models import Test1, Question, Option, Lesson, Test2, PictureDescriptionPair
from evaluation.models import NumberList, Test3
# Register your models here.


# Test 1
class OptionsInline(admin.TabularInline):
    model = Option
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        OptionsInline,
    ]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Test1)
class Test1Admin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]


class Test1Inline(admin.TabularInline):
    verbose_name_plural = "Multiple Choices Tests"
    verbose_name = "Multiple Choices Test"
    model = Test1
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['name', 'heading',]
        else:
            return []


# Test 2
class PicturePairInline(admin.TabularInline):
    model = PictureDescriptionPair
    extra = 1


@admin.register(Test2)
class Test2Admin(admin.ModelAdmin):
    inlines = [
        PicturePairInline,
    ]


class NumberListInline(admin.TabularInline):
    model = NumberList
    extra = 1
    verbose_name_plural = "Numbers List (space separated, max. 5 recommended)"


@admin.register(Test3)
class Test3Admin(admin.ModelAdmin):
    inlines = [
        NumberListInline,
    ]


class Test3Inline(admin.TabularInline):
    verbose_name_plural = "Number Sorting Puzzles"
    verbose_name = "Number Sorting Puzzle"
    model = Test3
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['name', 'heading',]
        else:
            return []


class Test2Inline(admin.TabularInline):
    verbose_name_plural = "Picture Description Pairs"
    verbose_name = "Picture Description Match"
    model = Test2
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['name', 'heading', ]
        else:
            return []


class LessonForm(forms.ModelForm):
    study_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Lesson
        fields = ['title', 'intro_text', 'study_text']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    inlines = [
        Test1Inline,
        Test2Inline,
        Test3Inline
    ]

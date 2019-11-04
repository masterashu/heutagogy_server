from django.contrib import admin
from evaluation.models import Test1, Question, Option, Lesson, Test2, PictureDescriptionPair
from evaluation.models import NumberList, Test3
# Register your models here.


# Test 1
class OptionsInline(admin.TabularInline):
    model = Option


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
    verbose_name_plural = "Multiple Choices Questions"
    verbose_name = "Multiple Choices Question"
    model = Test1
    extra = 1


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


class Test2Inline(admin.TabularInline):
    verbose_name_plural = "Picture Description Pairs"
    verbose_name = "Picture Description Match"
    model = Test2
    extra = 1


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [
        Test1Inline,
        Test2Inline,
        Test3Inline
    ]

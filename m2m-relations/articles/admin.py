from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_count += 1
            else:
                continue
        if main_count == 0:
            raise ValidationError('Укажите основной тег')        
        elif main_count > 1:
            raise ValidationError('Основной тег может быть только один')
        
        return super().clean()


@admin.register(Tag)    
class TagAdmin(admin.ModelAdmin):
    pass


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
   
# admin.py
from django.contrib import admin
from django import forms
from django_quill.forms import QuillFormField
from .models import QuillPost

class QuillPostAdminForm(forms.ModelForm):
    content = QuillFormField()

    class Meta:
        model = QuillPost
        fields = '__all__'

class QuillPostAdmin(admin.ModelAdmin):
    form = QuillPostAdminForm
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image', 'content', 'date'),
        }),
    )

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',),
        }

admin.site.register(QuillPost, QuillPostAdmin)

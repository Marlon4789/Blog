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
            'all': (
                'admin/css/custom_admin.css',
                'https://cdn.quilljs.com/1.3.6/quill.snow.css',
                'https://cdn.jsdelivr.net/npm/prismjs/themes/prism.css',
                ),
        }
        js = (
            'https://cdn.quilljs.com/1.3.6/quill.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.js',
            '/static/js/quill_config.js',  # Asegúrate de que esta ruta sea correcta
        )

admin.site.register(QuillPost, QuillPostAdmin)

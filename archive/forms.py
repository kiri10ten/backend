from django.forms import ModelForm

from .models import Archive

class ArchiveForm(ModelForm):
    class Meta:
        model = Archive
        fields = (
             'subject',
            'title',
            'description',
            'url'
        )

   
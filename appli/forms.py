from django import forms

from appli.models.image import Image
from appli.models.tag import Tag

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(selfself, tag):
        return "%s" % tag.nom

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['chemin','username']
        fields= ['tags']

    tags = CustomMMCF(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)


from django import forms

from petstagram.common.models import PhotoComment


class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = '__all__'

class SearchPhotosForm(forms.Form):
    pet_name = forms.CharField(
        max_length=50,
        required=False,
    )
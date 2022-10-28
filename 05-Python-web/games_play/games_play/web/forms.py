from django import forms
from games_play.web.models import Profile, Game




class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"

class GameCreateForm(GameBaseForm):
    pass

class GameDetailForm(GameBaseForm):
    pass

class GameEditForm(GameBaseForm):
    pass

class GameDeleteForm(GameBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly']= 'readonly'
            field.widget.attrs['disabled'] = 'disabled'



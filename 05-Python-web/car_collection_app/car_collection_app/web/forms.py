from django import forms
from car_collection_app.web.models import Profile, Car


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_name', 'email', 'age', 'password' )
        password = forms.CharField(
            widget=forms.PasswordInput
        )

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def save(self, commit =True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()

        return self.instance

class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class CarCreateForm(CarBaseForm):
    pass

class CarEditForm(CarBaseForm):
    pass

class CarDeleteForm(CarBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.__set_disabled_fields()
    def save(self, commit =True):
        if commit:
            self.instance.delete()

        return self.instance
    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.disabled = True

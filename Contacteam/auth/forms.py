from django import forms
from django.contrib.auth import models


class addUser(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(addUser, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'username', 'password',)
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

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

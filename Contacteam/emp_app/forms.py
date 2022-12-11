from django import forms
from emp_app import models


class addEmpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(addEmpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.Employee
        exclude = ('hire_date', 'employer',)


class addDeptForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(addDeptForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.Department
        fields = ('name', 'location',)

from django import forms
from app2.models import Department


class MovieChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    Department = forms.ModelMultipleChoiceField(queryset=Department.objects.all(), required=False)
    print(Department)

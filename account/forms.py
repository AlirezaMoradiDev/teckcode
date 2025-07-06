from django import forms
from django.core.exceptions import ValidationError

from .models import Skill, MyUser, InstructorProfile


class InstructorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    input_new_skill = forms.CharField(required=False)

    class Meta:
        model = InstructorProfile
        fields = [
            'image',
            'skill',
            'bio',

        ]

    def clean(self):
        super().clean()
        account = MyUser.objects.get(id=self.user.id)
        if not account.is_instructor:
            raise ValidationError('you not access')
        else:
            self.cleaned_data['name'] = self.user
            return self.cleaned_data


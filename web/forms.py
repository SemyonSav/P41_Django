from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя')
    age = forms.IntegerField(label='Возраст')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['age'] < 18:
            self.add_error('age', 'Возраст меньше 18')
        return cleaned_data


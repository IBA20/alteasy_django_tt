from django import forms


class SettingsForm(forms.Form):
    name = forms.BooleanField(label='Название', required=False, disabled=True)
    title = forms.BooleanField(label='Заглавие', required=False)
    author = forms.BooleanField(label='Автор', required=False)
    description = forms.BooleanField(label='Описание', required=False)
    price = forms.BooleanField(label='Цена', required=False)

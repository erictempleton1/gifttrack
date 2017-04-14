from django import forms


class GiftForm(forms.Form):
    gift_desc = forms.CharField(
        label='Gift Description',
        widget=forms.TextInput(
            attrs={'max_length': 500}
        )
    )
    gift_from = forms.CharField(
        label='Gift From',
        widget=forms.TextInput(
            attrs={'max_length': 200}
        )
    )
    gift_notes = forms.CharField(
        label='Gift Notes',
        widget=forms.TextInput(
            attrs={'max_length': 500}
        )
    )


class RegForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'max_length': 150}
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'required': True, 'max_length': 150}
        ),
    )
    password_confirm = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'required': True, 'max_length': 150}
        )
    )


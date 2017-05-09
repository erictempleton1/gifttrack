from django import forms


def base_attrs():
    return {
        'required': True,
        'max_length': 150,
        'class': 'mdl-textfield__input'
    }


class GiftForm(forms.Form):
    mod_base_attrs = base_attrs()
    mod_base_attrs['max_length'] = 500
    gift_desc = forms.CharField(
        label='Gift Description',
        widget=forms.TextInput(
            attrs=mod_base_attrs
        )
    )
    mod_base_attrs['max_length'] = 200
    gift_from = forms.CharField(
        label='Gift From',
        widget=forms.TextInput(
            attrs=mod_base_attrs
        )
    )
    mod_base_attrs['max_length'] = 500
    gift_notes = forms.CharField(
        label='Gift Notes',
        widget=forms.TextInput(
            attrs=mod_base_attrs
        )
    )


class RegForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs=base_attrs()
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs=base_attrs()
        ),
    )
    password_confirm = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs=base_attrs()
        )
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs=base_attrs()
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs=base_attrs()
        )
    )


class GiftListForm(forms.Form):
    name = forms.CharField(
        label="Gift List Name",
        widget=forms.TextInput(
            attrs=base_attrs()
        )
    )
    description = forms.CharField(
        label="Gift List Name",
        widget=forms.TextInput(
            attrs=base_attrs()
        )
    )

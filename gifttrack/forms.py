from django import forms


class GiftForm(forms.Form):
    gift_desc = forms.CharField(label='Gift Description: ', max_length=500)
    gift_from = forms.CharField(label='Gift From: ', max_length=200)
    gift_notes = forms.CharField(label='Gift Notes: ', max_length=500)

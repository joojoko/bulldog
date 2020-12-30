from django import forms


class ContactForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': 'Please enter the subject'
        },
        max_length=128, label="Subject")
    contents = forms.CharField(
        error_messages={
            'required': 'Please enter your details.'
        },
        widget=forms.Textarea, label="Details")

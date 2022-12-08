from django import forms


class BorrowForm(forms.Form):
    due_back = forms.DateTimeField(widget=forms.SelectDateWidget)
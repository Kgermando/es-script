from django import forms

class ReportFilterForm(forms.Form):
    datetime_range = forms.CharField(
        label='Choose Date and time Range:',
        widget=forms.TextInput(attrs={
            'class': 'form-control pull-right',
            'name': 'datetimerange',
            'id': 'datetimerange',
            'width': '200px',
            }
        ),
        required=False,
    )


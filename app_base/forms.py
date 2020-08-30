from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .models import TestModel
# Jalali DateTimePicker Widget imports
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime



class DateTimepickerForm(forms.Form):
    date_input = forms.DateTimeField(widget=AdminDateWidget())
    time_input = forms.DateTimeField(widget=AdminTimeWidget())
    date_time_input = forms.DateTimeField(widget=AdminSplitDateTime())


class JalaliDateTimepickerForm(forms.Form):
    date_input = forms.DateTimeField(widget=AdminJalaliDateWidget)
    date_time_input = forms.DateTimeField(widget=AdminSplitDateTime)

class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ('date', 'date_time')

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=('date'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        self.fields['date_time'] = SplitJalaliDateTimeField(label=('date time'), 
            widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        )

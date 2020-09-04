from django import forms
from .models import FactorModel, ProductModel
import re


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = (
            'title', 'number', 'price',
        )


class FactorForm(forms.ModelForm):
    class Meta:
        model = FactorModel
        fields = (
            'customer_name',
            'customer_last_name',
            'customer_phone_number',
            'customer_postal_code',
            'customer_national_code',
            'customer_city',
            'customer_state',
            'customer_birthdate',
            'customer_address',
            'description',
            'purchase_method',
        )

    def clean_customer_national_code(self):
        cd = self.cleaned_data
        if not re.search(r'^\d{10}$', cd['customer_national_code']):
            raise forms.ValidationError(
                'لطفا کد ملی را به صورت کامل وارد کنید - کد ملی شامل ده رقم است')

        nums = []
        last_num = int(cd['customer_national_code'][9])
        for i in range(9):
            nums.append(int(cd['customer_national_code'][i]) * (10 - i))

        remain = sum(nums) % 11
        if (remain < 2 and last_num == remain) or (remain >= 2 and 11 - remain == last_num):
            return cd['customer_national_code']
        else:
            raise forms.ValidationError(
                'معتبر نیست داداش ی بار دیگه وارد کن ایندفعه با دقت بیشتر لطفا '
            )


# from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
# Jalali DateTimePicker Widget imports
# from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
# from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


# class DateTimepickerForm(forms.Form):
#     date_input = forms.DateTimeField(widget=AdminDateWidget())
#     time_input = forms.DateTimeField(widget=AdminTimeWidget())
#     date_time_input = forms.DateTimeField(widget=AdminSplitDateTime())


# class JalaliDateTimepickerForm(forms.Form):
#     date_input = forms.DateTimeField(widget=AdminJalaliDateWidget)
#     date_time_input = forms.DateTimeField(widget=AdminSplitDateTime)

# class TestForm(forms.ModelForm):
#     class Meta:
#         model = TestModel
#         fields = ('date', 'date_time')

#     def __init__(self, *args, **kwargs):
#         super(TestForm, self).__init__(*args, **kwargs)
#         self.fields['date'] = JalaliDateField(label=('date'), # date format is  "yyyy-mm-dd"
#             widget=AdminJalaliDateWidget # optional, to use default datepicker
#         )

#         # you can added a "class" to this field for use your datepicker!
#         # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

#         self.fields['date_time'] = SplitJalaliDateTimeField(label=('date time'),
#             widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
#         )

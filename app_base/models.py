from django.core.validators import RegexValidator
from django_jalali.db import models as jmodels
from django.db import models
from django.contrib.auth.models import User
from .widgets import IconPicker

PRODUCTS = (
    (1, 'یخچال/فریزر (REF)'),
    (2, 'اجاق گاز (GC)'),
    (3, 'ماشین لباسشویی (WM)'),
    (4, 'تلویزیون (TV)'),
    (5, 'لوازم خانگی کوچک (SHA)'),
    (6, 'متفرقه (OTHER)'),
    (7, 'محصولات نوکار (BI)'),
    (8, 'ماشین ظرفشویی (DW)'),
    (9, 'تهویه هوا (AC)')
)


class ProductList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    test = IconPicker(max_length=100, null=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    prodict_list = models.ForeignKey(
        ProductList, on_delete=models.CASCADE, null=True)
    title = models.PositiveSmallIntegerField(null=True, choices=PRODUCTS)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    # @property
    # def title(self):
    #     return self._title

    # @title.setter
    # def title(self, value):
    #     if ...:
    #         self._title = 2

    def __str__(self):
        return str(self.title)


class TestModel(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    date_time = models.DateTimeField()


# purchase_method = (
#     ('purchase_method_1', 1),
#     ('purchase_method_2', 2),
# )


# class FactorModel(models.Model):
#     customer_name = models.CharField(max_length=20)
#     customer_last_name = models.CharField(max_length=80)
#     customer_phone_number = models.CharField(max_length=12)
#     customer_postal_code = models.CharField(max_length=10,
#                                             validators=[RegexValidator(r'^\d{10}$')])
#     customer_national_code = models.CharField(max_length=10,
#                                               validators=[RegexValidator(r'\b(?!(\d)\1{3})[13-9]{4}[1346-9][013-9]{5}\b')])
#     customer_city = models.CharField(max_length=20)
#     # any better idea for saving it in a better format
#     customer_state = models.CharField(max_length=20)
#     customer_birth = jmodels.jDateTimeField()
#     customer_address = models.CharField(max_length=200)
#     customer_extra_explanation = models.CharField(null=True)
#     purchase_method = models.CharField(choices=purchase_method)
#     product_title = models.CharField(max_length=20)
#     product_brand = models.CharField(max_length=20)
#     product_number = models.PositiveIntegerField(default=0)
#     amount = models.PositiveIntegerField(default=0)
#     datetime = jmodels.jDateTimeField() # add_now True
#     staff_username = models.CharField() # staff username, the guy who filled the form, and maybe a foreinkey


# # what the am i suppose to do with 'brand' field in 'product' model

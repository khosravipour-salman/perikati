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
    product_title = models.PositiveSmallIntegerField(
        null=True, choices=PRODUCTS)

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
    date = jmodels.jDateField()
    date_time = jmodels.jDateTimeField()

# /////////////////////// project models ///////////////////////



class FactorModel(models.Model):
    customer_name = models.CharField(max_length=20, verbose_name=u'نام خریدار')
    customer_last_name = models.CharField(max_length=80, verbose_name=u'نام خانوادگی خریدار')
    customer_phone_number = models.CharField(max_length=12, verbose_name=u'شماره همراه خریدار')
    customer_postal_code = models.CharField(max_length=10,
                                            validators=[RegexValidator(r'^\d{10}$')], verbose_name=u'کد پستی')
    customer_national_code = models.CharField(max_length=10, verbose_name=u'کد ملی خریدار')
    customer_city = models.CharField(max_length=20, verbose_name=u'شهر')
    customer_state = models.CharField(max_length=20, verbose_name=u'استان')
    customer_birthdate = models.CharField(max_length=10, null=True, verbose_name=u'تاریخ تولد خریدار')
    customer_address = models.CharField(max_length=200, verbose_name=u'آدرس')
    description = models.CharField(null=True, max_length=300, verbose_name=u'توضیحات')
    purchase_method = models.CharField(max_length=20, verbose_name=u'نحوه تسویه حق العمل')
    # products = models.ForeignKey(
    #     ProductModel, on_delete=models.CASCADE, related_name='factors', null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    # this field gotta change to on_delete=set.null
    staff_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'مشتری')

    class Meta:
        ordering = ('-datetime',)
        verbose_name_plural = 'پیش فاکتور ها'
        verbose_name = 'پیش فاکتور'

    def __str__(self):
        return f'پیش فاکتور {self.id} برای {self.customer_name} {self.customer_last_name}'


class ProductModel(models.Model):
    title = models.CharField(choices=PRODUCTS, max_length=100, verbose_name=u'نام محصول')
    factors = models.ForeignKey(FactorModel, on_delete=models.CASCADE, related_name='products', null=True)
    # brand = models.CharField(max_length=80) # wait till get the answer
    number = models.PositiveIntegerField(default=0, verbose_name=u'تعداد محصول')
    price = models.PositiveIntegerField(default=0, verbose_name=u'مبلغ به ریال')

    def __str__(self):
        return f'{self.number} of {self.title} and price is: {self.price}'

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'

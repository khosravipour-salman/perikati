# from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from django.contrib import admin
from .models import Product, ProductList, TestModel


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1


class ProductListAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)


admin.site.register(Product)
admin.site.register(ProductList, ProductListAdmin)





# from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin  

# class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
#     model = TestModel

# class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
#     model = TestModel

# @admin.register(TestModel)
# class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
#     inlines = (MyInlines1, MyInlines2, )
#     readonly_fields = ('name', 'date', 'date_time',)
# class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
#     model = TestModel


# # class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
# #     model = ThirdModel


# @admin.register(TestModel)
# class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
#     # show jalali date in list display
#     list_display = ['name', 'get_created_jalali']

#     inlines = (MyInlines1, MyInlines2, )
#     raw_id_fields = ('name', )
#     readonly_fields = ('name', 'date_field',)
#     # you can override formfield, for example:
#     formfield_overrides = {
#         JSONField: {'widget': JSONEditor},
#     }

#     def get_created_jalali(self, obj):
#         return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

#     get_created_jalali.short_description = 'تاریخ ایجاد'
#     get_created_jalali.admin_order_field = 'created'

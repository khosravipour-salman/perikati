# from jalali_date import datetime2jalali, date2jalali
from django.shortcuts import render, redirect
# from .forms import DateTimepickerForm, JalaliDateTimepickerForm
from .models import PRODUCTS, FactorModel, ProductModel
from .forms import FactorForm, ProductForm
from pprint import pprint
from .city_list import city_list
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms.utils import ErrorList


@login_required(login_url='admin/login')
def index(request):
    fixed_products = {}
    flag = 0
    price_total = 0
    if request.method == 'POST':
        for key, value in request.POST.items():
            if 'product' in key:
                products = {}
                if not key.find('csrfmiddlewaretoken'):
                    continue
                if value:
                    products[key] = value
                for key, value in products.items():
                    item = key.split('-')
                    if item[2] not in fixed_products.keys():
                        fixed_products[item[2]] = {item[1]: value}
                    else:
                        fixed_products[item[2]][item[1]] = value
        if not products:
            return redirect('index')
        if fixed_products:
            flag = 1

        initial = {
            'customer_name': request.POST.get('customer_name'),
            'customer_last_name': request.POST.get('customer_last_name'),
            'customer_phone_number': request.POST.get('customer_phone_number'),
            'customer_postal_code': request.POST.get('customer_postal_code'),
            'customer_national_code': request.POST.get('customer_national_code'),
            'customer_city': request.POST.get('city'),
            'customer_birthdate': request.POST.get('customer_birthdate'),
            'customer_address': request.POST.get('customer_address'),
            'csrfmiddlewaretoken': request.POST.get('csrfmiddlewaretoken'),
        }

        if request.POST.get('state') != 'استان را انتخاب کنید':
            initial.update({'customer_state': request.POST.get('state')})

        if request.POST.get('purchase-method') == 'نقدی' or request.POST.get('purchase-method') == 'کارت اعتباری' :
            initial.update(
                {'purchase_method': request.POST.get('purchase-method')})

        if request.POST.get('description'):
            initial.update({'description': request.POST.get('description')})

        form = FactorForm(data=initial)
        if form.is_valid():
            flag = 2
            new_form = form.save(commit=False)
            new_form.staff_user = request.user
            new_form.save()

            for product in fixed_products:
                product_initial = {
                    'title': product,
                    'number': int(fixed_products[product]['count']),
                    'price': int(fixed_products[product]['price']),
                }
                price_total = product_initial['price'] + price_total

                product_form = ProductForm(data=initial)
                if product_form.is_valid():
                    new_product_form = product_form.save(commit=False)
                    new_product_form.factor = new_form
                    new_product_form.save()
                else:
                    print(product_form.errors)
                # products_objects.append(
                #     ProductModel(
                #         title=int(product),
                #         number=int(fixed_products[product]['count']),
                #         price=int(fixed_products[product]['price'])
                #     )
                # )
                # product_saved_obj = products_objects[-1].save()
                # product_saved_obj.factor = new_form
                # product_saved_obj.save()
            # for obj in products_objects:
            #     new_form.products = obj
            #     new_form.save()

        else:
            flag = 1
            print(
                "i'm your error and i'm still here =======================================================")
            # print(form.errors)
    else:
        form = FactorForm()

    # if request.method == 'POST':  # Create mode
    #     # Products data getting ready to save to model
    #     products = {}
    #     customer_information = {}
    #     for key, value in request.POST.items():
    #         if 'product' in key:
    #             if not key.find('csrfmiddlewaretoken'):
    #                 continue
    #             if value:
    #                 products[key] = value

    #             fixed_products = {}
    #             for key, value in products.items():
    #                 item = key.split('-')
    #                 if item[2] not in fixed_products.keys():
    #                     fixed_products[item[2]] = {item[1]: value}
    #                 else:
    #                     fixed_products[item[2]][item[1]] = value
    #         else:
    #             if not key.find('csrfmiddlewaretoken'):
    #                 continue
    #             if value:
    #                 customer_information.update({key: value})
    #         flag = 2

        # products_objects = []
        # for product in fixed_products:
        #     products_objects.append(
        #         ProductModel(
        #             title=int(product),
        #             number=int(fixed_products[product]['count']),
        #             price=int(fixed_products[product]['price'])
        #         )
        #     )
        #     products_objects[-1].save()

    #     factor_obj = FactorModel(
        # customer_name=customer_information['name'],
        # customer_last_name=customer_information['last-name'],
        # customer_phone_number=customer_information['phone-number'],
        # customer_postal_code=customer_information['postal-code'],
        # customer_national_code=customer_information['national-code'],
        # customer_city=customer_information['city'],
        # customer_state=customer_information['state'],
        # customer_birthdate=customer_information['birthdate'],
        # customer_address=customer_information['address'],
        # description=customer_information['description'],
        # purchase_method=customer_information['purchase-method'],
        # staff_user=request.user,
    #     )
    #     factor_obj.save(commit=False)
    #     factor_obj.products = (*products_objects)

    #     print(factor_obj)

    # if request.method == 'POST':  # create mode
    #     products = {}
    #     for key, value in request.POST.items():
    #         if value:
    #             # print(key, value)
    #             products[key] = value
    #     pprint(products)

    #     for key, value in products.items():

    #         # pprint.pprint(products)
    #         # return render(request, 'index.html', context)
    #         # default view

    # form = DateTimepickerForm()

    context = {
        'form': form,
        # 'section': 'index',
        'flag': flag,
        'products': PRODUCTS,
        'city_list': city_list,
        'fixed_product': fixed_products,
    }
    if price_total:
        context.update({'price_total': price_total})

    return render(request, 'index.html', context)


# @login_required(login_url='/admin/login')
def logout_user(request):
    logout(request)
    # return redirect('login')
    return HttpResponse('login')
# def my_view(request):
#     jalali_join = datetime2jalali(
#         request.user.date_joined
#     ).strftime('%y/%m/%d _ %H:%M:%S')
#     form = JalaliDateTimepickerForm()
#     context = {
#         'form': form,
#         'section': 'date',
#         'date': jalali_join,
#     }
#     return render(request, 'index.html', context)

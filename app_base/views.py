from jalali_date import datetime2jalali, date2jalali
from django.shortcuts import render
from .forms import DateTimepickerForm, JalaliDateTimepickerForm
from .models import PRODUCTS
from pprint import pprint
from .city_list import city_list


def index(request):
    flag = False
    if request.method == 'POST':  # Create mode
        # Products data getting ready to save to model
        products = {}
        customer_information = {}
        for key, value in request.POST.items():
            if 'product' in key:
                if not key.find('csrfmiddlewaretoken'):
                    continue
                if value:
                    products[key] = value

                fixed_product = {}
                for key, value in products.items():
                    item = key.split('-')
                    if item[2] not in fixed_product.keys():
                        fixed_product[item[2]] = {item[1]: value}
                    else:
                        fixed_product[item[2]][item[1]] = value
            else:
                if not key.find('csrfmiddlewaretoken'):
                    continue
                if value:
                    customer_information.update({key: value})
            flag = True
        # set flag for startindex in fieldset for step jquery
        #

    else:
        pass
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
        # 'form': form,
        # 'section': 'index',
        'products': PRODUCTS,
        'city_list': city_list,
    }
    return render(request, 'index.html', context)


def my_view(request):
    jalali_join = datetime2jalali(
        request.user.date_joined
    ).strftime('%y/%m/%d _ %H:%M:%S')
    form = JalaliDateTimepickerForm()
    context = {
        'form': form,
        'section': 'date',
        'date': jalali_join,
    }
    return render(request, 'index.html', context)

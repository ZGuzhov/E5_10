from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
import operator
from cars.models import Car


def reduce(func, items):
    result = items.pop()
    for item in items:
        result = func(result, item)

    return result


class CarsListView(ListView):

    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        # context = super().get_queryset()
        context = Car.objects.all()
        get_params = self.request.GET.dict()

        if get_params:
            q_list = []
            if get_params['brand'] == '':
                del(get_params['brand'])
            else:
                q_list.append(Q(brand=get_params['brand']))
            
            if get_params['model'] == '':
                del(get_params['model'])
            else:
                q_list.append(Q(model=get_params['model']))
            
            if get_params['gearbox'] == 'Выберите коробку передач':
                del(get_params['gearbox'])
            else:
                q_list.append(Q(gearbox=get_params['gearbox']))
            
            if get_params['year'] == '':
                del(get_params['year'])
            else:
                q_list.append(Q(year=get_params['year']))
            
            if get_params['color'] == '':
                del(get_params['color'])
            else:
                q_list.append(Q(color=get_params['color']))

            if q_list:
                context = Car.objects.filter(reduce(operator.and_, q_list))
        
        return context
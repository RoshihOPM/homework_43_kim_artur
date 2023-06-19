from django.shortcuts import render
from django import forms


# Create your views here


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def res_view(request):
    try:
        fir_num = float(request.POST.get('fir_num'))
        sec_num = float(request.POST.get('sec_num'))
        operation = request.POST.get('operation')
        result = 0
        if sec_num == 0 and operation == 'div':
            result = 'Divide by zero forbidden'
            result_to_rend = {'Result': result}
            return render(request, 'error.html', result_to_rend)
        if operation == 'add':
            sign = '+'
            result =  fir_num + sec_num
        if operation == 'sub':
            sign = '-'
            result = fir_num - sec_num
        if operation == 'mult':
            sign = '*'
            result = fir_num * sec_num
        if operation == 'div':
            sign = '/'
            result = fir_num / sec_num
        if fir_num == int(fir_num):
            fir_num = int(fir_num)
        if sec_num == int(sec_num):
            sec_num = int(sec_num)
        if result == int(result):
            result = int(result)
        res_as_str = f'{fir_num} {sign} {sec_num} = {round(result, 2)}'
        result_to_rend = {'Result': res_as_str}
        return render(request, 'result.html', result_to_rend)
    except ValueError:
        result_to_rend = {'Result': 'Enter numbers'}
        return render(request, 'error.html', result_to_rend)

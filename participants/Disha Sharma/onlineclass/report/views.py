from django.shortcuts import render


def sheet(request):
    return render(request, 'report/sheets1.html', {})
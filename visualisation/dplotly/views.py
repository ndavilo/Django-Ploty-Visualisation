from django.shortcuts import render
from .models import BTC, BNB, ETH
from django.shortcuts import render
import csv
from .forms import csvForm
from datetime import datetime

# Create your views here.
def Home(request):

    return render(request, 'home.html')

def UploadCSV(request):
    form = csvForm()
    alart = 'None'
    if request.method == 'POST' and request.FILES['myfile']:
        csvFile = request.FILES['myfile']
        csv_data = csvFile.read().decode("utf-8")

        csv_list = csv_data.split("\n")[1:]
        if str(request.POST['select']) == 'Bitcoin':
            BTC.objects.all().delete()
            for row in csv_list:
                row = row.split(",")
                btc = BTC(
                    Date    = row[0],
                    Open    = row[1],
                    High    = row[2],
                    Low     = row[3],
                    Close   = row[4],
                    AdjClose= row[5],
                    Volume  = row[6]
                )
                btc.save()
        if str(request.POST['select']) == 'Ethereum':
            ETH.objects.all().delete()
            for row in csv_list:
                row = row.split(",")
                eth = ETH(
                    Date    = row[0],
                    Open    = row[1],
                    High    = row[2],
                    Low     = row[3],
                    Close   = row[4],
                    AdjClose= row[5],
                    Volume  = row[6]
                )
                eth.save()
        
        if str(request.POST['select']) == 'Binance':
            BNB.objects.all().delete()
            for row in csv_list:
                row = row.split(",")
                bnb = BNB(
                    Date    = row[0],
                    Open    = row[1],
                    High    = row[2],
                    Low     = row[3],
                    Close   = row[4],
                    AdjClose= row[5],
                    Volume  = row[6]
                )
                bnb.save()

        context = {
            'alart':'saved',
            'form':form
        }
        return render(request, 'uploadcsv.html', context)
    
    context = {
        'alart':alart,
        'form':form
    }
    return render(request, 'uploadcsv.html', context)
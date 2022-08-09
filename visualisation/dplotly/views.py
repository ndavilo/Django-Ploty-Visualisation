from django.shortcuts import render
from .models import BTC, BNB, ETH
from django.shortcuts import render
import csv
from .forms import csvForm
from datetime import datetime
import plotly.express as px
import pandas as pd
import numpy as np

def NumpyArrary(database):
    Date    = [c.Date for c in database]
    Open    = [c.Open for c in database]
    High    = [c.High for c in database]
    Low     = [c.Low for c in database]
    Close   = [c.Close for c in database]
    AdjClose= [c.AdjClose for c in database]
    Volume  = [c.Volume for c in database]

    return np.array([Date, Open, High, Low, Close, AdjClose, Volume])

def CreateDataFrame(array, columns):
    df = pd.DataFrame(array, columns)
    return df.transpose()

def Home(request):
    btc = BTC.objects.all()
    eth = ETH.objects.all()
    bnb = BNB.objects.all()
    if request.method == 'POST':
        if str(request.POST['select']) == 'Bitcoin':
            df = CreateDataFrame(NumpyArrary(btc), ['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
            alart = 'Bitcoin'
        if str(request.POST['select']) == 'Ethereum':
            df = CreateDataFrame(NumpyArrary(btc), ['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
            alart = 'Ethereum'
        if str(request.POST['select']) == 'Binance':
            df = CreateDataFrame(NumpyArrary(btc), ['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
            alart = 'Binance'
    else:
         df = CreateDataFrame(NumpyArrary(btc), ['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
         alart = 'Bitcoin'
    fig = px.scatter(
        df,
        x='Date',
        y=['Open', 'High', 'Low', 'Close', 'AdjClose'],
        title='Cryptocurrency Line Plot'
    )
    scatterchart = fig.to_html()
    fig = px.box(
        df,
        x='Date',
        y=['Open', 'High', 'Low', 'Close', 'AdjClose'],
        title='Cryptocurrency Scatter Plot'
    )
    boxchart = fig.to_html()
    fig = px.line(
        df,
        x='Date',
        y=['Open', 'High', 'Low', 'Close', 'AdjClose'],
        title='Cryptocurrency Scatter Plot'
    )
    chart = fig.to_html()

    context = {
        'chart':chart,
        'scatterchart':scatterchart,
        'boxchart':boxchart,
        'alart':alart
    }
    return render(request, 'home.html', context)

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
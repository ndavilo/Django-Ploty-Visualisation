from django.shortcuts import render
from .models import BTC, BNB, ETH
from django.shortcuts import render
import csv
from datetime import datetime
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go


class PackData:
    def __init__(self, database):
        self.Date    = [c.Date for c in database]
        self.Open    = [c.Open for c in database]
        self.High    = [c.High for c in database]
        self.Low     = [c.Low for c in database]
        self.Close   = [c.Close for c in database]
        self.AdjClose= [c.AdjClose for c in database]
        self.Volume  = [c.Volume for c in database]

    def NumpyArrary(self):
        return np.array([self.Date, self.Open, self.High, self.Low, self.Close, self.AdjClose, self.Volume])

    def ZipData(self):
        return zip(self.Date[-10:], self.Open[-10:], self.High[-10:], self.Low[-10:], self.Close[-10:], self.AdjClose[-10:], self.Volume[-10:])

def CreateDataFrame(array, columns):
    df = pd.DataFrame(array, columns)
    return df.transpose()

class myplots:
    def __init__(self, df, title):
        self.df = df
        self.y=['Open', 'High', 'Low', 'Close', 'AdjClose']
        self.x='Date'
        self.title = title
        self.titlesize = {'font_size': 22, 'xanchor': 'center', 'x':0.5} #To resize and center the title

    def ScatterPlot(self): #For scatter plot
        fig = px.scatter(self.df, x=self.x, y=self.y, title=self.title+ ' Scatter Plot')
        fig.update_layout(title=self.titlesize)
        return fig.to_html()

    def BoxPlot(self): #For box plot
        fig = px.box(self.df, x=self.x, y=self.y, title=self.title+ ' Box Plot')
        fig.update_layout(title=self.titlesize)
        return fig.to_html()
    
    def LinePlot(self): #For line plot
        fig = px.line(self.df, x=self.x, y=self.y, title=self.title+ ' Line Plot')
        fig.update_layout(title=self.titlesize)
        return fig.to_html()

    def Candle(self):
        fig = go.Figure(data=[go.Candlestick(x=self.df['Date'],
                open=self.df['Open'],
                high=self.df['High'],
                low=self.df['Low'],
                close=self.df['Close']
                )])
        fig.update_layout(title=self.title+ ' Candle Plot')
        fig.update_layout(title={'font_size': 22, 'xanchor': 'center', 'x':0.5})
        return fig.to_html()

    def Bar(self):
        fig = go.Figure(
            data=[go.Bar(y=self.df['Close'])],
            layout_title_text="A Figure Displayed with fig.show()"
        )
        return fig.to_html()

    def scatter_matrix(self):  
        fig = px.scatter_matrix(self.df, dimensions=self.y)
        return fig.to_html()

class Gplots:
    def __init__(self, btc, eth, bnb):
        self.btc = btc
        self.eth = eth
        self.bnb = bnb
        self.y1 = [c.AdjClose for c in btc]
        self.y2 = [c.AdjClose for c in eth]
        self.y3 = [c.AdjClose for c in bnb]
        self.columns = ['Bitcoin', 'Ethereum', 'Binance']
        self.df = CreateDataFrame((np.array([self.y1, self.y2, self.y3])), self.columns)

    def Heatmap(self):
        fig = px.imshow(self.df)
        fig.update_layout(title= 'Heatmap')
        fig.update_layout(title={'font_size': 22, 'xanchor': 'center', 'x':0.5})
        return fig.to_html()
    
    def scatter_matrix(self):  
        fig = px.scatter_matrix(self.df, dimensions=self.columns)
        return fig.to_html()

    def CombinePlot(self):
        x = [c.Date for c in self.btc]
        x_rev = x[::-1]

        # Line 1
        y1 = self.y1
        y1_upper = [c.High for c in self.btc]
        y1_lower = [c.Low for c in self.btc]
        y1_lower = y1_lower[::-1]

        # Line 2
        y2 = self.y2
        y2_upper = [c.High for c in self.eth]
        y2_lower = [c.Low for c in self.eth]
        y2_lower = y2_lower[::-1]

        # Line 3
        y3 = self.y3
        y3_upper = [c.High for c in self.bnb]
        y3_lower = [c.Low for c in self.bnb]
        y3_lower = y3_lower[::-1]


        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=x+x_rev,
            y=y1_upper+y1_lower,
            fill='toself',
            fillcolor='rgba(0,100,80,0.2)',
            line_color='rgba(255,255,255,0)',
            showlegend=False,
            name='Binance',
        ))
        fig.add_trace(go.Scatter(
            x=x+x_rev,
            y=y2_upper+y2_lower,
            fill='toself',
            fillcolor='rgba(0,176,246,0.2)',
            line_color='rgba(255,255,255,0)',
            name='Ethereum',
            showlegend=False,
        ))
        fig.add_trace(go.Scatter(
            x=x+x_rev,
            y=y3_upper+y3_lower,
            fill='toself',
            fillcolor='rgba(231,107,243,0.2)',
            line_color='rgba(255,255,255,0)',
            showlegend=False,
            name='Binance',
        ))
        fig.add_trace(go.Scatter(
            x=x, y=y1,
            line_color='rgb(0,100,80)',
            name='Bitcoin',
        ))
        fig.add_trace(go.Scatter(
            x=x, y=y2,
            line_color='rgb(0,176,246)',
            name='Ethereum',
        ))
        fig.add_trace(go.Scatter(
            x=x, y=y3,
            line_color='rgb(231,107,243)',
            name='Binance',
        ))

        fig.update_traces(mode='lines')
        fig.update_layout(title='Cryptocurrency')
        fig.update_layout(title={'font_size': 22, 'xanchor': 'center', 'x':0.5})
        return fig.to_html()

def Home(request):
    btc = BTC.objects.all()
    eth = ETH.objects.all()
    bnb = BNB.objects.all()

    if request.method == 'POST' and request.POST['select']:
        requested = str(request.POST['select'])
        if requested == 'Ethereum':
            pack = PackData(eth)
            df = CreateDataFrame(pack.NumpyArrary(), ['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
            numpy = pack.ZipData()
            alart = 'Ethereum'
        elif requested == 'Binance':
            pack = PackData(bnb)
            df = CreateDataFrame(pack.NumpyArrary(), ['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
            numpy = pack.ZipData()
            alart = 'Binance'
        else:
            pack = PackData(btc)
            df = CreateDataFrame(pack.NumpyArrary(), ['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
            numpy = pack.ZipData()
            alart = 'Bitcoin'
    else:
        pack = PackData(btc)
        df = CreateDataFrame(pack.NumpyArrary(), ['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
        numpy = pack.ZipData()
        alart = 'Bitcoin'

    plot = myplots(df, alart)
    gplot = Gplots(btc, eth, bnb)

    context = {
        'chart':plot.LinePlot(),
        'scatterchart':plot.ScatterPlot(),
        'boxchart':plot.BoxPlot(),
        'mainchart':gplot.CombinePlot(),
        'candle':plot.Candle(),
        'heat':gplot.Heatmap(),
        'gscatter_matrix':gplot.scatter_matrix(),
        'bar':plot.Bar(),
        'scatter_matrix':plot.scatter_matrix(),
        'alart':alart,
        'numpy':numpy,
    }
    return render(request, 'home.html', context)

def UploadCSV(request):
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
        }
        return render(request, 'uploadcsv.html', context)
    
    context = {
        'alart':alart,
    }
    return render(request, 'uploadcsv.html', context)
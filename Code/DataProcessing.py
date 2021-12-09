from json import decoder
import math
import yfinance as yf
import numpy as np
import pandas as pd
from datetime import date
from datetime import timedelta
import math

class data:
    def __init__(self,ticker):
        self.ticker = ticker

    #generates the equavilent percentile strikes for historical data
    def strikeGeneration(pStrikes, price):
        adjStrikes = np.array([i*price for i in pStrikes])
        return adjStrikes

    # def deltaFunc( riskF, curPrice, strike, vola):
    #     d1 = (math.log(curPrice/strike) + .125(riskF + (vola**2)/(2)))/(vola * math.sqrt(.125))

    #     d2 = d1 - vola*math.sqrt(.125)

    #     normProbd1 = (1/math.sqrt(2*math.pi)) * math.e **-1((d1**2)/2)
    #     ## May need to figure out if I input d1 as -d1
    #     normProbd2 = (1/math.sqrt(2*math.pi)) * math.e **-1((d2**2)/2)
    #     ## May need to figure out if I input d2 as -d2
    #     delta = (strike*math.e**(-riskF*.125)) * normProbd2 - curPrice*normProbd1
    #     return delta

    #function to Standardize and Normalize a numpy array of data for use in volatility function
    def standardNormal(rawArray, extraArray):
        array = pd.concat([extraArray.tail(4), rawArray])
        mean = np.sum(array) / np.size(array)
        sd = np.std(array)
        normalized  = np.array([((x-mean)/sd) for x in array])
        return normalized

    def volatility(rawArray, extraArray):
        array = data.standardNormal(rawArray["Close"], extraArray["Close"])
        volatility = []
        for index, value in enumerate(array):
            if index > 3:
                prevWeek = array[index-4:index+1]
                mean = (np.sum(prevWeek))/5
                deviation = np.array([(x-mean)**2 for x in prevWeek])
                variance = np.sum(deviation)/5
                currVolatility = math.sqrt(variance)
                volatility.append(currVolatility)
        return volatility
            


    #handles data preprocessing 
    def build(self):
        print(self)
        stock = yf.Ticker(self.upper())
        #closest to 45 days away, initialized as arbitrary days far away
        cl45 = "1999-01-01"
        for i in stock.options:
            if abs(45-(date(int(i[:4]),int(i[5:7]),int(i[8:10]))-date.today()).days) < abs(45-(date(int(cl45[:4]),int(cl45[5:7]),int(cl45[8:10]))-date.today()).days):
                cl45 = i
        #days till expiry
        dte = (date(int(cl45[:4]),int(cl45[5:7]),int(cl45[8:10]))-date.today()).days
        yesterday = str((date.today() - timedelta(days=1)).year) + "-" + str((date.today() - timedelta(days=1)).month) + "-" + str((date.today() - timedelta(days=1)).day)
        option_chain = stock.option_chain(date = cl45).puts
        currentPrice = stock.info['regularMarketPrice']
        strikes = np.array([x for x in option_chain.loc[:,"strike"]])
        percentileStrikes = np.array([i/currentPrice for i in strikes])
        rawHistoricalData = yf.download(tickers = self, start = "2010-01-01", end = yesterday)
        #Exception Handling for pulling of extra data for companies that have IPO'd after 2010-01-01
        if '-'.join(i.zfill(2) for i in (str(rawHistoricalData.index[0].to_pydatetime().date().year) + "-" + str(rawHistoricalData.index[0].to_pydatetime().date().month) + "-" + str(rawHistoricalData.index[0].to_pydatetime().date().day)).split('-')) == "2010-01-04":    
            extraHistoricalData = yf.download(tickers = self, start = "2009-12-01", end = "2010-01-01")
        elif len(rawHistoricalData) > 750:
            extraStartDate = '-'.join(i.zfill(2) for i in (str(rawHistoricalData.index[0].to_pydatetime().date().year) + "-" + str(rawHistoricalData.index[0].to_pydatetime().date().month) + "-" + str(rawHistoricalData.index[0].to_pydatetime().date().day)).split('-'))
            rawStartDate = extraStartDate[0:5] + str(int(extraStartDate[5:7])+1).zfill(2) + extraStartDate[7:10]
            rawHistoricalData = yf.download(tickers = self, start = rawStartDate, end = yesterday)
            extraHistoricalData = yf.download(tickers = self, start = extraStartDate, end = rawStartDate)
        else:
            print("NOT ENOUGH HISTORICAL PRICE DATA")
            return "NOT ENOUGH HISTORICAL PRICE DATA"
        divider = math.floor(len(rawHistoricalData)*0.7)
        #70% of the data is used for training
        training = rawHistoricalData.iloc[0:divider]
        trainingVolatility = data.volatility(training, extraHistoricalData)
        trainingDailyChange = training["Close"] - training["Open"]
        training = training.drop(["High", "Low", "Adj Close"], axis = 1)
        training["Daily Change"] = trainingDailyChange
        training["Volatility"] = trainingVolatility
        #30% of the data is used for testing
        testing = rawHistoricalData[divider:len(rawHistoricalData)]
        testingVolatility = data.volatility(testing,training) #training is only used to calculate volatility for the first time step in testing
        testingDailyChange = testing["Close"] - testing["Open"]
        testing = testing.drop(["High", "Low", "Adj Close"], axis = 1)
        testing["Daily Change"] = testingDailyChange
        testing["Volatility"] = testingVolatility
        print(training)
        return(training,testing)
    
data.build("MSFT")

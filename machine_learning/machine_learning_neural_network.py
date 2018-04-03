import requests
import datetime
from datetime import date
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import math

model_path = 'C:/Users/diginamic/Desktop/Travis-test/machine_learning/model'

# Retrieve data from CoinDesk API
def get_historique_data(currency, start_date, end_date):	
	url_cours_bitcoin = 'https://api.coindesk.com/v1/bpi/historical/close.json?currency='+currency+'&start='+start_date+'&end='+end_date
	res = requests.get(url_cours_bitcoin)
	if res.ok:
		return res
	else:
		return None

def create_dataset(dataset):
  dataX, dataY = [], []
  for i in range(len(dataset)-1):
    dataX.append(dataset[i])
    dataY.append(dataset[i + 1])
  return np.asarray(dataX), np.asarray(dataY)

def save_model(model, model_path):
	model.save(model_path)
  
def main():
	data_historique = get_historique_data('EUR', '2011-01-01', '2018-04-02')
	data = data_historique.json()
	dataset_raw = []
	date = []
	rate = []
	for i in data["bpi"]:
		date_event = datetime.datetime.strptime(i, "%Y-%m-%d").date()
		value_event = data["bpi"][i]
		date.append(date_event)
		rate.append(value_event)
		dataset_raw.append(value_event)
		
	# plt.plot(date, rate)
	# plt.show()
	
	dataset = np.asarray(dataset_raw).reshape(-1,1)
	scaler = MinMaxScaler(feature_range=(0,1))
	dataset = scaler.fit_transform(dataset)

	# dataX : value at n_i dataY : value at n_i+1
	dataX, dataY = create_dataset(dataset)
	# Split data into training data and testing data 80/20
	trainX, testX, trainY, testY = train_test_split(dataX, dataY, test_size=0.20, shuffle=False)
	# Reshape to fit input requirement for LSTM neural network
	trainX = np.reshape(trainX, (trainX.shape[0], 1, 1))
	testX = np.reshape(testX, (testX.shape[0], 1, 1))
	
	# Create LSTM Network
	'''model = Sequential()
	model.add(LSTM(4, input_shape=(1,1)))
	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')
	model.fit(trainX, trainY, epochs=5, batch_size=1, verbose=2)'''
	
	# Save model
	# save_model(model, model_path)
	# Load model
	model = load_model(model_path)
	
	# Make predictions
	trainPredict = model.predict(trainX)
	testPredict = model.predict(testX)
	
	futurePredict = model.predict(np.asarray([[testPredict[-1]]]))
	futurePredict = scaler.inverse_transform(futurePredict)
	
	# Invert predictions to get BTC value back 
	trainPredict = scaler.inverse_transform(trainPredict)
	trainY = scaler.inverse_transform(trainY)
	testPredict = scaler.inverse_transform(testPredict)
	testY = scaler.inverse_transform(testY)
	
	print ('Value for last 5 days')
	print (dataset_raw[-5:])
	print ('predicted Value for last 5 days')
	print (testPredict[-5:])
	print ('Bitcoin value for tomorrow : ', futurePredict)
	
	# Calculate root mean squared error
	trainScore = math.sqrt(mean_squared_error(trainY[:,0], trainPredict[:,0]))
	print('Train Score: %.2f RMSE' % (trainScore))
	testScore = math.sqrt(mean_squared_error(testY[:,0], testPredict[:,0]))
	print('Test Score: %.2f RMSE' % (testScore))
	
	'''# shift train predictions for plotting
	trainPredictPlot = np.empty_like(dataset)
	trainPredictPlot[:, :] = np.nan
	trainPredictPlot[1:len(trainPredict)+1, :] = trainPredict
	# shift test predictions for plotting
	testPredictPlot = np.empty_like(dataset)
	testPredictPlot[:, :] = np.nan
	testPredictPlot[len(trainPredict):len(dataset)-1, :] = testPredict
	
	# plot baseline and predictions
	plt.plot(scaler.inverse_transform(dataset))
	plt.plot(trainPredictPlot)
	plt.plot(testPredictPlot)
	plt.show()'''
	
if __name__ == '__main__':
	main()
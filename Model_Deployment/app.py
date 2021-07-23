
from flask import Flask, render_template, request
import pickle
import numpy as np
filename = 'msft_model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Month = int(request.form['Month'])
        Day = int(request.form['Day'])
        Open = float(request.form['Open'])
        High = float(request.form['High'])
        Low = float(request.form['Low'])
        Close = float(request.form['Close'])
    
        
        data = np.array([[Year, Month, Day, Open, High, Low, Close]])
        my_prediction = classifier.predict(data)
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)
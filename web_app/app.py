from flask import Flask, render_template, request
import numpy as np
import pickle as pkl  

app = Flask(__name__)

# Load the pre-trained model
model = pkl.load(open("./model/medical_insurance.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input data from the form
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = int(request.form['smoker'])
        region = int(request.form['region'])
        
        # Create the input array
        df_input = np.array([age, sex, bmi, children, smoker, region]).reshape(1, -1)
        
        # Make the prediction
        prediction = model.predict(df_input)[0]
        
        return render_template('index.html', prediction=f"Medical Insurance Cost: ${prediction:.2f}")
    
if __name__ == '__main__':
    app.run(debug=True)

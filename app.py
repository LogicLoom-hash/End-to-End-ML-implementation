import joblib
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = joblib.load(open('model.pkl', 'rb'))
scaler = joblib.load(open('scaler.pkl', 'rb'))

# Define a mapping from prediction to species name
species_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input values from the form
        data = [float(x) for x in request.form.values()]
        
        # Reshape and scale the data
        final_input = scaler.transform(np.array(data).reshape(1, -1))
        print("Scaled input:", final_input)
        
        # Use the model to predict the species (returns string like 'Iris-setosa')
        output = model.predict(final_input)[0]
        print("Model prediction:", output)
        
        # Return the species name directly from the prediction
        return render_template("home.html", prediction_text=f"The prediction of iris flower species is: {output}")
    
    except Exception as e:
        print("Error:", str(e))  # Debugging the actual error message
        return render_template("home.html", prediction_text=f"Error occurred: {str(e)}")



if __name__ == "__main__":
    app.run(debug=True)

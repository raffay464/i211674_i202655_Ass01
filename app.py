import pickle
from flask import Flask, request, jsonify

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

app = Flask(__name__)

# Load the pre-trained model and scaler
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Convert the input data into a numpy array
    input_data = [[
        data['total_acidity'],  
        data['sugar_content'],  
        data['mineral_content'],  
        data['acidity_of_base'],  
        data['element_X'],  
        data['phenol_compound'],  
        data['compound_Y'],  
        data['phenolic_derivative'],  
        data['color_agent'],  
        data['intensity_modifier'],   
        data['hue_value'],  
        data['dilution_ratio'],  
        data['protein_level'] 
    ]]


    # Scale the input data using the loaded scaler
    input_data_scaled = scaler.transform(input_data)

    # Make predictions using the loaded model
    prediction = model.predict(input_data_scaled)

    # Convert the prediction into a human-readable label
    if prediction == 0:
        label = 'Class 0'
    elif prediction == 1:
        label = 'Class 1'
    else:
        label = 'Class 2'

    # Prepare the response
    response = {
        'prediction': label
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
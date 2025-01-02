from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load('xgboost_best_model.pkl')
except FileNotFoundError:
    raise FileNotFoundError("Model file 'xgboost_best_model.pkl' not found. Please ensure the file exists.")
except Exception as e:
    raise Exception(f"An error occurred while loading the model: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        df = pd.DataFrame([data])
        prediction = model.predict(df)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
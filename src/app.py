from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('models/titanic_rf_model.pkl')

@app.route('/')
def home():
    return "Titanic Survival Prediction API is running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)

        expected_keys = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Title', 'FamilySize', 'isAlone']
        for key in expected_keys:
            if key not in data:
                return jsonify({'error': f'Missing feature: {key}'}), 400

        input_df = pd.DataFrame([data])

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        return jsonify({
            'Survived': int(prediction),
            'Survival Probability': float(probability)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

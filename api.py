from flask import Flask, request
from model import predict_price

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def ModelPredict():
    Year = request.args.get('Year')
    Mileage = request.args.get('Mileage')
    State = request.args.get('State')
    Make = request.args.get('Make')
    Model = request.args.get('Model')
    return {
        "1. Year": Year,
        "2. Mileage": Mileage,
        "3. State": State,
        "4. Make": Make,
        "5. Model": Model,
        "Price predicted": predict_price(Year,Mileage,State,Make,Model)      
        }, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)

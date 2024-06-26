from flask import Flask, jsonify, request
app = Flask(__name__)
import util
@app.route('/get_locations', methods=['GET'])
def get_locations():
    response=jsonify({
        'locations':util.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    print(util.get_locations() ,"response!!!!")
    return response


@app.route('/predict_home_price',methods=['GET','POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response=jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    # util.load_saved_artifacts()
    app.run(debug=True,host='0.0.0.0', port=8000)

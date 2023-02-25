from flask import Flask , render_template , request , jsonify
import prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# api listening to POST requests and predicting sentiments
@app.route('/predict' , methods = ['POST'])
def predict():

    response = ""
    review = request.json.get('customer_review')
    if not review:
        response = {'status' : 'error',
                    'message' : 'Empty Review'}
    
    else:

        # calling the predict method from prediction.py module
        sentiment , path = prediction.predict(review)
        response = {'status' : 'success',
                    'message' : 'Got it',
                    'sentiment' : sentiment,
                    'path' : path}

    return jsonify(response)


# Creating an API to save the review, user clicks on the Save button
@app.route('/predict_emotion' , methods = ['POST'])
def save():

    # extracting date , product name , review , sentiment associated from the JSOn data
    date = request.json.get('')
    product = request.json.get('')
    review = request.json.get('')
    sentiment = request.json.get('')

    # creating a final variable seperated by commas
    data_entry = date + "," + product + "," + review + "," + sentiment
@app.route("/predict-emotion", methods=["POST"])
def predict_emotion():
    input_text = request.json.get("text")
    if not input_text:
        return jsonify({
            "status": "error",
            "message": "Please enter some text to predict emotion!"
        }), 400
    else:
        predicted_emotion, predicted_emotion_img_url = predict(input_text)   
    return jsonify({'status' : 'success' , 
                    'message' : 'Data Logged'})


if __name__  ==  "__main__":
    app.run(debug = True)
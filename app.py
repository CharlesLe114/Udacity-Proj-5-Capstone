from flask import Flask


app = Flask(__name__)
@app.route("/")
def home():
    html = f"<h3>I'm Le Bao Toan, This is capstone project for Udacity AWS DevOps program</h3>"
    return html.format(format)


if __name__ == "__main__":
    # load pretrained model as clf
    # clf = joblib.load("./model_data/boston_housing_prediction.joblib")
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80

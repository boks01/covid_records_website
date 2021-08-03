from flask import Flask, render_template
import requests
app = Flask(__name__)
URL = "https://coronavirus-19-api.herokuapp.com/countries"
response = requests.get(URL)
result = response.json()
@app.route('/')
def home():
    return render_template("index.html", result=result)

@app.route('/<country>')
def covid_records(country):
    print(country)
    return render_template("post.html", result=result, country=country,)

@app.route('/back')
def back():
    print()
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', clima=data.json_data)

@app.route("/setting")
def setting():
    return render_template('setting.html')

if __name__ == "__main__":
    app.run(debug=True)
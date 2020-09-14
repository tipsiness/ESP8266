from flask import Flask, redirect, url_for, request, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post():
    dev_id = request.form.get('dev_id')
    value1 = request.form.get('temp')
    value2 = request.form.get('humi')
    print "Device ID: " + dev_id + ", Temperature: " + value1 + ", Humidity: " + value2

    return render_template('resp.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999, debug=True)

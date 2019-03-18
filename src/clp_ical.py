#!/usr/bin/env python

from flask import Flask, Response, request
import requests

EVENTS_URI = 'https://www.carnegielibrary.org/events/'

app = Flask(__name__)

@app.route("/events", methods=['GET'])
def events():
    params = {
        'ical': '1',
    }
    for k, v in request.args.items():
        params['tribe-bar-' + k] = v

    response = requests.get(url=EVENTS_URI, params=params)
    response.raise_for_status()
    return Response(response.content.strip(), mimetype="text/calendar")

if __name__ == "__main__":
    app.run()

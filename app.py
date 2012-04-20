import os, time

from datetime import datetime, timedelta
from pytz import timezone
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    # Device gets passed through as mi_type
    device = request.args.get('mi_type')

    # Location information
    city      = request.args.get('mi_city')
    region    = request.args.get('mi_reg') # region (state)
    country   = request.args.get('mi_cc')  # country code, e.g. US
    latitude  = float(request.args.get('mi_lat') or 0) # latitude
    longitude = float(request.args.get('mi_lon') or 0) # longitude

    # You can pass arbitrary parameters through via the embed code image src
    name   = request.args.get('name')

    # full user-agent string, uri-encoded
    agent   = request.args.get('mi_agent')
    # timezone
    tz      = request.args.get('mi_tz')

    location = city
    if country == "US":
        location = location + ", " + region


    if tz and tz != "":
        zone = timezone(tz)
        date = zone.fromutc(datetime.now())
    else:
        date = datetime.now()


    time_string = date.strftime("%A, %B %d, %Y at %I:%M:%S %p")

    return render_template("index.html", name=name, location=location, device=device,
                           latitude=latitude, longitude=longitude, time_string=time_string)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

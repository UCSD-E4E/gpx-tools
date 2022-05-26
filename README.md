# GPX Tools
Installation: 
```
python3 -m venv .venv
.venv\Scripts\Activate
python -m pip install .
```
## GPX Cut
Usage: 
```
gpxcut [-h] [--track TRACK] [--start START] [--stop STOP] [--output OUTPUT] gpx

positional arguments:
  gpx

options:
  -h, --help            show this help message and exit
  --track TRACK, -t TRACK
  --start START         ISO Datetime string of start time
  --stop STOP           ISO Datetime string of stop time
  --output OUTPUT, -o OUTPUT
```

Example:
```
gpxcut --start 2022-05-26T14:00-04:00 --stop 2022-05-26T16:00-04:00 --output output.gpx input.gpx
```
The above invocation takes `input.gpx` and saves the section from 2 PM EDT to 4 PM EDT on 5/26 to `output.gpx`
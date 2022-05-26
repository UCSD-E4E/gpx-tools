import argparse
import datetime as dt

import gpxpy
import gpxpy.gpx


def main():
    parser = argparse.ArgumentParser(
        prog="gpxcut",
    )
    parser.add_argument('gpx')
    parser.add_argument('--track', '-t', default=None)
    parser.add_argument('--start', default=None, help="ISO Datetime string of start time")
    parser.add_argument('--stop', default=None, help="ISO Datetime string of stop time")
    parser.add_argument("--output", "-o")

    args = parser.parse_args()
    
    with open(args.gpx, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    if args.track == None:
        track = gpx.tracks[0]
    else:
        for t in gpx.tracks:
            if args.track == t.name:
                track = t
                break
    
    if args.start:
        start_time = dt.datetime.fromisoformat(args.start)
    else:
        start_time = dt.datetime(0, 0, 0, 0, 0, 0)
    
    if args.stop:
        stop_time = dt.datetime.fromisoformat(args.stop)
    else:
        stop_time = dt.datetime.now()

    segments_to_remove = []
    for segment in track.segments:
        points_to_remove = []
        for point in segment.points:
            if point.time < start_time or point.time > stop_time:
                points_to_remove.append(point)
        for point in points_to_remove:
            segment.points.remove(point)
        if len(segment.points) == 0:
            segments_to_remove.append(segment)
    
    for segment in segments_to_remove:
        track.segments.remove(segment)
    
    with open(args.output, 'w') as outfile:
        outfile.write(gpx.to_xml())
    

    



if __name__ == "__main__":
    main()

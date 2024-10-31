from flask import Flask, jsonify, request, abort
from flask_restful import Resource, Api, reqparse, inputs
import sys
from datetime import datetime

app = Flask(__name__)
api = Api(app)

events = []
event_id_counter = 1

parser = reqparse.RequestParser()
parser.add_argument(
    'event',
    type=str,
    help="The event name is required!",
    required=True
)
parser.add_argument(
    'date',
    type=inputs.date,
    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
    required=True
)

class EventResource(Resource):
    def post(self):
        global event_id_counter
        args = parser.parse_args()
        event = {
            "id": event_id_counter,
            "event": args['event'],
            "date": args['date'].strftime('%Y-%m-%d')
        }
        events.append(event)
        event_id_counter += 1
        return {
            "message": "The event has been added!",
            "event": args['event'],
            "date": args['date'].strftime('%Y-%m-%d')
        }

class EventsResource(Resource):
    def get(self):
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        if start_time and end_time:
            start_time = datetime.strptime(start_time, '%Y-%m-%d')
            end_time = datetime.strptime(end_time, '%Y-%m-%d')
            filtered_events = [event for event in events if start_time <= datetime.strptime(event['date'], '%Y-%m-%d') <= end_time]
            return jsonify(filtered_events)
        return jsonify(events)

class TodayEventsResource(Resource):
    def get(self):
        today = datetime.now().strftime('%Y-%m-%d')
        today_events = [event for event in events if event['date'] == today]
        return jsonify(today_events)

class EventByIDResource(Resource):
    def get(self, event_id):
        event = next((event for event in events if event['id'] == event_id), None)
        if event is None:
            abort(404, "The event doesn't exist!")
        return jsonify(event)

    def delete(self, event_id):
        global events
        event = next((event for event in events if event['id'] == event_id), None)
        if event is None:
            abort(404, "The event doesn't exist!")
        events = [event for event in events if event['id'] != event_id]
        return {"message": "The event has been deleted!"}

api.add_resource(EventResource, '/event')
api.add_resource(EventsResource, '/event')
api.add_resource(TodayEventsResource, '/event/today')
api.add_resource(EventByIDResource, '/event/<int:event_id>')

# Do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
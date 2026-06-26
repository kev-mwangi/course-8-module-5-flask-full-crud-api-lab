from flask import Flask, jsonify, request

app = Flask(__name__)


# Simulated Database
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }


events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


# Home Route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Event API"
    })


# GET All Events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])


# POST Create Event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    # Validate input
    if not data or "title" not in data:
        return jsonify({
            "error": "Title is required"
        }), 400

    # Generate a new ID
    new_id = max([event.id for event in events], default=0) + 1

    # Create and store the event
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    # Return the new event with status 201
    return jsonify(new_event.to_dict()), 201


if __name__ == "__main__":
    app.run(debug=True)




    from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated Database
events = [
    {"id": 1, "title": "Tech Meetup"},
    {"id": 2, "title": "Python Workshop"}
]


# Home Route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Event API"})


# GET All Events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)


# POST Create Event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    # Validate input
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_event = {
        "id": len(events) + 1,
        "title": data["title"]
    }

    events.append(new_event)

    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)
#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'])
def get_status():
    """
    Retrieves the status of the API.

    Returns:
        JSON response with the status of the API.
    Example:
        {
            "status": "OK"
        }
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def get_stats():
    """
    Retrieves the number of each object by type from the storage.

    Utilizes the storage.count() method to get the count of each object type.

    Returns:
        JSON response containing the counts of each object type.
    Example:
        {
            "Amenity": 10,
            "City": 5,
            "Place": 20,
            "Review": 30,
            "State": 7,
            "User": 15
        }
    """
    stats = {
        "Amenity": storage.count("Amenity"),
        "City": storage.count("City"),
        "Place": storage.count("Place"),
        "Review": storage.count("Review"),
        "State": storage.count("State"),
        "User": storage.count("User")
    }
    return jsonify(stats)

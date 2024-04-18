#!/usr/bin/python
"""
Importing necessary libraries and modules
and creating the Flask web application
"""
from flask import Flask
from models import storage
import os
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(exception):
    """Teardown function to close the storage
    after the application context is destroyed"""
    storage.close()


if __name__ == "__main__":
    port = int(os.environ.get("HBNB_API_PORT", 5000))
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    app.run(host=host, port=port, threaded=True)

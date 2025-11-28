import json
import os
from datetime import datetime

class DatabaseModule:
    """
    Database Module (Prototype Version)

    Stores triage interactions in a local JSON file,
    simulating the persistent storage described in the SRS.

    Each entry stored:
        - timestamp
        - symptom description
        - urgency level
    """

    FILE = "database.json"

    def save(self, entry: dict):
        """Save one interaction into database.json"""
        data = []

        if os.path.exists(self.FILE):
            with open(self.FILE, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

        entry_with_timestamp = {
            "timestamp": datetime.now().isoformat(),
            **entry
        }

        data.append(entry_with_timestamp)

        with open(self.FILE, "w") as f:
            json.dump(data, f, indent=4)

    def get_all(self):
        """Retrieve all stored interactions"""
        if not os.path.exists(self.FILE):
            return []
        with open(self.FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("data/decision_history.json")

def save_decision_log(log_data):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        **log_data
    }

    if LOG_FILE.exists():
        with open(LOG_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(history, f, indent=2)


def get_decision_history():
    if not LOG_FILE.exists():
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)

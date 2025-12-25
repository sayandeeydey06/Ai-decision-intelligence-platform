from datetime import datetime

def perform_action(decision_result):
    action_log = {
        "timestamp": datetime.now().isoformat(),
        "decision": decision_result["decision"],
        "action_taken": ""
    }

    if decision_result["decision"] == "Increase inventory":
        action_log["action_taken"] = "Alert sent to inventory manager"

    elif decision_result["decision"] == "Maintain current inventory":
        action_log["action_taken"] = "No action required"

    else:
        action_log["action_taken"] = "Inventory reduction notice sent"

    return action_log

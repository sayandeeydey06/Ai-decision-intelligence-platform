def make_decision(predicted_sales):
    if predicted_sales >= 1600:
        return {
            "decision": "Increase inventory",
            "reason": "High demand expected",
            "confidence": "High"
        }

    elif predicted_sales >= 1200:
        return {
            "decision": "Maintain current inventory",
            "reason": "Stable demand expected",
            "confidence": "Medium"
        }

    else:
        return {
            "decision": "Reduce inventory",
            "reason": "Low demand expected",
            "confidence": "Low"
        }

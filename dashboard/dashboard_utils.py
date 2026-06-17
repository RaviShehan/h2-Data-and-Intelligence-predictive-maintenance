import json


def normalize_predictions(prediction_response):
    if isinstance(prediction_response, dict):
        prediction_items = prediction_response.get("predictions", [])
    elif isinstance(prediction_response, list):
        prediction_items = prediction_response
    else:
        prediction_items = []

    cleaned_predictions = []

    for item in prediction_items:
        if isinstance(item, dict):
            cleaned_predictions.append(item)
        elif isinstance(item, str):
            try:
                cleaned_predictions.append(json.loads(item))
            except json.JSONDecodeError:
                pass

    return cleaned_predictions
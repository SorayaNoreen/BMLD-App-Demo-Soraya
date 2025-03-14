from utils import helpers

def calculate_carbohydrates(intake, weight, timezone='Europe/Zurich'):
    """
    Calculate carbohydrate intake per kilogram of body weight and return a dictionary with inputs, 
    calculated intake per kg, category, and timestamp.

    Args:
        intake (float): Total carbohydrate intake in grams.
        weight (float): Body weight in kilograms.

    Returns:
        dict: A dictionary containing the inputs, calculated intake per kg, category, and timestamp.
    """
    if intake <= 0 or weight <= 0:
        raise ValueError("Intake and weight must be positive values.")

    intake_per_kg = intake / weight

    if intake_per_kg < 2:
        category = 'Niedrig'
    elif intake_per_kg < 5:
        category = 'Moderat'
    else:
        category = 'Hoch'

    result_dict = {
        "timestamp": helpers.ch_now(),
        "intake": intake,
        "weight": weight,
        "intake_per_kg": round(intake_per_kg, 2),
        "category": category,
    }

    return result_dict
def generate_example(subject, grade, topic, formula_name):
    # Simple fallback example logic
    if "Speed" in formula_name:
        return "If a car travels 100 km in 2 hours, its speed is 50 km/h."
    if "Area" in formula_name:
        return "A rectangle with length 5m and width 3m has area 15 m²."
    if "Slope" in formula_name:
        return "If (x₁, y₁) = (1, 2) and (x₂, y₂) = (3, 6), slope = (6−2)/(3−1) = 2."
    return f"Here's a simple example of '{formula_name}' for Grade {grade} {subject} ({topic})."

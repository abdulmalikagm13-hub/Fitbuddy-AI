from app.gemini_flash_generator import generate_nutrition_tip_with_flash

def get_nutrition_advice(goal: str) -> str:
    return generate_nutrition_tip_with_flash(goal)
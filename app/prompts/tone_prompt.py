def get_tone_prompt(text):
    return f"""
    Classify the tone of this message:
    "{text}"
    
    Options: casual, rude, unclear, professional
    """

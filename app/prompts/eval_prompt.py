def get_eval_prompt(text):
    return f"""
    Rate this text from 1–10 for professionalism and clarity:
    
    "{text}"
    
    Only return a number.
    """

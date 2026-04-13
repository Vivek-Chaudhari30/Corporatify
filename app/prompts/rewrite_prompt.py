def get_rewrite_prompt(text, tone):
    return f"""
    Convert this into professional corporate language.

    Tone: {tone}
    Text: {text}

    Make it polite, clear, and professional.
    """

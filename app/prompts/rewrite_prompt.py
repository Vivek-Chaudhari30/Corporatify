def get_rewrite_prompt(text, tone, platform, corporatify_level):
    rules = []
    
    if platform == "Email":
        rules.append("- Format it as a standard professional email with a subject line, greeting, and sign-off.")
    elif platform in ["Slack", "WhatsApp"]:
        rules.append("- Keep it concise and direct suitable for a chat message without long formalities.")
        
    if corporatify_level < 0.6:
        rules.append("- Keep the tone friendly, polite, and approachable (e.g. casual yet professional).")
    elif corporatify_level >= 0.8:
        rules.append("- Make the tone highly formal, rigid, and strictly bureaucratic (ultra-corporate).")
    else:
        rules.append("- Make the tone standard corporate professional.")

    rules_text = "\n".join(rules)

    return f"""
    Convert this into professional corporate language.

    Original Tone: {tone}
    Target Platform: {platform}
    Corporatify Level: {corporatify_level}/1.0
    
    Additional Rules:
    {rules_text}

    Text: "{text}"

    Make it clear, professional, and obey the rules above strictly.
    """

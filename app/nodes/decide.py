def decide(state):
    if state["score"] < 8 and state["iterations"] < 3:
        return "rewrite"
    return "end"

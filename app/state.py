from typing import TypedDict

class State(TypedDict):
    input_text: str
    tone: str
    rewritten_text: str
    score: int
    iterations: int

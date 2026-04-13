from typing import TypedDict

class State(TypedDict):
    input_text: str
    platform: str
    corporatify_level: float
    tone: str
    rewritten_text: str
    score: int
    iterations: int

from app.llm import get_llm
from app.prompts.tone_prompt import get_tone_prompt

llm = get_llm()

def detect_tone(state):
    response = llm.invoke(get_tone_prompt(state["input_text"]))
    return {"tone": response.content.strip()}

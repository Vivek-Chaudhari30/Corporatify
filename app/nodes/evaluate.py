from app.llm import get_llm
from app.prompts.eval_prompt import get_eval_prompt

llm = get_llm()

def evaluate(state):
    response = llm.invoke(get_eval_prompt(state["rewritten_text"]))
    
    try:
        score = int(response.content.strip()[0])
    except:
        score = 6

    return {"score": score}

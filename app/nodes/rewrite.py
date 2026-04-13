from app.llm import get_llm
from app.prompts.rewrite_prompt import get_rewrite_prompt

llm = get_llm()

def rewrite(state):
    platform = state.get("platform", "Email")
    corp_level = state.get("corporatify_level", 0.5)
    
    response = llm.invoke(
        get_rewrite_prompt(state["input_text"], state["tone"], platform, corp_level)
    )
    
    return {
        "rewritten_text": response.content,
        "iterations": state.get("iterations", 0) + 1
    }

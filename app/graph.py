from langgraph.graph import StateGraph, END
from app.state import State
from app.nodes.detect import detect_tone
from app.nodes.rewrite import rewrite
from app.nodes.evaluate import evaluate
from app.nodes.decide import decide

def build_graph():
    builder = StateGraph(State)

    builder.add_node("detect", detect_tone)
    builder.add_node("rewrite", rewrite)
    builder.add_node("evaluate", evaluate)

    builder.set_entry_point("detect")

    builder.add_edge("detect", "rewrite")
    builder.add_edge("rewrite", "evaluate")

    builder.add_conditional_edges("evaluate", decide, {
        "rewrite": "rewrite",
        "end": END
    })

    return builder.compile()

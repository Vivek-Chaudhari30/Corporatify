from app.graph import build_graph

graph = build_graph()

result = graph.invoke({
    "input_text": "send me the report asap"
})

print("Original: send me the report asap")
print("Professional:", result["rewritten_text"])

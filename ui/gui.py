import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.graph import build_graph

graph = build_graph()

st.title("👔 Corporatify: Corporate Tone AI")

text = st.text_area("Enter your message:")

if st.button("Convert"):
    with st.spinner("Corporatifying..."):
        result = graph.invoke({"input_text": text})
        st.subheader("Professional Version:")
        st.write(result["rewritten_text"])
        st.caption(f"Tone Detected: {result.get('tone')} | Refinement Iterations: {result.get('iterations')} | Score: {result.get('score')}/10")

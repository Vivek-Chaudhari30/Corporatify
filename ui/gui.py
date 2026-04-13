import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.graph import build_graph

graph = build_graph()

st.title("👔 Corporatify: Corporate Tone AI")
st.markdown("Convert casual or rude messages into perfectly toned professional communication.")

col1, col2 = st.columns(2)
with col1:
    platform = st.selectbox("📺 Target Platform:", ["Email", "Slack", "WhatsApp"])
with col2:
    corp_level = st.slider("🎚️ Corporatify Level:", min_value=0.0, max_value=1.0, value=0.3, step=0.1, help="0.0 = Casual, 0.3-0.5 = Friendly/Polite, 1.0 = Highly Formal/Corporate")

st.markdown("---")
text = st.text_area("💬 Enter your informal message:", height=150)

if st.button("Convert ✨", type="primary", use_container_width=True):
    with st.spinner("👔 Corporatifying..."):
        result = graph.invoke({
            "input_text": text,
            "platform": platform,
            "corporatify_level": corp_level
        })
        st.subheader("Professional Version:")
        st.write(result["rewritten_text"])
        st.caption(f"Tone Detected: {result.get('tone')} | Refinement Iterations: {result.get('iterations')} | Score: {result.get('score')}/10")

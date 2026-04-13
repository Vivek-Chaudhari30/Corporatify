# Corporatify: Corporate Tone AI

Corporatify is an AI system that converts informal text into corporate communication strictly using iterative refinement and evaluation. 
It uses LangGraph for agentic workflows powered by gpt-4o-mini and Streamlit for the frontend.

## Setup
1. Use `pip install -r requirements.txt`
2. Update the `.env` file with your `OPENAI_API_KEY`

## Running Locally
Run the Streamlit app:
```bash
streamlit run ui/app.py
```

Run evaluating checks without UI:
```bash
python main.py
```

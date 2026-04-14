# Corporatify: Corporate Tone AI

Corporatify is an AI system that converts informal text into corporate communication strictly using iterative refinement and evaluation. 
It uses LangGraph for agentic workflows powered by gpt-4o-mini and Streamlit for the frontend.

## Prerequisites
- Python 3.9+
- An OpenAI API Key

## Setup Instructions

1. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```
   *(On Windows, use `.\venv\Scripts\activate`)*

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Update the `.env` file in the project directory with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Running Locally

### 1. Streamlit Web Interface (Recommended)
To run the interactive web application, ensure you're in your virtual environment and run:
```bash
streamlit run ui/gui.py
```

### 2. CLI Mode
To run evaluating checks in a headless mode without the UI:
```bash
python main.py
```

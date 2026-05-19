# LangChain + LangServe Chatbot

A production-ready LLM chatbot built with **LangChain** and served as a REST API using **LangServe + FastAPI**. Includes an evaluation pipeline to measure response quality.

---

## What makes this different

Most LLM demos run only in a notebook. This project goes further — the chatbot is:
- Built with structured LangChain prompt pipelines
- **Deployed as a REST API** using LangServe & FastAPI (ready for frontend integration)
- **Evaluated** using test data with results logged to CSV

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| LangChain | Prompt management & LLM pipeline |
| LangServe | Serve LangChain chains as REST APIs |
| FastAPI | Web framework for API deployment |
| Python | Core language |

---

## Project Structure

```
Langchain-Langserve-Chatbot/
├── chatbot.py          # LangChain chatbot logic & prompt pipeline
├── serve.py            # LangServe + FastAPI server
├── evaluate.py         # Evaluation pipeline for response quality
├── test_data.json      # Test questions for evaluation
├── results.csv         # Evaluation results
├── requirements.txt    # Dependencies
└── .gitignore
```

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Nancyparmar/Langchain-Langserve-Chatbot-.git
cd Langchain-Langserve-Chatbot-
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your API key
```bash
export OPENAI_API_KEY="your-api-key"
```

### 4. Run the chatbot
```bash
python chatbot.py
```

### 5. Start the API server
```bash
python serve.py
```
API will be available at `http://localhost:8000`

---

## API Usage

Once the server is running, send POST requests:

```bash
curl -X POST http://localhost:8000/chat/invoke \
  -H "Content-Type: application/json" \
  -d '{"input": {"question": "What is machine learning?"}}'
```

LangServe also provides an auto-generated playground UI at `http://localhost:8000/chat/playground`

---

## Evaluation

Run the evaluation pipeline to test response quality:

```bash
python evaluate.py
```

Results are saved to `results.csv` with question, expected answer, and model response.

---

## Architecture

```
User Request
     ↓
FastAPI (serve.py)
     ↓
LangServe Router
     ↓
LangChain Pipeline (chatbot.py)
     ↓
LLM (OpenAI / any model)
     ↓
JSON Response
```

---

## Future Improvements

- [ ] Add memory for multi-turn conversations
- [ ] Integrate RAG for domain-specific knowledge
- [ ] Deploy to cloud (Railway / Render / AWS)
- [ ] Add authentication to the API

---

## Author

**Nancy Parmar** — [GitHub](https://github.com/Nancyparmar) · [LinkedIn](https://www.linkedin.com/in/nancy-parmar/)

> Built during Data Science Internship at C9 Lab, Indore

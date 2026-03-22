# AI STEM Tutor

A modular AI tutor for STEM education, integrating Agentic AI, RAG, and advanced math reasoning. Built for the IBM Hackathon.

## Features
- Step-by-step math problem solving
- RAG (Retrieval-Augmented Generation) for grounded explanations
- Agentic orchestration for dynamic task routing
- Modular backend (FastAPI)

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the backend:
   ```bash
   uvicorn ai_stem_tutor.main:app --reload
   ```

## Structure
- `routers/`: API endpoints
- `services/`: Core logic (math, RAG, LLM)
- `models/`: Pydantic schemas
- `utils/`: Config and helpers

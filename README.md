# KeaBuilder ML Assessment

## 1. Problem
Find similar user inputs using ML

## 2. Approach
- TF-IDF + Cosine Similarity
- Lightweight, no heavy training

## 3. How to Run

### Step 1: Install dependencies
pip install -r requirements.txt

### Step 2: Run API
uvicorn app:app --reload

### Step 3: Test
http://127.0.0.1:8000/match?query=pricing

## 4. Sample Output
Query: What is the pricing?
Best Match: Looking for pricing details

## 5. Design Decisions
- Chose TF-IDF for simplicity
- Avoided heavy models for speed

## 6. Future Improvements
- Use embeddings (BERT/OpenAI)
- Add caching

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def generate_answer(question: str, contexts: list[str]) -> str:
    context_text = " ".join(contexts)

    prompt = (
        "Answer the question based only on the context below.\n\n"
        f"Context:\n{context_text}\n\n"
        f"Question:\n{question}\n\nAnswer:"
    )

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=256)

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

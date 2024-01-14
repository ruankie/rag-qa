from fastapi import FastAPI, File, Form
# from langchain import LangChain

app = FastAPI()
# lc = LangChain()


@app.get("/")
def root():
    return {"Status": "Server running."}

@app.get("/test")
def root():
    return {"Status": "Server running."}


# @app.post("/answer")
# def answer(pdf: bytes = File(...), question: str = Form(...)):
#     # TODO: implement the logic to answer the question based on the PDF document
#     # Hint: use lc.rag to perform the retrieval-augmented generation
#     answer = "This is a dummy answer"
#     return {"answer": answer}

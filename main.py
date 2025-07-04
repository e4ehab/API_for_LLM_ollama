from fastapi import FastAPI
import ollama
import uvicorn

app=FastAPI()

#create an end point we can access
@app.post("/generate")
def generate(prompt: str):
    try:
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )    #we want to chat with ollama,and specify the messages we want to pass

        return {"response": response["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}


    #return the response and pthon dictionary that has a response , and the response will be the [message]+[content]
 
 
 #to run the api --> uvicorn main:app --reload. (make sure to activate the venv (source ./.venv/bin/activate))
 # if we run the project normally uv run main.py (it will run)
 # but we need to run the api so activate the venv first then run --> uvicorn main:app --reload
 
 #it will tell us the port which the api runs on --> http://127.0.0.1:8000
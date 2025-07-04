from fastapi import FastAPI,Depends,HTTPException,Header
import ollama
import os
from dotenv import load_dotenv

app=FastAPI()

load_dotenv() # Loads environment variables from a .env file 
API_KEYS_CREDITS = {os.getenv("API_KEY"): 5} # The secret key is allowed 5 credits (could mean 5 API calls, 5 chat generations, etc).

#----------------------------------------------------------------------------------------------------------------------------------#
#create a function to check if the user have an api key before allow them to use the llm

def verify_api_key(x_api_key: str =Header(None)): # It checks for an X-API-Key HTTP header in incoming requests, EG --> X-API-Key: abc123secretkey
    credits = API_KEYS_CREDITS.get(x_api_key, 0) # If the key isn't found, it defaults to 0.
    if credits <=0:
        raise HTTPException(status_code=401, detail="Invalid API Key, or no credits left")
    
    return x_api_key # If valid, it simply returns the key, allowing the request to continue.

#----------------------------------------------------------------------------------------------------------------------------------#
@app.post("/generate") # create an end point we can access
def generate(prompt: str, x_api_key: str=Depends (verify_api_key)):
    #to use this function it depends on calling the function (verify_api_key) first and if it raised an error we won't be able to call this function
    try:
        API_KEYS_CREDITS[x_api_key]-=1 #substract a credit every time we use the api
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
 # but we need to run the api so activate the venv first then run --> uvicorn main:app --reloa
 #it will tell us the port which the api runs on --> http://127.0.0.1:8000
#----------------------------------------------------------------------------------------------------------------------------------#

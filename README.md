# debendenceies
----------------
fastapi -> for building api
uvicorn -> for runnig the fastapi app
ollama -> for interfacing with ollamato use a local llm
python-dotenv -> for loading an env file
requests -> for sending request to test the API
---------------------------------------------------------------------------------------------------------------
# virtual env creation 
----------------------
create-> uv venv
select it
add dependencies -> uv add fastapi uvicorn ollama python-dotenv requests
# ---------------------------------------------------------------------------------------------------------------
# ollama setup
--------------
. download it from the website
. add the model (mistral) -->  terminal -> ollama pull mistral


# ---------------------------------------------------------------------------------------------------------------
# test the api using postman
----------------------------
1. uvicorn main:app --reload

2. add the url -> http://127.0.0.1:8000/generate?prompt="What is the capital of France?"

# ---------------------------------------------------------------------------------------------------------------
# secure the api using keys
----------------------------
. make only users who have access, to use our llm , and add credits
. we can have value attached to the key to limit the number of request the user can make (credits)
. make a function to verify the api key and credits left

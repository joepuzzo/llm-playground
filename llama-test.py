
from llama_cpp import Llama

# Load the model
model_path = "./llama-2-7b-chat.Q5_K_M.gguf"

LLM = Llama(model_path)

# create a text prompt
prompt = "Q: What are the names of the days of the week? A:"

# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])

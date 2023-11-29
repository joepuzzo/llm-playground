import os
from llama_cpp import Llama

# Load the model
model_path = "~/.cache/models/llama-2-7b-chat.Q5_K_M.gguf"
expanded_model_path = os.path.expanduser(model_path)
llm = Llama(expanded_model_path)

# Loop to continuously take user input and generate responses
while True:
    # Take user input
    prompt = input("Enter your prompt (type 'exit' to quit): ")
    
    # Check if the user wants to exit the loop
    if prompt.lower() == 'exit':
        break

    # Generate a response
    try:
        # output = llm(prompt)
        output = llm(
 			f"Q: {prompt}? A: ", # Prompt
  			max_tokens=32, # Generate up to 32 tokens
  			stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
		)
        # Display the response
        print("LLaMA says:", output["choices"][0]["text"])
    except Exception as e:
        print("An error occurred:", e)

    print("\n")


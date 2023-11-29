import os
from llama_cpp import Llama

# Load the model
model_path = "~/.cache/models/llama-2-7b-chat.Q4_0.gguf"
expanded_model_path = os.path.expanduser(model_path)
llm = Llama(expanded_model_path)

# Initial setup prompt
initial_prompt = "You are a robot arm named alfred who makes cofee. You are a 7 axis arm made by a company called flexiv. You can hold up to 9 lbs and are very flexible. Your job is to talk to the customers. Have generic friendly conversation when they ask questions."

# Variable to keep track of the conversation history
conversation_history = initial_prompt

# Maximum number of tokens that the model can handle
max_token_limit = 1024  # Adjust this based on the model's capability

# Loop to continuously take user input and generate responses
while True:
    # Take user input
    user_input = input("Enter your prompt (type 'exit' to quit): ")
    
    # Check if the user wants to exit the loop
    if user_input.lower() == 'exit':
        break

    # Update conversation history with user input
    conversation_history += f"\nUser: {user_input}\nAI: "

    # Generate a response
    try:
        output = llm(
            conversation_history,
            #max_tokens=32,  # Generate up to 32 tokens
            stop=["User:", "\n"]  # Stop generating just before the next user input
        )

        # Extract and display the response
        response = output["choices"][0]["text"]
        print("LLaMA says:", response)

        # Update conversation history with the model's response
        conversation_history += response

        # Truncate conversation history if it gets too long
        tokens = conversation_history.split()  # Simple tokenization based on spaces
        if len(tokens) > max_token_limit:
            conversation_history = " ".join(tokens[-max_token_limit:])  # Keep only the last `max_token_limit` tokens

    except Exception as e:
        print("An error occurred:", e)

    print("\n")


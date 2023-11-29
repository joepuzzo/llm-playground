from langchain.chat_models import ChatOllama
llm = ChatOllama(model="llama2:7b-chat")
res = llm.predict("hello")
print (res)

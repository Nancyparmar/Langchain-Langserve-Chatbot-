from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage

chatbot_runnable = ChatOllama(model="llama3.2:1b")

if __name__ == "__main__":
    
    resp = chatbot_runnable.invoke([HumanMessage(content="Hello, how are you?")])
    print(resp.content)

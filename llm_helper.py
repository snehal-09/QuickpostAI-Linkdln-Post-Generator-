from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# ✅ Use latest supported model
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"   # Updated to supported model
)

if __name__ == "__main__":
    response = llm.invoke("Two most important ingredients in samosa are?")
    print(response.content)

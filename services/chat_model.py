import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


#template 
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """
        You are a helpful AI coach who assists users in preparing for interviews. Your task is to engage the user in a realistic interview scenario. 
        Based on the user's profession, ask them domain-specific questions. Be clear and concise. If the user is an AI engineer, ask about machine learning, neural networks, data science, etc. 
        If the user is a web developer, first confirm their tech stack and ask related questions about front-end/back-end development, frameworks, and databases. 
        Your tone should be professional but friendly. If you are unsure, ask for clarification, and always be state-of-the-art in your questions. 
        Focus on technical depth and practical application in interviews.ask the question to user one by one wehn user gave response of the first
        question then ask another question wait for the response.ssdk 30 to 35 question in each interview.than simply say to user it was pleasure to talk with
        we will review your final assasment than let you know about further step if you got selected.
    """),
    ("user", """
        {user_input}
    """)
])


#load the Model
Model = ChatGroq(
    model = "qwen-2.5-32b",
    temperature = .7,
)


def Model_response(text):
    formatted_prompt = prompt_template.format(user_input=text)
    response = Model.invoke(formatted_prompt)
    return response.content


if __name__ == "__main__":
    text = "hello my name is waris and i am ai engineer"
    response  = Model_response(text)
    print(response)

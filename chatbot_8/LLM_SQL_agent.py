#pip install -U langchain-community 
#pip install langchain openai sqlalchemy psycopg2-binary python-dotenv
#pip install langchain-openai


import os
from dotenv import load_dotenv

# ✅ Modern LangChain imports
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.llms import OpenAI
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent



# Load credentials from the custom .env file in chatbot_8 folder
base_path = os.getcwd()
cred_path = os.path.abspath(os.path.join(base_path, "chatbot_8", "open_ai_cred.env"))

print("-------OpenAI Credential Path-------")
print("Base Path:", base_path)
print("OpenAI Credential Path:", cred_path)

# Fetch the containing folder (i.e., 'chatbot_8')
database_folder = os.path.dirname(cred_path)

print(f"In {database_folder} folder, Is open_ai_cred file really exists?", os.path.isfile(cred_path)) 

if os.path.isfile(cred_path):
    load_dotenv(dotenv_path=cred_path)
    print("✅ Loaded OpenAI credentials from .env file\n")
else:
    print("❌ .env file not found at:", cred_path, "\n")



# Load from .env or set manually
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
# print(f"Loaded OpenAI Key: {OPENAI_API_KEY}")


# 1. Create SQLAlchemy URI
db_uri = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 2. Initialize LangChain SQL components
db = SQLDatabase.from_uri(db_uri)

# ✅ Use ChatOpenAI (modern OpenAI LLM for chat-based agents)
llm = OpenAI(
    temperature=0,
    openai_api_key=OPENAI_API_KEY
    # model="gpt-3.5-turbo"  # Or "gpt-4", "gpt-4o", etc.
)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

# -------- Function to Run Natural Language Queries --------
def run_chat_query(question: str) -> str:
    """Ask a natural language question and get SQL-based response."""
    try:
        return agent_executor.invoke({"input": question})["output"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

# -------- Run Example Query --------
if __name__ == "__main__":
    question = "How many helmet violations were there in the last 7 days?"
    print(run_chat_query(question))

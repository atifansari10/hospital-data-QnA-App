from APIs import gemini_api_key
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain


def get_connection():
    db_user = "root"
    db_password = "*******"
    db_host = "localhost"
    db_name = "hospital_management_system"
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
    llm = GoogleGenerativeAI(
        google_api_key=gemini_api_key,
        temperature=0.6,
        model="models/text-bison-001"
    )
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
    return db_chain

from dotenv import load_dotenv
import os

load_dotenv()


class Settings:


    APP_NAME = os.getenv("APP_NAME")
    APP_ENV = os.getenv("APP_ENV")
    DEBUG = os.getenv("DEBUG") == "True"

    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))


    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT"))

    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = int(os.getenv("REDIS_PORT"))
    REDIS_DB = int(os.getenv("REDIS_DB"))

    REDIS_CHAT_STREAM = os.getenv("REDIS_CHAT_STREAM")
    REDIS_CONSUMER_GROUP = os.getenv("REDIS_CONSUMER_GROUP")
    REDIS_CONSUMER_NAME = os.getenv("REDIS_CONSUMER_NAME")

    CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")
    CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION")

    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")

    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
    OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL")


    SHORT_TERM_MEMORY_LIMIT = int(
        os.getenv("SHORT_TERM_MEMORY_LIMIT")
    )

    MEMORY_SUMMARY_THRESHOLD = int(
        os.getenv("MEMORY_SUMMARY_THRESHOLD")
    )


    RAG_TOP_K = int(os.getenv("RAG_TOP_K"))

    RAG_SCORE_THRESHOLD = float(
        os.getenv("RAG_SCORE_THRESHOLD")
    )

    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))

    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))

    MAX_INPUT_TOKENS = int(
        os.getenv("MAX_INPUT_TOKENS")
    )

    MAX_OUTPUT_TOKENS = int(
        os.getenv("MAX_OUTPUT_TOKENS")
    )

    API_SECRET_KEY = os.getenv("API_SECRET_KEY")

    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    )


    LOG_LEVEL = os.getenv("LOG_LEVEL")


settings = Settings()
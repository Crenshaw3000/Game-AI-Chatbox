from langchain_ollama import OllamaEmbeddings
#from langchain_bedrock import BedrockEmbeddings  # Update this if using Bedrock embeddings
from langchain_openai import OpenAIEmbeddings

def get_embedding_function(embedding_type="openai"):
    if embedding_type == "openai":
        # Create an instance of OpenAIEmbeddings with model_kwargs
        return OpenAIEmbeddings(model_kwargs={"model_name": "text-embedding-ada-002"})
    
    #elif embedding_type == "bedrock":
        # Create an instance of BedrockEmbeddings
        #return BedrockEmbeddings(credentials_profile_name="default", region_name="us-east-1")
    
    elif embedding_type == "ollama":
        # Create an instance of OllamaEmbeddings
        return OllamaEmbeddings(model="nomic-embed-text")
    
    else:
        raise ValueError(f"Unsupported embedding type: {embedding_type}")

# Example usage:
# embeddings = get_embedding_function("openai")
# embeddings = get_embedding_function("bedrock")
# embeddings = get_embedding_function("ollama")

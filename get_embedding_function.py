from langchain_ollama import OllamaLLM, OllamaEmbeddings

def get_embedding_function(embedding_type="mistral"):
    if embedding_type == "mistral":
        # Create an instance of OllamaEmbeddings with Mistral
        return OllamaEmbeddings(model="mistral")
    else:
        raise ValueError(f"Unsupported embedding type: {embedding_type}")



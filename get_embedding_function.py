from langchain_ollama import OllamaLLM, OllamaEmbeddings


def get_embedding_function(embedding_type="mistral"):
    if embedding_type == "mistral":
        # Create an instance of OllamaEmbeddings with Mistral
        return OllamaEmbeddings(model="mistral")
    
    elif embedding_type == "llama3":
        # Create an instance of OllamaEmbeddings with Llama 3
        return OllamaEmbeddings(model="llama-3")

    else:
        raise ValueError(f"Unsupported embedding type: {embedding_type}")



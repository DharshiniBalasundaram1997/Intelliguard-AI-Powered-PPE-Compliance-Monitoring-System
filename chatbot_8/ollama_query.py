#Step 1:
# ollama serve

#if the server is running already then we can kill it use below step 2 & step 3
#Step 2 
# netstat -ano | findstr :11434

#Step 3:
# taskkill /PID 22280 /F

#To check the model lists:
# ollama list

# pip install ollama



from ollama import Client

client = Client(host="http://localhost:11434")

def run_ollama_query(prompt):
    """
    Call the local Ollama LLM (Llama 3.2) to get a response.
    """
    response = client.chat(
        model="llama3.2:latest",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI assistant that answers questions about PPE violation logs. "
                    "Be precise and concise."
                ),
            },
            {"role": "user", "content": prompt},
        ]
    )
    return response["message"]["content"]


if __name__ == "__main__":
    query = "Summarize the key PPE violations detected this month."
    answer = run_ollama_query(query)
    print("Response from Llama 3.2:\n", answer)

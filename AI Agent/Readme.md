# 🧠 AI Research Agent

An autonomous research assistant built using **LangGraph**, **LangChain**, **Pydantic**, and **Groq's LLaMA 3.3 (70B)** model.  
The agent automatically gathers information from **Wikipedia** and **web search**, synthesizes the findings, and outputs clean, validated **JSON research summaries**.

---

## 📘 Overview

The **AI Research Agent** automates the entire research workflow:

- Accepts a research topic from the user  
- Fetches information from **Wikipedia**  
- Performs **web searches** (simulated for demo)  
- Synthesizes all data using **Groq’s LLaMA 3.3 model**  
- Produces structured, validated **JSON** results  
- Saves all research outputs to a text file  

Built using:

- **LangGraph** → Workflow orchestration  
- **LangChain** → LLM interaction  
- **Groq LLaMA 3.3 (70B)** → Fast inference  
- **Pydantic** → Type-safe output validation  

---

## ✨ Features

- 🔍 **Multi-Source Research**  
  Combines Wikipedia summaries with web search info.

- 📦 **Structured JSON Output**  
  Returns neatly formatted results with topic, summary, tools, and sources.

- 🛡️ **Robust Error Handling**  
  Handles API errors, malformed JSON, and connection failures gracefully.

- 💾 **Automatic File Saving**  
  Each research result is stored in `research_output.txt`.

- 🔒 **Type Safety with Pydantic**  
  Ensures that every output follows a consistent JSON schema.

- ⚙️ **Workflow Automation with LangGraph**  
  Manages task sequencing and state transitions automatically.

- ⚡ **Ultra-Fast LLM Inference**  
  Powered by Groq’s optimized LLaMA 3.3 model.

---

## 🛠 Installation & Setup

### **1. Install Python**

Python **3.8+** is required (Python **3.12 recommended**).

### **2. Create a Virtual Environment**

bash
python -m venv venv  

### **3. Activate the Environment**

bash
venv\Scripts\activate

### **4.Install Dependencies**

bash
pip install -r requirements.txt

### **5. Add Groq API Key**

Get your api key from groq and place it in .env file (GROQ_API_KEY=your_groq_api_key_here )

### **6. Running the Agent**

Simply run your main.py file 
(python main.py)

## 🔍 How It Works

**User Input**  
The user enters a research topic via the command line.  
Example: `"Who is Albert Einstein?"`

**State Initialization**  
LangGraph initializes the agent’s state:  
`{"query": "Albert Einstein", "result": ""}`

**Tool Execution (llm_node)**  
- **Wikipedia Lookup:** Fetches a summary from the Wikipedia REST API  
- **Web Search:** Returns search results (currently simulated)  
- **Metadata Logged:** Tools used, source URLs, retrieved text  

**Prompt Construction**  
- Combines user query + Wikipedia summary + search results  
- Adds JSON schema instructions for structured output  
- Builds a formatted prompt for the LLM  

**LLM Processing**  
- Sends the prompt to **Groq’s LLaMA 3.3 70B** model  
- Uses **temperature = 0.2** for factual, accurate output  
- Model returns structured JSON  

**Output Parsing**  
- Pydantic validates the JSON structure  
- Ensures required fields: `topic`, `summary`, `sources`, `tools_used`  
- Converts data into a `ResearchResponse` object  

**Output Delivery**  
- Displays structured output in the console  
- Saves the result to `researchoutput.txt`  
- Confirms successful completion to the user


## Screenshots




 


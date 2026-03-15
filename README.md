---

# 📄 RAG PDF Question Answering System

A **Retrieval-Augmented Generation (RAG)** application that extracts knowledge from research papers (PDFs), stores embeddings in a local vector database, and answers questions using a local LLM.

The project uses:

* **LangChain** for building the RAG pipeline
* **Chroma** for storing embeddings
* **Streamlit** for the user interface
* **Ollama** for running local models

---

# 🚀 Project Overview

This project implements a **complete RAG pipeline**:

```
PDF Papers
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embeddings
   ↓
Chroma Vector Database
   ↓
Retriever
   ↓
Local LLM (Mistral)
   ↓
Answer Generation
```

Users can ask questions about the PDFs, and the system retrieves the most relevant chunks before generating the answer.

---

# 🧠 Key Features

✅ PDF downloading and ingestion
✅ Recursive text chunking
✅ Embedding generation
✅ Vector database storage (Chroma)
✅ Retrieval-Augmented Generation (RAG)
✅ Streamlit UI for question answering
✅ Local LLM inference using Ollama

---

# 📂 Project Structure

```
rag-pdf-qa/
│
├── pdf_.py
│   └── Downloads research papers from the internet
│
├── chunking.py
│   └── Extracts text from PDFs
│   └── Splits text into chunks
│   └── Generates embeddings
│   └── Stores embeddings in Chroma vector database
│
├── Streamlit.py
│   └── Loads stored embeddings
│   └── Runs the RAG pipeline
│   └── Provides a UI to ask questions
│
├── chroma_db/
│   └── Local vector database storing embeddings
│
└── README.md
```

---

# ⚙️ How the System Works

## 1️⃣ Download Research Papers

The script downloads PDFs from online sources.

```
python pdf_.py
```

This will save the files as:

```
file_pdf1.pdf
file_pdf2.pdf
```

---

## 2️⃣ Extract Text and Create Embeddings

The `chunking.py` script:

* Extracts text from the PDFs
* Splits the text into chunks using **RecursiveCharacterTextSplitter**
* Converts chunks into embeddings
* Stores them inside **Chroma vector database**

```
python chunking.py
```

This will create the folder:

```
chroma_db/
```

Which contains the stored embeddings.

---

## 3️⃣ Ask Questions Using Streamlit

The Streamlit app loads the stored embeddings and performs retrieval + generation.

```
streamlit run Streamlit.py
```

A browser window will open where you can ask questions about the documents.

---
# How to use the application
```
1. you a have to install all the packages before hand
2. have to install ollama for loacl_llm
3. this file contain agentic chunking and recursive chunking as but for agentic chunking you have to buy the tokens, otherwise you will get only limited calls
4. to run the chunking file, command : (python chunking.py)
5. to run the streamlit filr, command : (streamlit run streamlit.py)
6. you have to create an api for using agentic chunking before hand
```
# 🖥 Example Usage

### User Question

```
What is the main idea behind reasoning models?
```

### System Workflow

```
User Question
      ↓
Embedding Conversion
      ↓
Similarity Search in Chroma
      ↓
Relevant Context Retrieved
      ↓
Mistral LLM Generates Answer
```

---

# 📦 Dependencies

Install all required libraries:

```
pip install langchain
pip install langchain-community
pip install langchain-ollama
pip install chromadb
pip install streamlit
pip install pymupdf
pip install requests
pip install rich
pip install python-dotenv
```

---

# 🧾 Required Models

This project uses the **Mistral model via Ollama**.

Install Ollama and pull the model:

```
ollama pull mistral
```

The embedding model used:

```
nomic-embed-text
```

---

# 📊 Vector Database

Embeddings are stored locally using **Chroma**.

Directory created:

```
chroma_db/
 ├── chroma.sqlite3
 ├── collections
 └── index
```

This allows **fast similarity search during retrieval**.

---

# 🖥 Example UI

The Streamlit interface allows users to:

* Enter a question
* Retrieve answers from the PDFs
* Measure query response time

Displayed information:

```
Answer
Query Time
```

---
# Output_Image
<p align="center">
  <img src="Screenshot 2026-03-15 203359.png" width="700">
</p>
---

# 📚 Learning Concepts

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector databases
* Embeddings
* Document chunking
* Local LLM inference
* Semantic search

---

# 👨‍💻 Author

**Snigdh Chamoli**

Interested in:

* AI / Machine Learning
* Backend Engineering
* System Design
* Distributed AI Systems


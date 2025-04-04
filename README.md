AI-Powered PDF Q&A App

This project allows users to upload a PDF and ask questions about its content. Instead of reading through long documents, the app retrieves relevant information and provides concise answers.
Features:

    1. Upload a PDF file

    2. Ask questions in natural language

    3. Get AI-generated answers based on the document's content

    4. Runs locally with Ollama, no external API required

Installation and Setup:

Clone the repository:

    git clone https://github.com/sid-2672/pdf_qa_app.git
    
    cd pdf_qa_app  

Install dependencies:

    pip install -r requirements.txt  

Ensure Ollama is running:

    ollama serve  

Run the Streamlit app:

    streamlit run app.py  

Credits:
This project is inspired by the following article:
[LLM RAG: Creating an AI-Powered File Reader Assistant]
(https://towardsdatascience.com/llm-rag-creating-an-ai-powered-file-reader-assistant/?utm_campaign=tds%20variable&utm_medium=email&_hsmi=354843008&utm_source=newsletter)
Future Improvements:

    1. Support for additional file types (TXT, DOCX)

    2. Improved retrieval accuracy

    3. Option to deploy online
That's for all for today! 
Remember:
    DATA IS ALL, ALL IS DATA!

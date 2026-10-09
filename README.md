# Concise AI Q&A

A Streamlit interface for the LangChain/OpenAI question-answering script.

## Run locally

Install the dependencies and set the OpenAI API key:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:OPENAI_API_KEY = "your-api-key"
.\.venv\Scripts\python.exe -m streamlit run app.py
```

You can also create `.streamlit/secrets.toml` with:

```toml
OPENAI_API_KEY = "your-api-key"
```

Do not commit the API key or the secrets file.

## Deploy to Streamlit Community Cloud

1. Push this project to a GitHub repository. Keep `.venv` out of the repository.
2. In Streamlit Community Cloud, create an app from that repository and select `app.py` as the entry point.
3. Add `OPENAI_API_KEY` in the app's **Settings → Secrets**.

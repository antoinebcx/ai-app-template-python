# AI app template

This project is a template of an AI app, built with Python and Streamlit. It demonstrates how to use AI services to extract information in a structured way from text, audio, and images.

The project shows how to use structured outputs with a reasoning field, how to effectively structure a prompt with XML tags, and how to use few-shot examples (in-context learning).

The app supports text inputs, audio transcription and text extraction from images.

## To use the app

To use the app, you need to create a `.env` file at the root of the project with:
```
OPENAI_API_KEY = [your OpenAI API key]
```

Then, you can open a terminal window, go to the project path and run:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/main.py
```

All the code is in the `/src` directory.

# AI app template

This project is a template of an AI app, built with Python and Streamlit. It demonstrates how to use AI services to extract information in a structured way from text, audio, and images.

The project shows how to effectively structure a prompt with XML tags and how to use structured outputs with a reasoning field, function calling (tool use) and few-shot examples (in-context learning).

The app supports text inputs, audio transcription and text extraction from images.

<img width="1320" alt="image" src="https://github.com/user-attachments/assets/82067fb0-2bc4-4625-a3e9-551ebbf1544f" />

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


## The code

All the code is in the `/src` directory.

It contains:
- UI and orchestration in `main.py`
- AI services (LLM, audio transcription and text extraction from image) in `ai_services.py`
- Utilities (get the prompts, encode images) in `utils.py`
- System prompt and user prompt with XML tags in `prompts.py`
- Few-shot example in `few_shot.py`
- Structured outputs Pydantic schemas in `schemas.py`
- Function calling (tool use) in `function_calling.py`

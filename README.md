# AI app template

This project is a simple demo of an AI app, built with Python and Streamlit. It demonstrates how to use AI services to analyze text, audio, and images. 


## To use the app

To use the tool, you need to create a .env at the root of the project with inside:
```
OPENAI_API_KEY = [your OpenAI API key]
```

Then, you can open a terminal window, go to the project folder and run:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run main.py
```

If you just want to have a look at the code, you will find in `main.py` the code related to the Streamlit app, and in `ai_services.py` the utility and AI functions.

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# initialize OpenAI client
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)
model_function_calling = "gpt-4o-2024-08-06"

tools = [{
    "type": "function",
    "function": {
        "name": "classify_input",
        "description": "Classify the input text into predefined categories",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "enum": ["scientific", "historical", "technical", "business", "other"],
                    "description": "The category that best matches the input text"
                },
                "confidence": {
                    "type": "number",
                    "description": "Confidence score between 0 and 1"
                },
            },
            "required": ["category", "confidence"],
            "additionalProperties": False
        },
        "strict": True
    }
}]

def classify_input(text_input: str) -> dict:
    """
    Use function calling to classify the input text into categories.
    """
    try:
        completion = client.chat.completions.create(
            model=model_function_calling,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert at classifying text into categories. Analyze the input carefully and provide accurate classifications."
                },
                {
                    "role": "user", 
                    "content": f"Please classify this text:\n\n{text_input}"
                }
            ],
            tools=tools
        )
        
        tool_call = completion.choices[0].message.tool_calls[0]
        result = eval(tool_call.function.arguments)
        
        return result
        
    except Exception as e:
        print(f"Error in classification: {e}")
        return {
            "category": "other",
            "confidence": 0.0,
        }

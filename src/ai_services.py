import os
import base64
from typing import Dict, Any
from dotenv import load_dotenv
from openai import OpenAI
from schemas import InputAnalysisSchema

load_dotenv()

# initialize openai client
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)
model_gpt = "gpt-4o-2024-08-06"
model_vision = "gpt-4o-2024-08-06"


def get_system_prompt() -> str:
    return "You are a input element number counter."


def get_user_prompt(text_input: str) -> str:
    return f"""
<INSTRUCTIONS>
Your role is to perfectly analyze and describe the input in a structured way.
</INSTRUCTIONS>

Now, please analyze this input:
<INPUT>
{text_input}
</INPUT>
"""


def llm_analysis(text_input: str) -> Dict[str, Any]:
    """
    Using structured outputs, perform a structured analysis of the input with GPT.
    """

    try:
        completion = client.beta.chat.completions.parse(
            model=model_gpt,
            messages=[
                {"role": "system", "content": get_system_prompt()},
                {"role": "user", "content": get_user_prompt(text_input)}
            ],
            response_format=InputAnalysisSchema,
            temperature=0,
            seed=42
        )
    except Exception as e:
        print(f"Error: {e}")
        return None

    analysis_result = completion.choices[0].message.parsed

    return analysis_result


def audio_transcription(audio):
    """
    Transcribe audio using Whisper.
    """
    try:
        filename = 'input.mp3'
        with open(filename, "wb") as wav_file:
            wav_file.write(audio.read())
        with open(filename, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                language="en",
                file=audio_file,
                response_format="text"
            )
        os.remove(filename)
        return transcript
    except Exception as e:
        raise Exception(f"Failed to transcribe audio: {e}")


def encode_image(uploaded_file):
    """
    Encode an image to base64.
    """
    return base64.b64encode(uploaded_file.getvalue()).decode('utf-8')


def image_to_text(uploaded_image):
    """
    Extact text from an image using GPT-Vision.
    """
    try:
        base64_image = encode_image(uploaded_image)
        response = client.chat.completions.create(
            model=model_vision,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Please return all the text from this image, as is.",
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                        },
                    ],
                }
            ],
            temperature=0,
            seed=42
        )

        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Failed to extract text from image: {e}")

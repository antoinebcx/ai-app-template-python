import base64
from prompts import SYSTEM_PROMPT, USER_PROMPT
from few_shot import FEW_SHOT_EXAMPLE


def get_system_prompt() -> str:
    """
    Returns the system prompt for the GPT model.
    """
    return SYSTEM_PROMPT


def get_user_prompt(text_input: str) -> str:
    """
    Formats and returns the user prompt with the provided input text.
    """
    return USER_PROMPT.format(
        FEW_SHOT_EXAMPLE=FEW_SHOT_EXAMPLE,
        text_input=text_input
        )


def encode_image(uploaded_image) -> str:
    """
    Encodes an uploaded image to base64 string.
    """
    return base64.b64encode(uploaded_image.getvalue()).decode('utf-8')

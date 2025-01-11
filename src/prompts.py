SYSTEM_PROMPT = """You are an input analyzer."""


USER_PROMPT = """
<INSTRUCTIONS>
Your role is to perfectly analyze and describe the input in a structured way.
</INSTRUCTIONS>

<FEW-SHOT EXAMPLE>
{FEW_SHOT_EXAMPLE}
</FEW-SHOT EXAMPLE>

Now, please analyze this input:
<INPUT>
{text_input}
</INPUT>
"""

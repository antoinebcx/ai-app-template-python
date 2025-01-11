from typing import List
from pydantic import BaseModel, Field


class ElementSchema(BaseModel):
    """
    Model for tracking individual elements within an input and analyzing them.
    """

    element_number: int = Field(
        description="Number of appearance of the element."
    )
    element_name: str = Field(
        description="Name of the element."
    )
    element_description: str = Field(
        description="Description of the element."
    )


class InputAnalysisSchema(BaseModel):
    """
    Main Pydantic model for analyzing and summarizing the input.
    Contains a reasoning field, individual element identification, and a summary.
    """

    reasoning: str = Field(
        description="Reasoning field to understand the input before writing the analysis and summary."
    )
    elements: List[ElementSchema] = Field(
        description="Identifying and analyzing individual elements of the input, one by one."
    )
    summary: str = Field(
        description="The number of elements in the input."
    )

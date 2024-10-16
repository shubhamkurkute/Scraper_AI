import openai
import os
from pydantic import BaseModel


openai.api_key = os.environ["OPEN_API_KEY"]


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


completion = openai.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
    ],
    response_format=CalendarEvent,
)
event = completion.choices[0].message.parsed
print(event)

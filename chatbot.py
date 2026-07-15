import time
from google import genai

API_KEY = "YOUR_GEMINI_API_KEY"

client = genai.Client(api_key=API_KEY)


def get_response(prompt):

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception:

            if attempt < 2:
                time.sleep(2)
            else:
                return "⚠️ Gemini servers are currently busy. Please try again in a few moments."

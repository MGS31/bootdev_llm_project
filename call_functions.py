from google.genai import GenerativeModel
from functions.retry_utils import retry_on_429_503

# Example: wrap a Google AI API call with the retry decorator
@retry_on_429_503(max_retries=5, base_delay=1.0, max_delay=16.0)
def call_google_ai(prompt):
    model = GenerativeModel('gemini-pro')
    return model.generate_content(prompt)

if __name__ == "__main__":
    try:
        result = call_google_ai("Say hello!")
        print(result)
    except Exception as e:
        print(f"API call failed after retries: {e}")

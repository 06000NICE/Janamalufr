
# Required Libraries
import openai
from langdetect import detect
import os

# Function to detect language
def detect_language(text):
    return detect(text)

# Function to improve email using OpenAI's GPT
def improve_email(text, language):
    # Define the prompt based on the language
    if language == 'en':
        prompt = f"Improve the following email for clarity and professionalism:\n{text}"
    elif language == 'fr':
        prompt = f"Améliore cet e-mail pour qu’il soit plus clair et professionnel :\n{text}"
    elif language == 'ja':
        prompt = f"以下のメールをより丁寧で明確な日本語に改善してください：\n{text}"
    else:
        return "Unsupported language."

    # Call OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the improved email from the response
    improved_email = response.choices[0].text.strip()
    return improved_email

# Main function to run the script
def main():
    # Set your OpenAI API key here
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Input email text
    email_text = input("Enter the email text: ")

    # Detect language
    language = detect_language(email_text)
    print(f"Detected language: {language}")

    # Improve email
    improved_email = improve_email(email_text, language)
    print("\nImproved Email:\n")
    print(improved_email)

if __name__ == "__main__":
    main()

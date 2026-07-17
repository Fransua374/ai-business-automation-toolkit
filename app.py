from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_email():
    print("\n=== AI Email Generator ===")

    name = input("Who is the email for? ")
    topic = input("What is the email about? ")

    print("\nGenerating email...\n")

    response = client.responses.create(
        model="gpt-5",
        input=f"""
Write a professional business email.

Recipient: {name}
Purpose: {topic}

Return only the email.
"""
    )

    print(response.output_text)


def main():
    while True:
        print("\n================================")
        print("🚀 AI Business Assistant")
        print("================================")

        print("1. Generate Email")
        print("2. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            generate_email()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
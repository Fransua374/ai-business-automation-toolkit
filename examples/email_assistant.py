from src.ai.client import AIClient

def main():
    ai = AIClient()

    email = ai.generate(
        "Write a professional welcome email for a new client."
    )

    print(email)

if __name__ == "__main__":
    main()

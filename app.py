from src.ai.client import AIClient
from src.utils import log
from src.config import APP_NAME, VERSION

def main():
    log(f"Starting {APP_NAME} v{VERSION}")

    ai = AIClient()

    prompt = "Write a welcome email for a new customer."

    response = ai.generate(prompt)

    print("\nAI Response:")
    print(response)

if __name__ == "__main__":
    main()

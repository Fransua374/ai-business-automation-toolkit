from src.ai.client import AIClient

def main():
    ai = AIClient()

    summary = ai.generate(
        "Summarise a business document into bullet points."
    )

    print(summary)

if __name__ == "__main__":
    main()

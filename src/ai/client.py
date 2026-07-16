import os

class AIClient:
    def __init__(self):
        self.provider = "OpenAI"

    def generate(self, prompt):
        return f"Demo response for: {prompt}"

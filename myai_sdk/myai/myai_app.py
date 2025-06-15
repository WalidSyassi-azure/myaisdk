def answer(question: str) -> str:
    """
    Simple AI function that answers a specific question.
    Extend this with real AI later.
    """
    question = question.lower().strip()
    if question == "what is ai?":
        return "AI stands for Artificial Intelligence. It is the simulation of human intelligence by machines."
    else:
        return "Sorry, I can only answer: 'What is AI?' for now."

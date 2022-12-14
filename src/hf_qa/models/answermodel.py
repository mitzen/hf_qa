class AnswerModel:
    def __init__(self, answer: str, score: float, end: int, start: int) -> None:
        self.answer = answer
        self.score = score
        self.end = end
        self.start = start
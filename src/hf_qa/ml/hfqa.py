from models.questionmodel import QuestionModel
from models.answermodel import AnswerModel
from transformers import pipeline

class HuggingFaceQuestionAnswerModel:
    
    def __init__(self) -> None:
        self.qa_model = pipeline("question-answering")

    def process_qa(self, model: QuestionModel) -> AnswerModel:
        response = self.qa_model(question = model.question, context = model.context)
        return response
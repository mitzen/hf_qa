from flask import jsonify, request
from flask.views import MethodView
import json 
from types import SimpleNamespace
from models.questionmodel import QuestionModel
from ml.hfqa import HuggingFaceQuestionAnswerModel

class QaController(MethodView):
    
    def __init__(self, model: any):
        self.qa_model = HuggingFaceQuestionAnswerModel()

    async def post(self) -> str:
        model = await self.getQuestionModel(request.data)
        response = self.qa_model.process_qa(model)
        return jsonify(response)
    
    async def getQuestionModel(self, request: any) -> QuestionModel:
        model = json.loads(request, object_hook=lambda d: SimpleNamespace(**d))
        return model
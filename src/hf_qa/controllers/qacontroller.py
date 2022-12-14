from flask import jsonify, request
from flask.views import MethodView
import json 
from types import SimpleNamespace
from models.questionmodel import QuestionModel
from typing import Type as T
from transformers import pipeline

class QaController(MethodView):
    
    def __init__(self, model: any):
        self.qa_model = pipeline("question-answering")
        
    async def get(self, model: any) -> str:
        return ""

    async def post(self) -> str:
        model = await self.getQuestionModel(request.data)
        response = self.qa_model(question = model.question, context = model.context)
        return jsonify(response)
    
    async def getQuestionModel(self, request: any) -> QuestionModel:
        model = json.loads(request, object_hook=lambda d: SimpleNamespace(**d))
        return model
from flask import Flask
from controllers.qacontroller import QaController

app = Flask(__name__)

def register_api(app: Flask, model: any, url: str):
    targetAPI = QaController.as_view(f"{url}-item", model)
    app.add_url_rule(f"/{url}", view_func=targetAPI)

register_api(app, "", "/")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
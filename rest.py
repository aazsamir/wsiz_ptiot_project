from flask import Flask
import json

from lib.engine.fileConfigParser import FileConfigParser
from lib.api.repositoryFactory import RepositoryFactory
from lib.api.repository import Repository
from lib.api.result import Result

app = Flask(__name__)


def createRepository() -> Repository:
    config = FileConfigParser("config.json").parse()

    return RepositoryFactory().make(config)


@app.route("/")
def index():
    repository = createRepository()
    results = repository.getAll()

    return jsonize(results)


@app.route('/name/<name>')
def show(name: str):
    repository = createRepository()
    results = repository.getByName(name)

    return jsonize(results)


def jsonize(results: list[Result]) -> str:
    json_data = []

    for result in results:
        json_data.append({
            "name": result.name(),
            "result": result.result(),
            "date": result.date().strftime("%Y-%m-%d %H:%M:%S")
        })

    return json.dumps(json_data)

from flask import Flask, request, jsonify, render_template, make_response
from utils.validador_de_cpf import validandoCPF

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def cpf_index():

    return render_template('index.html')


@app.route('/validarCPF', methods=['POST', 'GET'])
def validarCPF():
    req = request.get_json()
    retornoCPF = validandoCPF(cpf=req['cpf'])
    res = make_response(jsonify({"mensagem": str(retornoCPF)}), 200)
    return res

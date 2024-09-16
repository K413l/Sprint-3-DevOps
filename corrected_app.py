from flask import Flask, jsonify

app = Flask(__name__)  # Mantendo a inicialização correta

# Removendo temporariamente a conexão com o banco de dados para testar a API sem dependência do banco
# Modelo para a tabela BANCO comentado temporariamente

# Função exemplo para testar a API
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello World!"}), 200

# Rotas adicionais desabilitadas devido à dependência do banco de dados removida

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

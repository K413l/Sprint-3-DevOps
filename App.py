from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+oracledb://RM551007:030803@oracle.fiap.com.br:1521/orcl'
db = SQLAlchemy(app)

# Modelo para a tabela BANCO
class Banco(db.Model):
    __tablename__ = 'TB_BANCO'
    id_banco = db.Column('ID_BANCO', db.Integer, primary_key=True)
    nm_banco = db.Column('NM_BANCO', db.String(100), nullable=True)
    cd_banco = db.Column('CD_BANCO', db.String(10), nullable=True)

# Função para criar o banco de dados
def create_database():
    with app.app_context():  # Cria um contexto de aplicação
        db.create_all()

@app.route('/', methods=['GET'])
print('Hello World')

@app.route('/bancos', methods=['POST'])
def create_banco():
    data = request.get_json()
    new_banco = Banco(nm_banco=data['nm_banco'], cd_banco=data['cd_banco'])
    db.session.add(new_banco)
    db.session.commit()
    return jsonify({"message": "Banco criado com sucesso!"}), 201

@app.route('/bancos', methods=['GET'])
def get_bancos():
    bancos = Banco.query.all()
    return jsonify([{'id_banco': banco.id_banco, 'nm_banco': banco.nm_banco, 'cd_banco': banco.cd_banco} for banco in bancos])

@app.route('/bancos/<int:id>', methods=['GET'])
def get_banco(id):
    banco = Banco.query.get(id)
    if not banco:
        return jsonify({"message": "Banco não encontrado"}), 404
    return jsonify({'id_banco': banco.id_banco, 'nm_banco': banco.nm_banco, 'cd_banco': banco.cd_banco})

@app.route('/bancos/<int:id>', methods=['PUT'])
def update_banco(id):
    data = request.get_json()
    banco = Banco.query.get(id)
    if not banco:
        return jsonify({"message": "Banco não encontrado"}), 404

    banco.nm_banco = data['nm_banco']
    banco.cd_banco = data['cd_banco']
    db.session.commit()
    return jsonify({"message": "Banco atualizado com sucesso!"})

@app.route('/bancos/<int:id>', methods=['DELETE'])
def delete_banco(id):
    banco = Banco.query.get(id)
    if not banco:
        return jsonify({"message": "Banco não encontrado"}), 404

    db.session.delete(banco)
    db.session.commit()
    return jsonify({"message": "Banco excluído com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
    create_database()  # Chama a função para criar as tabelas no banco
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Utilize a variável de ambiente definida no Azure
app.config['SQLALCHEMY_DATABASE_URI'] = "oracle+oracledb://RM551007:030803@oracle.fiap.com.br:1521/orcl"

db = SQLAlchemy(app)

# Modelo para a tabela TB_BANCO
class Banco(db.Model):
    __tablename__ = 'TB_BANCO'
    id_banco = db.Column('ID_BANCO', db.Integer, primary_key=True)
    nm_banco = db.Column('NM_BANCO', db.String(100), nullable=False)
    cd_banco = db.Column('CD_BANCO', db.String(10), nullable=False)
    
    clientes = db.relationship('Cliente', backref='banco', lazy=True)

# Modelo para a tabela TB_CLIENTE
class Cliente(db.Model):
    __tablename__ = 'TB_CLIENTE'
    id_cliente = db.Column('ID_CLIENTE', db.Integer, primary_key=True)
    nm_cliente = db.Column('NM_CLIENTE', db.String(100), nullable=False)
    em_cliente = db.Column('EM_CLIENTE', db.String(100), nullable=False)
    tf_cliente = db.Column('TF_CLIENTE', db.String(15), nullable=False)
    id_banco = db.Column('ID_BANCO', db.Integer, db.ForeignKey('TB_BANCO.ID_BANCO'), nullable=False)

# Função para criar o banco de dados
def create_database():
    with app.app_context():
        db.create_all()

# Rotas de CRUD para a tabela Banco
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


# Rotas de CRUD para a tabela Cliente
@app.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    new_cliente = Cliente(nm_cliente=data['nm_cliente'], em_cliente=data['em_cliente'], tf_cliente=data['tf_cliente'], id_banco=data['id_banco'])
    db.session.add(new_cliente)
    db.session.commit()
    return jsonify({"message": "Cliente criado com sucesso!"}), 201

@app.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([{'id_cliente': cliente.id_cliente, 'nm_cliente': cliente.nm_cliente, 'em_cliente': cliente.em_cliente, 'tf_cliente': cliente.tf_cliente, 'id_banco': cliente.id_banco} for cliente in clientes])

@app.route('/clientes/<int:id>', methods=['GET'])
def get_cliente(id):
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({"message": "Cliente não encontrado"}), 404
    return jsonify({'id_cliente': cliente.id_cliente, 'nm_cliente': cliente.nm_cliente, 'em_cliente': cliente.em_cliente, 'tf_cliente': cliente.tf_cliente, 'id_banco': cliente.id_banco})

@app.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.get_json()
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({"message": "Cliente não encontrado"}), 404

    cliente.nm_cliente = data['nm_cliente']
    cliente.em_cliente = data['em_cliente']
    cliente.tf_cliente = data['tf_cliente']
    cliente.id_banco = data['id_banco']
    db.session.commit()
    return jsonify({"message": "Cliente atualizado com sucesso!"})

@app.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({"message": "Cliente não encontrado"}), 404

    db.session.delete(cliente)
    db.session.commit()
    return jsonify({"message": "Cliente excluído com sucesso!"})


if __name__ == '__main__':
    create_database()  # Cria as tabelas no banco de dados
    app.run(debug=True)

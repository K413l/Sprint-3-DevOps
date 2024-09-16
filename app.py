from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)

# Configuração da conexão com o banco de dados Oracle
app.config['SQLALCHEMY_DATABASE_URI'] = "oracle+oracledb://RM551007:030803@oracle.fiap.com.br:1521/orcl"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando a instância do SQLAlchemy
db = SQLAlchemy(app)

# Configurando logging
logging.basicConfig(level=logging.DEBUG)

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
    try:
        data = request.get_json()
        new_banco = Banco(nm_banco=data['nm_banco'], cd_banco=data['cd_banco'])
        db.session.add(new_banco)
        db.session.commit()
        return jsonify({"message": "Banco criado com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()  # Reverte qualquer alteração no banco de dados em caso de erro
        app.logger.error(f"Erro ao criar banco: {str(e)}")
        return jsonify({"error": "Erro ao criar banco"}), 500

@app.route('/bancos', methods=['GET'])
def get_bancos():
    try:
        bancos = Banco.query.all()
        return jsonify([{'id_banco': banco.id_banco, 'nm_banco': banco.nm_banco, 'cd_banco': banco.cd_banco} for banco in bancos])
    except Exception as e:
        app.logger.error(f"Erro ao buscar bancos: {str(e)}")
        return jsonify({"error": "Erro ao buscar bancos"}), 500

@app.route('/bancos/<int:id>', methods=['GET'])
def get_banco(id):
    try:
        banco = Banco.query.get(id)
        if not banco:
            return jsonify({"message": "Banco não encontrado"}), 404
        return jsonify({'id_banco': banco.id_banco, 'nm_banco': banco.nm_banco, 'cd_banco': banco.cd_banco})
    except Exception as e:
        app.logger.error(f"Erro ao buscar banco: {str(e)}")
        return jsonify({"error": "Erro ao buscar banco"}), 500

@app.route('/bancos/<int:id>', methods=['PUT'])
def update_banco(id):
    try:
        data = request.get_json()
        banco = Banco.query.get(id)
        if not banco:
            return jsonify({"message": "Banco não encontrado"}), 404

        banco.nm_banco = data['nm_banco']
        banco.cd_banco = data['cd_banco']
        db.session.commit()
        return jsonify({"message": "Banco atualizado com sucesso!"})
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Erro ao atualizar banco: {str(e)}")
        return jsonify({"error": "Erro ao atualizar banco"}), 500

@app.route('/bancos/<int:id>', methods=['DELETE'])
def delete_banco(id):
    try:
        banco = Banco.query.get(id)
        if not banco:
            return jsonify({"message": "Banco não encontrado"}), 404

        db.session.delete(banco)
        db.session.commit()
        return jsonify({"message": "Banco excluído com sucesso!"})
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Erro ao excluir banco: {str(e)}")
        return jsonify({"error": "Erro ao excluir banco"}), 500


# Rotas de CRUD para a tabela Cliente
@app.route('/clientes', methods=['POST'])
def create_cliente():
    try:
        data = request.get_json()
        new_cliente = Cliente(nm_cliente=data['nm_cliente'], em_cliente=data['em_cliente'], tf_cliente=data['tf_cliente'], id_banco=data['id_banco'])
        db.session.add(new_cliente)
        db.session.commit()
        return jsonify({"message": "Cliente criado com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Erro ao criar cliente: {str(e)}")
        return jsonify({"error": "Erro ao criar cliente"}), 500

@app.route('/clientes', methods=['GET'])
def get_clientes():
    try:
        clientes = Cliente.query.all()
        return jsonify([{'id_cliente': cliente.id_cliente, 'nm_cliente': cliente.nm_cliente, 'em_cliente': cliente.em_cliente, 'tf_cliente': cliente.tf_cliente, 'id_banco': cliente.id_banco} for cliente in clientes])
    except Exception as e:
        app.logger.error(f"Erro ao buscar clientes: {str(e)}")
        return jsonify({"error": "Erro ao buscar clientes"}), 500

@app.route('/clientes/<int:id>', methods=['GET'])
def get_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if not cliente:
            return jsonify({"message": "Cliente não encontrado"}), 404
        return jsonify({'id_cliente': cliente.id_cliente, 'nm_cliente': cliente.nm_cliente, 'em_cliente': cliente.em_cliente, 'tf_cliente': cliente.tf_cliente, 'id_banco': cliente.id_banco})
    except Exception as e:
        app.logger.error(f"Erro ao buscar cliente: {str(e)}")
        return jsonify({"error": "Erro ao buscar cliente"}), 500

@app.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    try:
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
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Erro ao atualizar cliente: {str(e)}")
        return jsonify({"error": "Erro ao atualizar cliente"}), 500

@app.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if not cliente:
            return jsonify({"message": "Cliente não encontrado"}), 404

        db.session.delete(cliente)
        db.session.commit()
        return jsonify({"message": "Cliente excluído com sucesso!"})
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Erro ao excluir cliente: {str(e)}")
        return jsonify({"error": "Erro ao excluir cliente"}), 500


# Função principal para rodar a aplicação
if __name__ == '__main__':
    create_database()  # Cria as tabelas no banco de dados
    app.run(host="0.0.0.0", port=8000)

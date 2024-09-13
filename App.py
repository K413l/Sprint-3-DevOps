from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://<username>:<password>@<servername>.database.windows.net/<dbname>?driver=ODBC+Driver+17+for+SQL+Server'
db = SQLAlchemy(app)

# Lembre-se de substituir <username>, <password>, <servername> e <dbname> com as informações do seu SQL Server no Azure.

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Usuário criado com sucesso!"}), 201



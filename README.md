# Sprint-3-DevOps

Deploy de Aplicação Flask com Oracle DB no Azure
Este projeto é uma aplicação Flask que utiliza Oracle DB como banco de dados e é hospedada no Azure utilizando o serviço de App Service para o deploy contínuo via GitHub. O objetivo deste guia é ensinar como configurar todo o ambiente e realizar o deploy da aplicação.

Pré-requisitos
Antes de começar, você precisará:

Conta no Azure
Conta no GitHub
Azure CLI instalada na sua máquina
Python 3.x e pip instalados
Oracle Instant Client instalado
Passo 1: Criar um plano de serviço e grupo de recursos no Azure
Primeiro, você deve criar um grupo de recursos, um plano de serviço para o App Service e um App Service para hospedar sua aplicação.

Script para criar os recursos no Azure
Abra o terminal e execute os seguintes comandos:

bash
Copy code
# 1. Faça login na sua conta Azure
az login

# 2. Crie um grupo de recursos
az group create --name FlaskOracleGroup --location "East US"

# 3. Crie um plano de serviço para o App Service (SKU define o tipo de plano, aqui usamos 'B1' que é a camada básica)
az appservice plan create --name FlaskOraclePlan --resource-group FlaskOracleGroup --sku B1 --is-linux

# 4. Crie o App Service (que hospedará a aplicação)
az webapp create --resource-group FlaskOracleGroup --plan FlaskOraclePlan --name NomeDaSuaAplicacao --runtime "PYTHON|3.9"

# 5. Configure as variáveis de ambiente necessárias para o Oracle DB
az webapp config appsettings set --resource-group FlaskOracleGroup --name NomeDaSuaAplicacao --settings \
    ORACLE_HOST=<seu-host-do-db> \
    ORACLE_PORT=1521 \
    ORACLE_SID=orcl \
    ORACLE_USER=<seu-usuario> \
    ORACLE_PASSWORD=<sua-senha>
Explicação dos comandos:
az login: Faz login na sua conta Azure.
az group create: Cria um grupo de recursos, que agrupa os recursos da sua aplicação.
az appservice plan create: Cria um plano de serviço para o App Service, definindo as especificações de hardware da sua aplicação.
az webapp create: Cria o App Service, onde sua aplicação será hospedada.
az webapp config appsettings set: Configura as variáveis de ambiente do Oracle Database para serem acessadas pela aplicação Flask.

segue os dados JSON para teste:

post TB_BANCOS

[
    {
        "nm_banco": "Banco do Brasil",
        "cd_banco": "001"
    },
    {
        "nm_banco": "Caixa Econômica Federal",
        "cd_banco": "104"
    },
    {
        "nm_banco": "Bradesco",
        "cd_banco": "237"
    },
    {
        "nm_banco": "Itaú Unibanco",
        "cd_banco": "341"
    },
    {
        "nm_banco": "Santander",
        "cd_banco": "033"
    }
]

put TB_BANCO

{
    "nm_banco": "Banco do Brasil Atualizado",
    "cd_banco": "001"
}


post TB_CLIENTE

[
    {
        "nm_cliente": "João Silva",
        "em_cliente": "joao.silva@email.com",
        "tf_cliente": "11999999999",
        "id_banco": 1
    },
    {
        "nm_cliente": "Maria Oliveira",
        "em_cliente": "maria.oliveira@email.com",
        "tf_cliente": "21988888888",
        "id_banco": 2
    },
    {
        "nm_cliente": "Carlos Souza",
        "em_cliente": "carlos.souza@email.com",
        "tf_cliente": "31977777777",
        "id_banco": 3
    },
    {
        "nm_cliente": "Ana Costa",
        "em_cliente": "ana.costa@email.com",
        "tf_cliente": "41966666666",
        "id_banco": 4
    },
    {
        "nm_cliente": "Lucas Pereira",
        "em_cliente": "lucas.pereira@email.com",
        "tf_cliente": "51955555555",
        "id_banco": 5
    }
]

put TB_CLIENTES

{
    "nm_cliente": "João Silva Atualizado",
    "em_cliente": "joao.silva.novo@email.com",
    "tf_cliente": "11998765432",
    "id_banco": 2
}


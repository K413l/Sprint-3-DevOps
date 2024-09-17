# Sprint-3-DevOps
Sprint 3 DevOps

para fazer o passo a passo a seguir será necessário uma conta na Azure




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


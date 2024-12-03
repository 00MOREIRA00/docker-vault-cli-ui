# CLI - (Interface Command Line)

# KV

O KV (Key-Value) é um tipo de engine de secrets no HashiCorp Vault usado para armazenar e gerenciar dados de chave-valor de maneira segura. Ele é um dos engines mais simples e mais comuns no Vault, permitindo armazenar informações sensíveis, como senhas, chaves de API, tokens e outros dados que precisam de proteção.

### Como o KV Funciona no Vault

O KV permite armazenar dados como pares chave-valor, onde cada "chave" é um identificador único e cada "valor" é o dado associado à chave (como uma senha, por exemplo). Esses dados podem ser armazenados em diferentes versões, permitindo que você possa acessar, atualizar e auditar facilmente as mudanças feitas.

O KV é uma forma simples e eficaz de armazenar e gerenciar dados sensíveis de maneira segura dentro do Vault. Ele suporta versionamento, controle de acesso detalhado e operações fáceis para armazenar e acessar dados. O KV v2, com seu suporte a versões, torna o Vault ainda mais poderoso para gerenciar informações que mudam ao longo do tempo, como credenciais e segredos de configuração.

## Comandos Básicos 

* Acessando CLI

```
docker exec -it vault /bin/sh
```

* Saindo do CLI

```
exit
```

* Autenticação: Login do vault usando token

```
vault login <<token>>
```

* Status Vault: Verificando status do Vault

```
vault status
```

* Salvar uma secret: Realiza a criação de uma secret 

```
vault kv put secret/my-secret key1=value1 key2=value2
```

* Ler uma secret: realizar a leitura de uma secret criada

```
vault kv get secret/my-secret
```

* Listar secrets: Listar as secrets criadas em um determinado path

```
vault kv list secret
```

* Apagar uma secret: Realizar deleção de uma secret criada

```
vault kv delete secret/my-secret
```
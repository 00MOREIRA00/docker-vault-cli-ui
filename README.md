# Vault Secrets Manager

Este repositório contém a configuração de um ambiente HashiCorp Vault usando Docker e Docker Compose, além de exemplos para uso da CLI e integração com aplicações Python. O HashiCorp Vault é usado para gerenciar secrets de forma segura, como senhas, tokens de API e chaves criptográficas.s

## Pré-requisitos

Certifique-se de ter instalado no seu sistema:

* Docker
* Docker-Compose
* (Opcional) Vault CLI

## Uso

1. Clone este repositório em sua máquina local:

```
git clone https://github.com/00MOREIRA00/docker-vault-cli-ui.git
```

2. Navegue até o diretório do projeto:
```
cd docker-vault-cli-ui
```

3. Execute o seguinte comando para iniciar os contêineres:
```
docker-compose up -d
```
> Isso iniciará os contêineres em segundo plano (-d).


4. Acesse Vault UI em seu navegador:
    * URL: http://localhost:8200/ui/
        
       * Token: myroot
    
    * CLI: `docker exec -it vault /bin/sh`

5. Token para acesso ao vault é `myroot`.

6. Para parar os contêineres, execute:

```
docker-compose down
```

## Personalização

Você pode modificar as configurações do Vault no arquivo docker-compose.yml conforme necessário, como adicionar volumes, configurar senhas personalizadas etc.

## Avisos

* Não utilize essas configurações em um ambiente de produção sem adequada segurança e configuração.
As credenciais padrão são fornecidas apenas para fins de demonstração. 
* Certifique-se de alterá-las em um ambiente de produção.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar solicitações de pull (pull requests).













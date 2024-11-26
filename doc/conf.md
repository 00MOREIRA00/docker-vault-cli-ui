# Vault 

Para configurar o HashiCorp Vault no Docker e habilitar tanto a interface da linha de comando (CLI) quanto a interface gráfica (UI), você pode seguir as etapas abaixo:

## 1.Pré-requisitos

* Ter o Docker instalado em sua máquina.
* Familiaridade com o uso básico de containers e configuração de redes no Docker.

## 2.Criando Docker Compose 

```
version: '3.8'

services:
  vault:
    image: vault:latest
    container_name: vault
    ports:
      - "8200:8200"
    environment:
      VAULT_DEV_ROOT_TOKEN_ID: "myroot"
      VAULT_DEV_LISTEN_ADDRESS: "0.0.0.0:8200"
      VAULT_ADDR: "http://0.0.0.0:8200"
    volumes:
      - ./vault-data:/vault/file
    command: "server -dev"
```

### Explicação dos Paramêtros 

1. `services.vault:` Define o serviço do Vault.

2. `image: vault:latest:` Usa a imagem oficial do HashiCorp Vault.

3. `ports:` Expõe a porta 8200 no host para acessar o Vault.

4. `environment:` Define variáveis de ambiente

    * `VAULT_DEV_ROOT_TOKEN_ID:` Define o token root para autenticação no modo de desenvolvimento.

    * `VAULT_DEV_LISTEN_ADDRESS:` Configura o Vault para ouvir em todas as interfaces.

    * `VAULT_ADDR:` Define a variável de ambiente necessária para a CLI.

5. `volumes:` Monta um volume local para persistir os dados. A pasta vault-data será criada na mesma localização do arquivo docker-compose.yml.

6. `command:` Executa o Vault no modo de desenvolvimento.

## 3. Usando UI do Vault

* Acessar a url:

```
http://localhost:8200/ui/
```

* Logar com o usuário myroot

## 4. Usando a CLI do Vault

* Digitando o comando

```
docker exec -it vault /bin/sh
```

# Consumindo o Vault com Python

Este guia explica como integrar o Vault com uma aplicação Python, utilizando a biblioteca hvac para consumir segredos armazenados no Vault. Abaixo, detalhamos as etapas de configuração, autenticação e acesso aos segredos.

## Por que escolher o Python?

O Python foi escolhido para essa integração devido à sua simplicidade e ampla adoção em projetos de automação e segurança. A biblioteca hvac permite a comunicação fácil com o Vault, oferecendo recursos como autenticação, leitura e escrita de segredos


## Configuração do Ambiente

### Instalação da Biblioteca

Primeiro, instale a biblioteca hvac. Caso ainda não tenha feito isso, execute o comando:

```
pip install hvac
```

### Configurações do Vault

Em seguida, é necessário configurar as informações do seu Vault, como a URL e o token de autenticação. Para este exemplo, estamos utilizando um Vault local, mas em um ambiente de produção, você deve adaptar essas informações.

```
import hvac

vault_url = "http://127.0.0.1:8200"  
vault_token = "myroot"               
```

### Inicializando o Cliente

Agora, vamos inicializar o cliente hvac com as configurações definidas.

```
# Inicializa o cliente do Vault
client = hvac.Client(url=vault_url, token=vault_token)
```

## Inicializando o Cliente

Agora, vamos inicializar o cliente hvac com as configurações definidas.

```
# Inicializa o cliente do Vault
client = hvac.Client(url=vault_url, token=vault_token)
```

## Verificando a Autenticação

Após a inicialização do cliente, o próximo passo é verificar se a autenticação foi bem-sucedida.

```
# Verificar se a autenticação foi realizada com sucesso
if client.is_authenticated():
    print("Autenticado com sucesso!")
else:
    print("Erro na autenticação.")
    exit()
```

## Acessando o Segredo

Agora que a autenticação foi realizada com sucesso, podemos acessar o segredo armazenado no Vault. Para isso, definimos o caminho da secret que desejamos acessar.

```
# Caminho da secret no Vault
secret_path = "Testando"  # Substitua pelo caminho da sua secret
```

> Nota: O caminho secret/ é implicitamente incluído nas configurações do Vault para a gestão de secrets. Portanto, não é necessário especificá-lo ao acessar secrets no caminho definido.

### Leitura da Secret

Agora, vamos acessar a secret e ler seus dados. Usamos o método read_secret_version para isso.

```
# Acessar e ler o segredo
try:
    secret = client.secrets.kv.read_secret_version(path=secret_path)
    print("Secret encontrada:")
    print(secret['data']['data'])  # Exibe os dados do segredo
except Exception as e:
    print(f"Erro ao acessar a secret: {e}")
```

### Estrutura de Retorno

A resposta retornada pelo Vault tem a seguinte estrutura:

```
{
    "data": {
        "data": {
            "key1": "valor1",
            "key2": "valor2"
        },
        "metadata": {
            "created_time": "2024-11-27T10:00:00.000000Z",
            "version": 1
        }
    }
}
```

> Observação: O segredo real está dentro da chave data, que por sua vez contém os dados reais do segredo sob a chave interna data.

> Portanto, para acessar o conteúdo da secret, extraímos o valor de secret['data']['data'].

## Conclusão

Com essa implementação, conseguimos integrar facilmente uma aplicação Python ao Vault utilizando a biblioteca hvac. Seguindo as etapas acima, conseguimos autenticar, acessar e manipular segredos armazenados no Vault de maneira simples e eficiente.


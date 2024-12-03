import hvac

# Configurações do Vault
vault_url = "http://127.0.0.1:8200"  # URL do Vault
vault_token = "myroot"               # Token de root (ou outro token com permissões)

# Inicializar o cliente
client = hvac.Client(url=vault_url, token=vault_token)

# Verificar se está autenticado
if client.is_authenticated():
    print("Autenticado com sucesso!")
else:
    print("Erro na autenticação.")
    exit()

# Caminho da secret
secret_path = "Testando" # Ajuste para o caminho onde você salvou sua secret

# Acessar a secret
try:
    secret = client.secrets.kv.read_secret_version(path=secret_path)
    print("Secret encontrada:")
    print(secret['data']['data'])  # Dados da secret
except Exception as e:
    print(f"Erro ao acessar a secret: {e}")
import os

from google.cloud import bigquery
from google.cloud import storage
from google.oauth2 import service_account


def create_credentials(credentials_path: str) -> service_account.Credentials:
    """
    Cria o objeto Credentials do Google Service Account.
    Args:
        credentials_path: Nome do arquivo json com as credenciais. Para uso com o Django, enviar no formato
            staticfiles_storage.path(credentials_path).

    Returns: Objeto service_account.Credentials
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_full_path = os.path.join(current_directory, credentials_path)
    try:
        with open(file_full_path, encoding='utf-8'):
            return service_account.Credentials.from_service_account_file(file_full_path)
    except Exception as e:
        raise e


def init_bigquery_client(credentials: service_account.Credentials, project_id: str) -> bigquery.Client:
    """
    Inicializa o cliente do BigQuery.
    Args:
        credentials: Credentials do Google.
        project_id: Id do projeto. Encontrado no console do Google.

    Returns: bigquery.Client
    """
    try:
        return bigquery.Client(credentials=credentials, project=project_id)
    except Exception as e:
        raise e


def init_storage_client(credentials_path: str) -> storage.Client:
    """
    Inicializa o cliente do Storage.
    Args:
        credentials_path: Nome do arquivo json com as credenciais. Para uso com o Django, enviar no formato
            staticfiles_storage.path(credentials_path).

    Returns: storage.Client
    """
    try:
        return storage.Client.from_service_account_json(credentials_path)
    except Exception as e:
        raise e


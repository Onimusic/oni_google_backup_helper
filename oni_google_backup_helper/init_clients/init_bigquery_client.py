from google.cloud import bigquery
from google.oauth2 import service_account


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

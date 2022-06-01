from google.cloud import storage


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

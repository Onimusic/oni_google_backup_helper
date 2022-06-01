from typing import Tuple, List
from google.cloud import storage
from io import StringIO


def backup_to_bucket(
        storage_client: storage.Client,
        bucket_name: str,
        files: List[StringIO],
        file_name_prefix: str
) -> Tuple[bool, list]:
    """ Envia os dados do arquivo csv para o bucket.

    Args:
        storage_client: Cliente do Google Storage
        bucket_name: Nome do bucket no Google
        files: Lista de arquivos csv.
        file_name_prefix: Prefixo do nome para os arquivos csv.

    Returns: Booleano indicando o sucesso da operação e uma lista contendo os nomes dos arquivos enviados.
    """
    file_names = []
    try:
        bucket = storage_client.bucket(bucket_name)
        total_files = len(files)
        for i, file in enumerate(files):
            filename = f'{file_name_prefix}_{i + 1}_of_{total_files}.csv'
            blob = bucket.blob(filename)
            blob.upload_from_string(file.getvalue())
            file_names.append(filename)
        return True, file_names
    except Exception as e:
        raise e

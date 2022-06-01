from typing import List

import google.api_core.exceptions
from google.cloud import bigquery_datatransfer_v1
import time


def backup_to_bigquery(file_names: List[str], bucket_name: str, parent: str, table_name: str, dataset_id: str) -> bool:
    """
    Faz o backup para o bigquery a partir de DataTransfers dos arquivos csv no Google Bucket. Cria DataTransfers com
    nomes no formato: f'{dataset_id}_{table_name}_{filename}', e envia o comando para executá-los imediatamente.
    Args:
        file_names: Lista contendo os nomes dos arquivos no bucket
        bucket_name: Nome do bucket no Google Storages. Ex.: "backups-oni"
        parent: Parent do Data Transfer. Vem no formato ^projects/<project_id>/locations/<location>$
        table_name: Nome da tabela do BigQuery. Ex.: "itens_financeiro"
        dataset_id: Id do dataset do BigQuery. Ex.: "apponi", ou "appeditora"

    Returns: Sucesso da operação
    """
    try:
        transfer_configs_params = {
            "destination_table_name_template": table_name,
            "file_format": "CSV",
            "max_bad_records": "1",
            "ignore_unknown_values": "true",
            "field_delimiter": ",",
            "skip_leading_rows": "1",
            "allow_quoted_newlines": "true",
            "delete_source_files": "false",
        }
        transfer_config = bigquery_datatransfer_v1.TransferConfig()
        transfer_config.destination_dataset_id = dataset_id
        transfer_config.name = transfer_config.display_name
        transfer_config.data_source_id = 'google_cloud_storage'
        transfer_config.schedule_options = {'disable_auto_scheduling': True}
        client = bigquery_datatransfer_v1.DataTransferServiceClient()
        for filename in file_names:
            transfer_config.display_name = f'{dataset_id}_{table_name}_{filename}'
            transfer_configs_params[
                "data_path_template"] = f'gs://{bucket_name}/{filename}'
            transfer_config.params = transfer_configs_params
            request_config = bigquery_datatransfer_v1.CreateTransferConfigRequest(
                parent=parent,
                transfer_config=transfer_config,
            )
            transfer_config_request = client.create_transfer_config(request=request_config)
            run_request_config = bigquery_datatransfer_v1.StartManualTransferRunsRequest()
            run_request_config.parent = transfer_config_request.name
            now = time.time()
            run_request_config.requested_run_time = google.protobuf.timestamp_pb2.Timestamp(seconds=int(now))
            client.start_manual_transfer_runs(run_request_config)
        return True
    except Exception as e:
        raise e

from oni_google_backup_helper.init_clients import init_sqladmin_client


def export_sql_query_as_csv(credentials_path: str, sql_query: str, bucket_path: str, csv_filename: str, project_id: int,
                            db_instance: str, db_name: str) -> str:
    """Realiza a exportação em csv da query desejada enviando o arquivo desejado para o bucket.

    Args:
        credentials_path: caminho da service account com as credenciais.
        sql_query: query sql objeto da exportação.
        bucket_path: caminho completo do bucket do tipo gs://bucket_name/.
        csv_filename: nome do arquivo csv desejado.
        project_id: id do projeto que abriga a instancia sql e o bucket.
        db_instance: instância do banco de dados no google sql
        db_name: nome do banco de dados dentro da instância.

    Returns: resposta retornada pela api.
    """

    sql_client = init_sqladmin_client(credentials_path)
    request_body = {
        "exportContext": {
            "kind": "sql#exportContext",
            "fileType": "CSV",
            "csvExportOptions": {
                "selectQuery": sql_query,
            },
            "uri": f"{bucket_path}{csv_filename}",
            "databases": db_name,
        },
    }
    return sql_client.instances().export(project=project_id,
                                         instance=db_instance,
                                         body=request_body).execute()

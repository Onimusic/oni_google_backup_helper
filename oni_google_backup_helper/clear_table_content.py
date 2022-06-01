from google.cloud import bigquery


def clear_table_content(bigquery_client: bigquery.Client, table_name: str, condition: str = None) -> None:
    """
    Limpa o conteúdo de uma tabela do BigQuery
    Args:
        bigquery_client: Cliente do BigQuery
        table_name: Nome da tabela que vai ser limpa.
        condition: Condicional para apagar os dados. Caso seja nula, limpará toda a tabela.

    Returns: None
    """
    query = f"""
                DELETE FROM `{table_name}`
                WHERE {condition or 'true'};
            """
    bigquery_client.query(query)

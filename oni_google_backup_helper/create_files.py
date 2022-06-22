import csv
from io import StringIO
from math import ceil
from typing import List, Any


def create_split_csv_files(header: List[str], data: List[Any], records_amnt: int, max_records: int) -> List[StringIO]:
    """
    Cria os arquivos csv que serão enviados para backup, fragmentados a cada {max_records} registros.
    Args:
        header: Lista de strings que comporão o cabeçalho do csv.
        data: Dados que serão impressos nas linhas do csv.
        records_amnt: Total de registros. Usualmente é dado por queryset.count().
        max_records: Máximo de registros por arquivo. Usualmente são 500_000.

    Returns: Lista de arquivos no formato StringIO.
    """
    files = []
    for i in range(ceil(records_amnt / max_records)):
        file = StringIO()
        writer = csv.writer(file, dialect='excel', delimiter=',')
        writer.writerow(header)
        for item in data[max_records * i: max_records * (i + 1)]:
            writer.writerow(item)
        files.append(file)
    return files


def create_single_csv_file(header: List[str], data: List[Any]) -> StringIO:
    """
    Cria um arquivo csv que pode ser enviados para backup.
    Args:
        header: Lista de strings que comporão o cabeçalho do csv.
        data: Dados que serão impressos nas linhas do csv.

    Returns: Arquivo no formato StringIO.
    """
    file = StringIO()
    writer = csv.writer(file, dialect='excel', delimiter=',')
    writer.writerow(header)
    for item in data:
        writer.writerow(item)
    return file

# OniDev's Helper Para Backup no Google

Faz upload para o Google Cloud Storage, e usando o DataTransfer, para o BigQuery também.

A documentação completa do pacote está disponível em: [https://onimusic.github.io/oni_google_backup_helper/](https://onimusic.github.io/oni_google_backup_helper/).

Para atualizar a documentação:
- Instale o Sphinx e o Sphinx-napoleon: `pip install Sphinx sphinxcontrib-napoleon`.
- Instale o próprio pacote na venv (caso ainda não esteja instalado) com `pip install .` no diretório raiz.
- Rode o napoleon no diretório base para compilar as docstrings escritas no padrão do Google para o Sphinx (por padrão, o Sphinx só consegue ler docstrings escritas em Re-Structured Text): `sphinx-apidoc -f -o docsrc/source .`.
- No diretório `docsrc/`, rode o comando `make github`. Isso vai gerar os arquivos html e static e enviá-los para a pasta docs, de onde o GitHub Pages puxa para postar no site.

## Como testar sua contribuíção antes de enviar uma PR
Primeiramente faça a desinstalação do pacote presente em sua `venv`.

```bash
pip uninstall oni_google_backup_helper
```

Após a desinstalação, instale o pacote atráves do código fonte modificado.

```bash
pip install -e <path>/oni_google_backup_helper/
```

Teste a implementação feita em um projeto terceiro ou até mesmo usando os códigos de teste disponíveis. Após testar o código atual faça a desinstalação do pacote novamente.

```bash
pip uninstall oni_google_backup_helper
```

Após o teste crie sua PR e envie para avaliação.

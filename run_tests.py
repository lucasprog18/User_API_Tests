import pytest
import datetime
import os

def main():
    # Gera timestamp atual para nomear o relatório de forma única
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Cria a pasta 'reports' caso ainda não exista
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    # Define nome completo do arquivo de relatório com data e hora
    report_file = f"{report_dir}/report_{now}.html"

    # Argumentos para execução do pytest com relatório HTML autônomo
    pytest_args = [
        "tests/",                       
        f"--html={report_file}",       
        "--self-contained-html"       
    ]

    # Executa os testes com os argumentos definidos
    pytest.main(pytest_args)

# ---------------------------------------------
# 🧪 Optional: code coverage using pytest-cov
#
# To measure code coverage, install the package:
#   pip install pytest-cov
#
# Then run:
#   pytest --cov=src tests/
#
# To generate an HTML report:
#   pytest --cov=src --cov-report=html tests/
#   → Opens in /htmlcov/index.html
#
# This helps visualize which lines/files are covered by tests.
# ---------------------------------------------


if __name__ == "__main__":
    main()


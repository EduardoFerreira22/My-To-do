import logging
import inspect
import os
from datetime import datetime

class LogManager:
    def __init__(self, pasta_logs='logs'):
        # Criar o diretório base para logs
        os.makedirs(pasta_logs, exist_ok=True)

        # Definir a data e hora para o nome dos arquivos
        data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Definir os caminhos dos arquivos de log
        info_log_dir = os.path.join(pasta_logs, 'logs_info_warning')
        error_log_dir = os.path.join(pasta_logs, 'logs_errors_log')
        info_log_path = os.path.join(info_log_dir, f'logs_{data_hora}.log')
        error_log_path = os.path.join(error_log_dir, f'logs_{data_hora}.log')

        # Criar os subdiretórios para os logs
        os.makedirs(info_log_dir, exist_ok=True)
        os.makedirs(error_log_dir, exist_ok=True)

        # Configurar o logger
        self.logger = logging.getLogger(f"LogManager_{data_hora}")
        self.logger.setLevel(logging.DEBUG)  # Captura todos os níveis

        # Definir o formato do log
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Handler para INFO e WARNING
        fh_info = logging.FileHandler(info_log_path)
        fh_info.setLevel(logging.INFO)
        fh_info.setFormatter(formatter)

        # Handler para ERROR e EXCEPTION
        fh_error = logging.FileHandler(error_log_path)
        fh_error.setLevel(logging.ERROR)
        fh_error.setFormatter(formatter)

        # Adicionar os handlers ao logger
        self.logger.addHandler(fh_info)
        self.logger.addHandler(fh_error)

    def _get_funcao_origem(self):
        stack = inspect.stack()
        if len(stack) > 2:
            return stack[2].function
        elif len(stack) > 1:
            return stack[1].function
        else:
            return "__main__"

    def info(self, mensagem: str):
        origem = self._get_funcao_origem()
        self.logger.info(f"[{origem}] {mensagem}")

    def aviso(self, mensagem: str):
        origem = self._get_funcao_origem()
        self.logger.warning(f"[{origem}] {mensagem}")

    def erro(self, mensagem: str):
        origem = self._get_funcao_origem()
        self.logger.error(f"[{origem}] {mensagem}")

    def excecao(self, mensagem: str):
        origem = self._get_funcao_origem()
        self.logger.exception(f"[{origem}] {mensagem}")  # Imprime traceback completo
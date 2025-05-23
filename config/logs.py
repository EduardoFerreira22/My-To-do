import logging
import inspect
import os
from datetime import datetime

class LogManager:
    def __init__(self, pasta_logs='logs'):
        os.makedirs(pasta_logs, exist_ok=True)

        data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        info_log_path = os.path.join(pasta_logs, f'logs_info_warning/logs_{data_hora}.log')
        error_log_path = os.path.join(pasta_logs, f'logs_errors_log/logs_{data_hora}.log')

        self.logger = logging.getLogger(f"LogManager_{data_hora}")
        self.logger.setLevel(logging.DEBUG)  # captura todos os níveis

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # INFO / WARNING
        fh_info = logging.FileHandler(info_log_path)
        fh_info.setLevel(logging.INFO)
        fh_info.setFormatter(formatter)

        # ERROR / EXCEPTION
        fh_error = logging.FileHandler(error_log_path)
        fh_error.setLevel(logging.ERROR)
        fh_error.setFormatter(formatter)

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
        self.logger.exception(f"[{origem}] {mensagem}")  # imprime traceback completo

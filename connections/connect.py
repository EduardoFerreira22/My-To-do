import sqlite3
from config import configuracoes as cfg
from config.logs import LogManager


logger = LogManager()


class DBConnect:
    def __init__(self, path):
        self.cursor = None
        self.conn = None
        self.path = path

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.path)
            self.cursor = self.conn.cursor()
            logger.info(f'Conexão com o banco {self.path} estabelecida com sucesso.')
        except Exception as e:
            logger.excecao(f'Erro ao conectar ao banco de dados: {e}')
            cfg.show_popup('erro', 'Erro de Conexão', str(e))

    def close_connect(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
            logger.info('Conexão com o banco de dados encerrada.')
        except Exception as e:
            logger.erro(f'Erro ao encerrar conexão: {e}')

    def create_tables(self):
        try:
            self.connect()
            query = cfg.read_querys()
            if isinstance(query, list):
                query = "".join(query)
            
            self.cursor.executescript(query)
            self.conn.commit()
            self.close_connect()
            logger.info('Tabelas do sistema criadas com sucesso.')
            
            # cfg.show_popup('sucesso', 'Tabelas Criadas', 'As tabelas foram criadas com sucesso.')
            
        except Exception as e:
            logger.excecao(f"Erro ao criar as tabelas do sistema {e}")
            # cfg.show_popup('erro', 'Erro ao Criar Tabelas', f'{e}')

    def select_tasks(self):
        ...

    def select_categorias(self):
        ...

    def insert_categorias(self, categoria=str, cor=str):
        try:
            self.connect()
            query = "INSERT INTO CATEGORIAS(CATEGORIA, COR) VALUES (?, ?)"           
            self.cursor.execute(query, (categoria, cor))
            self.conn.commit()
            self.close_connect()
            logger.info(f'Categoria{categoria} criada com sucesso.')
            cfg.show_popup(tipo="sucesso", titulo="Sucesso!", mensagem="f'Categoria{categoria} criada com sucesso.'")
            # cfg.show_popup('sucesso', 'Tabelas Criadas', 'As tabelas foram criadas com sucesso.')
        except Exception as e:
            logger.excecao(f"Erro ao criar uma nova categoria {e}")
            cfg.show_popup(tipo="erro",titulo="Erro!" ,mensagem=f"Erro ao criar uma nova categoria {e}")
            # cfg.show_popup('erro', 'Erro ao Criar Tabelas', f'{e}')

    def insert_tasks(self):
        ...

    def update_tasks(self):
        ...
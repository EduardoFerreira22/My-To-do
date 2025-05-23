from PySide6.QtWidgets import QMessageBox




def show_popup(tipo: str, titulo: str, mensagem: str):
    """
    Exibe uma mensagem de popup (erro, sucesso, informação ou aviso).

    :param tipo: 'erro', 'sucesso', 'info' ou 'aviso'
    :param titulo: Título da janela
    :param mensagem: Texto da mensagem
    :param parent: Referência opcional à janela principal (self, por exemplo)
    """
    msg_box = QMessageBox()
    msg_box.setWindowTitle(titulo)
    msg_box.setText(mensagem)

    if tipo == 'erro':
        msg_box.setIcon(QMessageBox.Critical)
    elif tipo == 'sucesso':
        msg_box.setIcon(QMessageBox.Information)
    elif tipo == 'info':
        msg_box.setIcon(QMessageBox.Information)
    elif tipo == 'aviso':
        msg_box.setIcon(QMessageBox.Warning)
    else:
        msg_box.setIcon(QMessageBox.NoIcon)

    msg_box.exec()


def read_querys():
    path = "Data/data.txt"
    try:
        with open(path, "r", encoding='utf-8') as file:
            query = file.read()
            print(query)
        return query
    except Exception as e:
        show_popup(
            tipo='erro',
            titulo='Erro de leitura',
            mensagem=f'Não foi possível ler o arquivo {e}',
            parent=None
            )


read_querys()
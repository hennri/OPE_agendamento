from model.relatorio import ItemRelatorio

def relatorio():
    from services.cliente_service import localizar as localizar_cliente

    resultado = []

    for sm in listar_s_matriculas():
        cliente = localizar_cliente(sm.id)
        item = ItemRelatorio(cliente.nome)
        resultado.append(item)
    return resultado
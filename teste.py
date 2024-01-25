import os

caminho = 'W://Pessoal//EmpresasSemOcorrenciasFolhaAutomatica//Automação Folha//Configuração 0018 - FR//2024//Automação Folha//Configuração 0018//012024'
nome_pasta = os.listdir(caminho)

# Fiz um obj com todos
mapeamento = {
    'Recibo': 'RECIBO DCTFWEB.pdf',
    'DeclaracaoCompleta': 'DECLARACAO COMPLETA.pdf',
    'GuiaPagamento': 'DARF FEDERAL.pdf',
    'Demonstrativo': 'DEMONSTRATIVO INSS.pdf',
    'Envelope': 'RECIBOS DE SALÁRIO.pdf',
    'quidos': 'LIQUIDOS DE CALCULO.pdf',
    'Geral': 'RESUMO GERAL.pdf',
    'IRRF': 'RELACAO IRRF.pdf'
}

def renomear_arquivo(caminho_novo, file_name, novo_nome):
    old_path = os.path.join(caminho_novo, file_name)
    new_path = os.path.join(caminho_novo, novo_nome)
    os.rename(old_path, new_path)

for pastaempresa in nome_pasta:
    caminho_novo = os.path.join(caminho, pastaempresa)
    
    for file_name in os.listdir(caminho_novo):
        for padrao, novo_nome in mapeamento.items():
            if padrao in file_name:
                renomear_arquivo(caminho_novo, file_name, novo_nome)
                break  # Se o padrão é encontrado, não é necessário verificar os outros 

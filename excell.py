import xlwt

# Criar um novo workbook e adicionar uma planilha
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Planilha1')

# Definir largura máxima para cada coluna
largura_maxima = {
    'titulo': 50,
    'problema': 50,
    'orientacao': 50
}

# Exemplo de dados
dados = [
    {'titulo': 'Título muito grande que ultrapassa a largura máxima da coluna', 
     'problema': 'Problema muito longo que excede o limite da coluna', 
     'orientacao': 'Orientação extensa que precisa ser ajustada'},
    {'titulo': 'Título curto', 
     'problema': 'Problema curto', 
     'orientacao': 'Orientação breve'}
]

# Definir estilos para células (pode ajustar conforme necessário)
style = xlwt.XFStyle()
alignment = xlwt.Alignment()
alignment.wrap = 1  # Habilitar o wrapping de texto
style.alignment = alignment

# Escrever dados na planilha
for i, campo in enumerate(['titulo', 'problema', 'orientacao']):
    # Definir largura da coluna
    largura = min(len(max((d[campo] for d in dados), key=len)), largura_maxima[campo])
    sheet.col(i).width = 256 * largura  # A largura é definida em unidades de 1/256 do tamanho do caractere padrão
    
    # Escrever cabeçalhos
    sheet.write(0, i, campo.capitalize(), style=style)

    # Escrever dados
    for j, linha in enumerate(dados):
        sheet.write(j + 1, i, linha[campo], style=style)

# Salvar o workbook
workbook.save('planilha.xls')

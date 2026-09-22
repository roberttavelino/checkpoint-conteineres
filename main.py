"""Controle procedural de ocupação de um pátio logístico com Tkinter."""

import tkinter as tk
from tkinter import messagebox, ttk


# Constantes do cenário: cinco linhas por seis colunas formam trinta posições.
LINHAS = 5
COLUNAS = 6
TOTAL_POSICOES = LINHAS * COLUNAS

# Matriz de negócio: 0 indica livre e 1 indica ocupada.
ocupacao = [[0 for coluna in range(COLUNAS)] for linha in range(LINHAS)]
# Matriz paralela: guarda a identificação apenas onde existe contêiner.
identificacoes = [["" for coluna in range(COLUNAS)] for linha in range(LINHAS)]

janela = None
codigo_var = None
texto_ocupadas = None
texto_livres = None
texto_chegadas = None
botoes = []
total_chegadas = 0


def codigo_da_posicao(linha, coluna):
    """Converte índices internos em rótulos como A1, B3 e E6."""
    # chr() converte o código numérico em letra; evita uma tabela manual de rótulos.
    return chr(65 + linha) + str(coluna + 1)


def contar_ocupadas():
    """Conta os valores 1 percorrendo toda a matriz."""
    total = 0
    # Repetição: cada posição é visitada para manter a contagem derivada do estado real.
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if ocupacao[linha][coluna] == 1:
                total = total + 1
    return total


def codigo_ja_registrado(codigo):
    """Verifica se a identificação já aparece na matriz paralela."""
    encontrado = False
    # Repetição e seleção substituem uma busca pronta e deixam o algoritmo visível.
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if identificacoes[linha][coluna] == codigo:
                encontrado = True
    return encontrado


def atualizar_botao(linha, coluna):
    """Atualiza a representação visual conforme o valor 0 ou 1 da matriz."""
    posicao = codigo_da_posicao(linha, coluna)
    # Seleção: o texto acompanha diretamente o estado armazenado.
    if ocupacao[linha][coluna] == 1:
        texto = posicao + "\nOCUPADA\n" + identificacoes[linha][coluna]
        botoes[linha][coluna].configure(text=texto, style="Ocupada.TButton")
    else:
        botoes[linha][coluna].configure(text=posicao + "\nLIVRE", style="Livre.TButton")


def atualizar_resumo():
    """Atualiza os indicadores mostrados em tempo real."""
    ocupadas = contar_ocupadas()
    livres = TOTAL_POSICOES - ocupadas
    # set() atualiza a variável observada pelas Labels sem reescrever cada widget.
    texto_ocupadas.set("Posições ocupadas: " + str(ocupadas))
    texto_livres.set("Posições livres: " + str(livres))
    texto_chegadas.set("Chegadas registradas: " + str(total_chegadas))


def registrar_chegada(linha, coluna):
    """Valida a identificação e registra a chegada em uma vaga livre."""
    global total_chegadas
    # get() lê o Entry; strip() remove espaços e upper() padroniza letras.
    codigo = codigo_var.get().strip().upper()
    # Seleção: rejeita entrada vazia antes de alterar as matrizes.
    if codigo == "":
        messagebox.showwarning("Código obrigatório", "Digite uma identificação antes de escolher a vaga.", parent=janela)
        return
    # Seleção: impede que o mesmo contêiner seja armazenado duas vezes.
    if codigo_ja_registrado(codigo):
        messagebox.showwarning("Contêiner duplicado", "Essa identificação já está no pátio.", parent=janela)
        return
    # Sequência: as duas matrizes e o contador são atualizados juntos.
    ocupacao[linha][coluna] = 1
    identificacoes[linha][coluna] = codigo
    total_chegadas = total_chegadas + 1
    # set("") limpa o campo para o próximo registro.
    codigo_var.set("")
    atualizar_botao(linha, coluna)
    atualizar_resumo()


def registrar_saida(linha, coluna):
    """Confirma a saída e libera a posição ocupada."""
    posicao = codigo_da_posicao(linha, coluna)
    codigo = identificacoes[linha][coluna]
    # askyesno() cria a decisão booleana que substitui uma leitura manual de confirmação.
    confirmar = messagebox.askyesno("Registrar saída", "Confirmar a saída de " + codigo + " da posição " + posicao + "?", parent=janela)
    # Seleção: apenas Sim altera o estado da matriz.
    if confirmar:
        ocupacao[linha][coluna] = 0
        identificacoes[linha][coluna] = ""
        atualizar_botao(linha, coluna)
        atualizar_resumo()


def clicar_posicao(linha, coluna):
    """Direciona o clique para chegada ou saída conforme o valor da matriz."""
    # Seleção: 0 chama chegada; 1 chama saída.
    if ocupacao[linha][coluna] == 0:
        registrar_chegada(linha, coluna)
    else:
        registrar_saida(linha, coluna)


def criar_acao_da_posicao(linha, coluna):
    """Cria o comando de cada botão preservando seus índices."""
    def acao():
        clicar_posicao(linha, coluna)
    return acao


def montar_interface():
    """Monta a interface nativa usando ttk, grid e pack."""
    global botoes
    global texto_ocupadas, texto_livres, texto_chegadas

    estilo = ttk.Style()
    # theme_use() consulta o tema nativo disponível antes de configurar os estilos.
    estilo.theme_use(estilo.theme_use())
    estilo.configure("Titulo.TLabel", font=("Segoe UI", 16, "bold"))
    estilo.configure("Livre.TButton", padding=(8, 12))
    estilo.configure("Ocupada.TButton", padding=(8, 12))

    principal = ttk.Frame(janela, padding=16)
    # pack() encaixa o quadro principal e permite expansão.
    principal.pack(fill="both", expand=True)
    principal.columnconfigure(0, weight=1)
    principal.rowconfigure(4, weight=1)

    ttk.Label(principal, text="Controle de Contêineres", style="Titulo.TLabel").grid(row=0, column=0, sticky="w")
    ttk.Label(principal, text="Matriz 5 x 6: clique em vaga livre para chegada e em vaga ocupada para saída.").grid(row=1, column=0, sticky="w", pady=(3, 14))

    entrada = ttk.LabelFrame(principal, text="Registro de chegada", padding=10)
    entrada.grid(row=2, column=0, sticky="ew", pady=(0, 12))
    entrada.columnconfigure(1, weight=1)
    ttk.Label(entrada, text="Identificação do contêiner:").grid(row=0, column=0, sticky="w", padx=(0, 8))
    ttk.Entry(entrada, textvariable=codigo_var, width=32).grid(row=0, column=1, sticky="ew")

    resumo = ttk.Frame(principal)
    resumo.grid(row=3, column=0, sticky="w", pady=(0, 12))
    ttk.Label(resumo, textvariable=texto_ocupadas).grid(row=0, column=0, padx=(0, 18))
    ttk.Label(resumo, textvariable=texto_livres).grid(row=0, column=1, padx=(0, 18))
    ttk.Label(resumo, textvariable=texto_chegadas).grid(row=0, column=2)

    patio = ttk.LabelFrame(principal, text="Pátio de armazenamento", padding=10)
    patio.grid(row=4, column=0, sticky="nsew")
    # Repetição: cria exatamente os trinta botões correspondentes à matriz.
    for coluna in range(COLUNAS):
        patio.columnconfigure(coluna, weight=1)
    for linha in range(LINHAS):
        patio.rowconfigure(linha, weight=1)
        linha_botoes = []
        for coluna in range(COLUNAS):
            botao = ttk.Button(patio, text=codigo_da_posicao(linha, coluna) + "\nLIVRE", style="Livre.TButton", command=criar_acao_da_posicao(linha, coluna))
            # grid() alinha a posição visual com os mesmos índices da matriz.
            botao.grid(row=linha, column=coluna, sticky="nsew", padx=4, pady=4)
            # append() adiciona o botão ao fim da linha, evitando índices manuais.
            linha_botoes.append(botao)
        botoes.append(linha_botoes)

    acoes = ttk.Frame(principal)
    acoes.grid(row=5, column=0, sticky="e", pady=(12, 0))
    ttk.Button(acoes, text="Encerrar e mostrar resumo", command=encerrar).grid(row=0, column=0)


def montar_lista_de_ocupacao():
    """Monta a lista textual de contêineres que permaneceram no pátio."""
    lista = ""
    encontrou = False
    # Repetição: percorre as trinta células e seleciona as ocupadas.
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if ocupacao[linha][coluna] == 1:
                encontrou = True
                lista = lista + "\n- " + codigo_da_posicao(linha, coluna) + ": " + identificacoes[linha][coluna]
    if encontrou:
        return lista
    return "\nNenhum contêiner permaneceu armazenado."


def encerrar():
    """Exibe o resumo final obrigatório e fecha a janela."""
    ocupadas = contar_ocupadas()
    livres = TOTAL_POSICOES - ocupadas
    mensagem = ("Resumo final do período\n\n" + "Posições ocupadas: " + str(ocupadas) + "\n" + "Posições livres: " + str(livres) + "\n" + "Chegadas registradas: " + str(total_chegadas) + "\n\nContêineres no pátio:" + montar_lista_de_ocupacao())
    # showinfo() apresenta o resumo em uma caixa modal antes do encerramento.
    messagebox.showinfo("Resumo final", mensagem, parent=janela)
    # destroy() encerra a janela criada pelo Tkinter.
    janela.destroy()


def iniciar_aplicacao():
    """Executa a sequência principal e inicia o laço de eventos."""
    global janela, codigo_var, texto_ocupadas, texto_livres, texto_chegadas
    # Sequência: cria a janela e as variáveis observáveis antes da interface.
    janela = tk.Tk()
    janela.title("Controle de Contêineres")
    janela.minsize(760, 560)
    # StringVar() permite que Entry e Labels compartilhem estado textual observável.
    codigo_var = tk.StringVar()
    texto_ocupadas = tk.StringVar()
    texto_livres = tk.StringVar()
    texto_chegadas = tk.StringVar()
    montar_interface()
    atualizar_resumo()
    # mainloop() mantém a aplicação aguardando eventos de clique e teclado.
    janela.mainloop()


if __name__ == "__main__":
    iniciar_aplicacao()

import tkinter as tk
from tkinter import ttk
from conversao import converter, get_historico
from taxas import TAXAS_CONVERSAO

def home():
    janela = tk.Tk()
    janela.title("Conversor de Moedas")
    janela.geometry("600x500")
    janela.resizable(False, False)

    frame_central = tk.Frame(janela)
    frame_central.place(relx=0.5, rely=0.5, anchor="center")

    titulo = tk.Label(frame_central, text="Conversor de Moedas", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    label_valor = tk.Label(frame_central, text="Insira o valor:", font=("Arial", 12))
    label_valor.pack(pady=5)

    entrada_valor = tk.Entry(frame_central, font=("Arial", 12), justify="center")
    entrada_valor.pack(pady=5)

    label_opcoes = tk.Label(frame_central, text="Selecione a conversão:", font=("Arial", 12))
    label_opcoes.pack(pady=5)

    opcao = tk.StringVar()
    opcoes_menu = ttk.Combobox(
        frame_central,
        textvariable=opcao,
        values=list(TAXAS_CONVERSAO.keys()),
        state="readonly",
        font=("Arial", 12)
    )
    opcoes_menu.pack(pady=5)
    opcoes_menu.set("Selecione a conversão")

    label_resultado = tk.Label(frame_central, text="", font=("Arial", 14, "bold"))
    label_resultado.pack(pady=10)

    # Insira aqui o rótulo e lista para exibir o histórico de conversões realizadas
    label_historico = tk.Label(frame_central, text="Histórico de Conversões:", font=("Arial", 12, "bold"))
    label_historico.pack(pady=5)

    listbox_historico = tk.Listbox(frame_central, height=5, width=50, font=("Arial", 10), selectmode="single")
    listbox_historico.pack(pady=5)

    def acao_converter():
        valor_digitado = entrada_valor.get()
        opcao_selecionada = opcao.get()

        if not valor_digitado:
            label_resultado["text"] = "Erro: Insira um valor numérico!"
            return

        try:
            valor = float(valor_digitado)
            resultado = converter(valor, opcao_selecionada)
            label_resultado["text"] = resultado

            # Insira aqui o código para adicionar a conversão realizada no histórico
            listbox_historico.delete(0, tk.END)
            for item in get_historico():
                listbox_historico.insert(0, item)

        except ValueError:
            label_resultado["text"] = "Erro: Insira um número válido."

    def acao_limpar():
        entrada_valor.delete(0, tk.END)
        opcoes_menu.set("Selecione a conversão")
        label_resultado["text"] = ""

    botao_converter = tk.Button(frame_central, text="Converter", command=acao_converter)
    botao_converter.pack(pady=10)

    botao_limpar = tk.Button(frame_central, text="Limpar", command=acao_limpar)
    botao_limpar.pack(pady=5)

    rodape = tk.Label(
        janela, 
        text="Desenvolvido por: Ademar Castro, Carlos Alexandre, Lucas Cauã e Lucas Eduardo.", 
        font=("Arial", 10)
    )
    rodape.pack(side="bottom", pady=10)

    janela.mainloop()
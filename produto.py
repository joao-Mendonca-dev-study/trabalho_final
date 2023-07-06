import tkinter as tk
from tkinter import END, messagebox
import os.path
import pickle


class Produto:
    def __init__(self, codNum, descricao, precoCompra, valorVenda, quantEstoq):
        self.__codNum = codNum
        self.__descricao = descricao
        self.__precoCompra = precoCompra
        self.__valorVenda = valorVenda
        self.__quantEstoq = quantEstoq

    @property
    def codNum(self):
        return self.__codNum

    @property
    def descricao(self):
        return self.__descricao

    @property
    def precoCompra(self):
        return self.__precoCompra

    @property
    def valorVenda(self):
        return self.__valorVenda

    @property
    def quantEstoq(self):
        return self.__quantEstoq

    @quantEstoq.setter
    def quantEstoq(self, quant):
        self.__quantEstoq = quant

    def getProduto(self, codigo):
        for gm in self.listaProdutos:
            if gm.codNum == codigo:
                return gm
        return None


class LimiteCadastraProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("250x200")
        self.title("Cadastrar Produto")
        self.controle = controle

        self.frameCodNum = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.framePrecoCompra = tk.Frame(self)
        self.frameValorVenda = tk.Frame(self)
        self.frameQuantEstoq = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodNum.pack()
        self.frameDescricao.pack()
        self.framePrecoCompra.pack()
        self.frameValorVenda.pack()
        self.frameQuantEstoq.pack()
        self.frameButton.pack()

        self.labelCodNum = tk.Label(self.frameCodNum, text="Código")
        self.labelDescricao = tk.Label(self.frameDescricao, text="Descricao ")
        self.labelPrecoCompra = tk.Label(self.framePrecoCompra, text="Custo: ")
        self.labelValorVenda = tk.Label(self.frameValorVenda, text="Valor: ")
        self.labelQuantEstoq = tk.Label(self.frameQuantEstoq, text="Quantidade: ")
        self.labelCodNum.pack(side="left")
        self.labelDescricao.pack(side="left")
        self.labelPrecoCompra.pack(side="left")
        self.labelValorVenda.pack(side="left")
        self.labelQuantEstoq.pack(side="left")

        self.inputCodNum = tk.Entry(self.frameCodNum, width=10)
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20)
        self.inputPrecoCompra = tk.Entry(self.framePrecoCompra, width=20)
        self.inputValorVenda = tk.Entry(self.frameValorVenda, width=15)
        self.inputQuantEstoq = tk.Entry(self.frameQuantEstoq, width=20)
        self.inputCodNum.pack(side="left")
        self.inputDescricao.pack(side="left")
        self.inputPrecoCompra.pack(side="left")
        self.inputValorVenda.pack(side="left")
        self.inputQuantEstoq.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteMostraProdutos:
    def __init__(self, str):
        messagebox.showinfo("Produtos em estoque: ", str)


class LimiteMostraFatura(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("250x200")
        self.title("Consultar Produto")
        self.controle = controle

        self.frameCodNum = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodNum.pack()
        self.frameButton.pack()

        self.labelCodNum = tk.Label(self.frameCodNum, text="Digite o código do produto")
        self.labelCodNum.pack(side="left")

        self.inputCodNum = tk.Entry(self.frameCodNum, width=10)
        self.inputCodNum.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaFaturamentoEnter)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerFaturamento)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteConsultaProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("250x200")
        self.title("Consultar Produto")
        self.controle = controle

        self.frameCodNum = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.framePrecoCompra = tk.Frame(self)
        self.frameValorVenda = tk.Frame(self)
        self.frameQuantEstoq = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodNum.pack()
        self.frameDescricao.pack()
        self.framePrecoCompra.pack()
        self.frameValorVenda.pack()
        self.frameQuantEstoq.pack()
        self.frameButton.pack()

        self.labelCodNum = tk.Label(self.frameCodNum, text="Código")
        self.labelDescricao = tk.Label(self.frameDescricao, text="Descricao ")
        self.labelPrecoCompra = tk.Label(self.framePrecoCompra, text="Custo: ")
        self.labelValorVenda = tk.Label(self.frameValorVenda, text="Valor: ")
        self.labelQuantEstoq = tk.Label(self.frameQuantEstoq, text="Quantidade: ")
        self.labelCodNum.pack(side="left")
        self.labelDescricao.pack(side="left")
        self.labelPrecoCompra.pack(side="left")
        self.labelValorVenda.pack(side="left")
        self.labelQuantEstoq.pack(side="left")

        self.inputCodNum = tk.Entry(self.frameCodNum, width=10)
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20, state="readonly")
        self.inputPrecoCompra = tk.Entry(
            self.framePrecoCompra, width=20, state="readonly"
        )
        self.inputValorVenda = tk.Entry(
            self.frameValorVenda, width=15, state="readonly"
        )
        self.inputQuantEstoq = tk.Entry(
            self.frameQuantEstoq, width=20, state="readonly"
        )
        self.inputCodNum.pack(side="left")
        self.inputDescricao.pack(side="left")
        self.inputPrecoCompra.pack(side="left")
        self.inputValorVenda.pack(side="left")
        self.inputQuantEstoq.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ControlProduto:
    def __init__(self, controlador):
        self.controlador = controlador
        self.listaProdutos = []
        self.listaNF = []
        if not os.path.isfile("Produtos.pickle"):
            self.listaProdutos = []
        else:
            with open("Produtos.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)

    def salvaProduto(self):
        with open("Produtos.pickle", "wb") as f:
            pickle.dump(self.listaProdutos, f)

    def getProduto(self, codigo):
        for pd in self.listaProdutos:
            if pd.codNum == codigo:
                return pd
        return None

    def getProdutoDesc(self, descricao):
        for pd in self.listaProdutos:
            if pd.descricao == descricao:
                return pd
        return None

    def cadastraProduto(self):
        self.limiteCadastra = LimiteCadastraProduto(self)

    # codNum, descricao, precoCompra, valorVenda, quantEstoq
    def enterHandler(self, event):
        self.atualizaListaProdutos()

        codNum = int(self.limiteCadastra.inputCodNum.get())
        descricao = self.limiteCadastra.inputDescricao.get()
        precoCompra = int(self.limiteCadastra.inputPrecoCompra.get())
        valorVenda = int(self.limiteCadastra.inputValorVenda.get())
        quantEstoq = int(self.limiteCadastra.inputQuantEstoq.get())

        try:
            produto = self.getProduto(codNum)
            if produto:
                produto.quantEstoq += quantEstoq
                self.limiteCadastra.mostraJanela("Sucesso", "Quantidade alterada")
                self.salvaProduto()
            else:
                produto = Produto(
                    codNum, descricao, precoCompra, valorVenda, quantEstoq
                )
                self.listaProdutos.append(produto)
                self.salvaProduto()
                self.limiteCadastra.mostraJanela(
                    "Sucesso", "Produto cadastrado com sucesso"
                )
                self.atualizaListaProdutos()
                self.clearHandler(event)
        except ValueError as error:
            self.limiteCadastra.mostraJanela("Erro", "error")

    def consultaHandler(self, event):
        self.atualizaListaProdutos()
        codNum = int(self.limiteConsulta.inputCodNum.get())

        try:
            produto = self.getProduto(codNum)
            if produto:
                self.limiteConsulta.inputDescricao.config(state="normal")
                self.limiteConsulta.inputDescricao.delete(0, END)
                self.limiteConsulta.inputDescricao.insert(0, produto.descricao)
                self.limiteConsulta.inputDescricao.config(state="readonly")

                self.limiteConsulta.inputPrecoCompra.config(state="normal")
                self.limiteConsulta.inputPrecoCompra.delete(0, END)
                self.limiteConsulta.inputPrecoCompra.insert(0, produto.precoCompra)
                self.limiteConsulta.inputPrecoCompra.config(state="readonly")

                self.limiteConsulta.inputValorVenda.config(state="normal")
                self.limiteConsulta.inputValorVenda.delete(0, END)
                self.limiteConsulta.inputValorVenda.insert(0, produto.valorVenda)
                self.limiteConsulta.inputValorVenda.config(state="readonly")

                self.limiteConsulta.inputQuantEstoq.config(state="normal")
                self.limiteConsulta.inputQuantEstoq.delete(0, END)
                self.limiteConsulta.inputQuantEstoq.insert(0, produto.quantEstoq)
                self.limiteConsulta.inputQuantEstoq.config(state="readonly")

                self.atualizaListaProdutos()
                # self.clearHandler(event)
            else:
                self.limiteConsulta.mostraJanela("Falha", "Produto nao cadastrado")
                self.atualizaListaProdutos()
                # self.clearHandler(event)
        except ValueError as error:
            self.limiteConsulta.mostraJanela("Erro", "error")

    def clearHandler(self, event):
        self.limiteCadastra.inputCodNum.delete(
            0, len(self.limiteCadastra.inputCodNum.get())
        )
        self.limiteCadastra.inputDescricao.delete(
            0, len(self.limiteCadastra.inputDescricao.get())
        )
        self.limiteCadastra.inputPrecoCompra.delete(
            0, len(self.limiteCadastra.inputPrecoCompra.get())
        )
        self.limiteCadastra.inputValorVenda.delete(
            0, len(self.limiteCadastra.inputValorVenda.get())
        )
        self.limiteCadastra.inputQuantEstoq.delete(
            0, len(self.limiteCadastra.inputQuantEstoq.get())
        )

    def fechaHandler(self, event):
        self.limiteCadastra.destroy()

    def mostraProdutos(self):
        self.atualizaListaProdutos()
        strTexto = "Código -- Descrição  --  Quantidade\n"
        for prod in self.listaProdutos:
            strTexto += (
                str(prod.codNum)
                + " -- "
                + prod.descricao
                + " -- "
                + str(prod.quantEstoq)
                + "\n"
            )
        self.limiteLista = LimiteMostraProdutos(strTexto)

    def atualizaListaProdutos(self):
        if not os.path.isfile("Produtos.pickle"):
            self.listaProdutos = []
        else:
            with open("Produtos.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)

    def atualizaListaNf(self):
        if not os.path.isfile("NotaFiscal.pickle"):
            self.listaNF = []
        else:
            with open("NotaFiscal.pickle", "rb") as f:
                self.listaNF = pickle.load(f)

    def limpaEstoque(self):
        self.limiteCadastra = LimiteCadastraProduto(self)
        if os.path.isfile("Produtos.pickle"):
            os.remove("Produtos.pickle")
            self.limiteCadastra.mostraJanela("Sucesso", "Estoque apagado")
        else:
            self.limiteCadastra.mostraJanela(
                "Atenção", "Não existe estoque para apagar"
            )
        self.atualizaListaProdutos()

    def consultaProduto(self):
        self.limiteConsulta = LimiteConsultaProduto(self)

    def mostraFaturamento(self):
        self.limiteConsultaFaturamento = LimiteMostraFatura(self)

    def consultaFaturamentoEnter(self, event):
        codigo = int(self.limiteConsultaFaturamento.inputCodNum.get())

        self.atualizaListaNf()
        for nf in self.listaNF:
            total = 0
            if nf.idProduto == codigo:
                total += nf.quantidade
            valor = 0
            for prod in self.listaProdutos:
                if prod.codNum == codigo:
                    valor = prod.valorVenda * total

        self.limiteConsultaFaturamento.mostraJanela(
            "Valor do faturamento", "R$" + str(valor)
        )

    def fechaHandlerFaturamento(self, event):
        self.limiteConsultaFaturamento.destroy()

import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
from tkinter import ttk
import cliente as cl
import produto as pd
import datetime


class NotaFiscal:
    def __init__(self, idNota, idProduto, idCliente, dataEmissao, quantidade):
        self.__idNota = idNota
        self.__idProduto = idProduto
        self.__idCliente = idCliente
        self.__dataEmissao = dataEmissao
        self.__quantidade = quantidade

    @property
    def idNota(self):
        return self.__idNota

    @property
    def idProduto(self):
        return self.__idProduto

    @property
    def idCliente(self):
        return self.__idCliente

    @property
    def dataEmissao(self):
        return self.__dataEmissao

    @property
    def quantidade(self):
        return self.__quantidade


class LimiteNotaFiscal(tk.Toplevel):
    def __init__(self, controle, listaProdutos, listaCliente):
        tk.Toplevel.__init__(self)
        self.geometry("300x400")
        self.title("Gerar Nota Fiscal de Venda")
        self.controle = controle
        self.listaProdutos = listaProdutos

        self.frameNumNota = tk.Frame(self)
        self.frameCpfCliente = tk.Frame(self)
        self.frameListBox = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameFechaNota = tk.Frame(self)
        self.frameData = tk.Frame(self)

        self.frameNumNota.pack()
        self.frameData.pack()
        self.frameCpfCliente.pack()
        self.frameListBox.pack()
        self.frameButton.pack()
        self.frameCpfCliente.pack()
        self.frameFechaNota.pack()

        self.labelNumNota = tk.Label(self.frameNumNota, text="Número da Nota")
        self.labelNumNota.pack(side="left")
        self.inputNumNotaInput = tk.Entry(self.frameNumNota, width=11)
        self.inputNumNotaInput.pack(side="left")

        self.labelData = tk.Label(self.frameData, text="Escolha a data formato: dd/mm")
        self.labelData.pack(side="left")
        self.inputDataNota = tk.Entry(self.frameData, width=11)
        self.inputDataNota.pack(side="left")

        self.labelCpfCliente = tk.Label(self.frameCpfCliente, text="Cpf do Cliente")
        self.labelCpfCliente.pack(side="left")
        self.inputCpfCliente = tk.Entry(self.frameCpfCliente, width=11)
        self.inputCpfCliente.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameCpfCliente, text="Buscar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterBuscaCliente)

        self.labelMostraCliente = tk.Label(self.frameListBox, text="")
        self.labelespaco = tk.Label(self.frameListBox, text="")

        self.labelMostraCliente.pack(side="top")
        self.labelespaco.pack(side="top")

        self.labelListaProdutosEscolha = tk.Label(
            self.frameListBox, text="Escolha o produto:"
        )

        self.labelListaProdutosEscolha.pack(side="top")

        self.listBox = tk.Listbox(self.frameListBox)

        for pds in self.listaProdutos:
            self.listBox.insert(
                tk.END,
                pds.descricao,
            )
        self.listBox.pack()

        self.labelQuantProduto = tk.Label(self.frameButton, text="Insira a quantidade")
        self.labelQuantProduto.pack(side="left")

        self.inputQuantProd = tk.Entry(self.frameButton, width=11)
        self.inputQuantProd.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Adicionar Produto")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterQuantProd)

        self.labelEspacoProdSegundo = tk.Label(self.frameFechaNota, text="")
        self.labelEspacoProdSegundo.pack(side="top")
        self.buttonFechaNf = tk.Button(self.frameFechaNota, text="Finaliza Nota Fiscal")
        self.buttonFechaNf.pack(side="left")
        self.buttonFechaNf.bind("<Button>", controle.criaNotaFiscal)


class LimiteAvisos:
    def __init__(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ControllerCriaNotaFicasl:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ctrlProduto = pd.ControlProduto(self)
        self.ctrlCliente = cl.ControllerCliente(self)

        self.listaProdutos = []
        self.atualizaListaProdutos()

        self.listaNotaFiscal = []
        self.carregaNotaFiscal()

    def cadastraNotaFiscal(self):
        self.ctrlProduto.atualizaListaProdutos()
        self.ctrlCliente.atualizaListaClientes()
        listaClienteNome = []
        for cliente in self.ctrlCliente.listaClientes:
            listaClienteNome.append(cliente.nome)

        self.limiteCadastraNotaFiscal = LimiteNotaFiscal(
            self, self.ctrlProduto.listaProdutos, listaClienteNome
        )

    def criaNotaFiscal(self, event):
        for nf in self.listaNotaFiscal:
            if nf.idNota == self.limiteCadastraNotaFiscal.inputNumNotaInput.get():
                quantidade = nf.quantidade
                for prod in self.listaProdutos:
                    if prod.codNum == nf.idProduto:
                        prod.quantEstoq -= quantidade
                        self.salvaProduto()

        self.limiteAviso = LimiteAvisos("Sucesso", "Nota Fiscal finalizada.")
        self.limiteCadastraNotaFiscal.inputCpfCliente.delete(
            0, len(self.limiteCadastraNotaFiscal.inputCpfCliente.get())
        )
        self.limiteCadastraNotaFiscal.inputQuantProd.delete(
            0, len(self.limiteCadastraNotaFiscal.inputQuantProd.get())
        )
        self.limiteCadastraNotaFiscal.inputNumNotaInput.delete(
            0, len(self.limiteCadastraNotaFiscal.inputNumNotaInput.get())
        )
        self.limiteCadastraNotaFiscal.inputDataNota.delete(
            0, len(self.limiteCadastraNotaFiscal.inputDataNota.get())
        )

        # idNota, idProduto, idCliente, dataEmissao, quantidade

        strTextoNota = f"{self.listaNotaFiscal[-1].idNota}\n {self.listaNotaFiscal[-1].idProduto}\n {self.listaNotaFiscal[-1].idCliente}\n{self.listaNotaFiscal[-1].dataEmissao}\n {self.listaNotaFiscal[-1].quantidade}"

        self.limiteAviso = LimiteAvisos("Sucesso", strTextoNota)

        self.salvaListaNotaFisca()

    def enterBuscaCliente(self, event):
        self.ctrlCliente.atualizaListaClientes()
        clienteNF = self.ctrlCliente.getCliente(
            int(self.limiteCadastraNotaFiscal.inputCpfCliente.get())
        )
        if clienteNF is not None:
            self.limiteCadastraNotaFiscal.labelMostraCliente["text"] = clienteNF.nome

        else:
            self.limiteAviso = LimiteAvisos(
                "CPF NÃO ENCONTRADO", "Faça o cadastro do cliente"
            )

    def enterQuantProd(self, event):
        self.ctrlProduto.atualizaListaProdutos()
        indice = self.limiteCadastraNotaFiscal.listBox.curselection()
        flagCadastra = False
        if indice:
            produtoSlc = self.limiteCadastraNotaFiscal.listBox.get(indice)
            produto = self.ctrlProduto.getProdutoDesc(produtoSlc)
            quantidadeSlc = int(self.limiteCadastraNotaFiscal.inputQuantProd.get())
            if quantidadeSlc > 0:
                if quantidadeSlc > produto.quantEstoq:
                    self.limiteAviso = LimiteAvisos(
                        "Erro", "Quantidade insuficiente em estoque"
                    )
                else:
                    quantidade = quantidadeSlc
                    flagCadastra = True

            else:
                self.limiteAviso = LimiteAvisos("Erro", "Nenhuma quantidade")
        else:
            self.limiteAviso = LimiteAvisos("Erro", "Nenhum produto selecionado")

        if flagCadastra:
            ####################
            idNotaFiscal = self.limiteCadastraNotaFiscal.inputNumNotaInput.get()

            inputCliente = self.limiteCadastraNotaFiscal.inputCpfCliente.get()
            if inputCliente is None:
                self.limiteAviso = LimiteAvisos("Erro", "Nenhum cliente selecionado")
            else:
                clienteSlc = self.ctrlCliente.getCliente(int(inputCliente))

            if clienteSlc is None:
                self.limiteAviso = LimiteAvisos("Erro", "Cliente não encontrado")
            else:
                idCliente = clienteSlc.cpf

            indice = self.limiteCadastraNotaFiscal.listBox.curselection()
            if indice:
                # Obtém o valor da linha selecionada
                produtoSlc = self.limiteCadastraNotaFiscal.listBox.get(indice)
                produto = self.ctrlProduto.getProdutoDesc(produtoSlc)
                idProduto = produto.codNum
            else:
                self.limiteAviso = LimiteAvisos("Erro", "Nenhum produto selecionado")

            dataLancamento = self.limiteCadastraNotaFiscal.inputDataNota.get()
            if dataLancamento is None:
                self.limiteAviso = LimiteAvisos("Erro", "Adicione data a nota fiscal")

            notaFiscal = NotaFiscal(
                idNotaFiscal, idProduto, idCliente, dataLancamento, quantidade
            )
            self.listaNotaFiscal.append(notaFiscal)

            self.limiteMostra = LimiteAvisos(
                "Sucesso", "Produto adicionado a nota fiscal"
            )
        else:
            self.limiteMostra = LimiteAvisos("Erro", "Produto não inserido")

    def carregaNotaFiscal(self):
        if not os.path.isfile("NotaFiscal.pickle"):
            self.listaNotaFiscal = []

        else:
            with open("NotaFiscal.pickle", "rb") as f:
                self.listaNotaFiscal = pickle.load(f)

    def salvaListaNotaFisca(self):
        with open("NotaFiscal.pickle", "wb") as f:
            pickle.dump(self.listaNotaFiscal, f)

    def atualizaListaProdutos(self):
        if not os.path.isfile("Produtos.pickle"):
            self.listaProdutos = []
        else:
            with open("Produtos.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)

    def salvaProduto(self):
        with open("Produtos.pickle", "wb") as f:
            pickle.dump(self.listaProdutos, f)

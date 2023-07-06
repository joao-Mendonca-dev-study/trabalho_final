import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
import cliente as cl
import produto as pd


class NotaFiscal:
    def __init__(self, nroUnico, listaDeProdVend, valorTotal, dataEmissao):
        self.__nroUnico = nroUnico
        self.__listaDeProdVend = listaDeProdVend
        self.__valorTotal = valorTotal
        self.__dataEmissao = dataEmissao

    @property
    def nroUnico(self):
        return self.__nroUnico

    @property
    def listaDeProdVend(self):
        return self.__listaDeProdVend

    @property
    def valorTotal(self):
        return self.__valorTotal

    @property
    def dataEmissao(self):
        return self.__dataEmissao


class LimiteNotaFiscal(tk.Toplevel):
    def __init__(self, controle, listaProdutos):
        tk.Toplevel.__init__(self)
        self.geometry("400x250")
        self.title("Gerar Nota Fiscal de Venda")
        self.controle = controle
        self.listaProdutos = listaProdutos

        self.frameCpfCliente = tk.Frame(self)
        self.frameListBox = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCpfCliente.pack()
        self.frameListBox.pack()
        self.frameButton.pack()

        self.labelCpfCliente = tk.Label(self.frameCpfCliente, text="Cpf do Cliente")
        self.labelCpfCliente.pack(side="left")
        self.labelListaProdutos = tk.Label(self.frameListBox, text="Lista de Produtos")
        self.labelListaProdutos.pack(side="top")
        self.listBox = tk.Listbox(self.frameListBox)

        for pds in self.listaProdutos:
            self.listBox.insert(
                tk.END,
                str(pds.codNum) + "-" + pds.descricao + "-" + str(pds.quantEstoq),
            )
        self.listBox.pack()

        self.inputCpfCliente = tk.Entry(self.frameCpfCliente, width=11)
        self.inputCpfCliente.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)


class LimiteAvisos:
    def __init__(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ControllerCriaNotaFicasl:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ctrlProduto = pd.ControlProduto(self)
        self.ctrlCliente = cl.ControllerCliente(self)

    def cadastraNotaFiscal(self):
        self.ctrlProduto.atualizaListaProdutos()
        self.limiteCadastraNotaFiscal = LimiteNotaFiscal(
            self, self.ctrlProduto.listaProdutos
        )

    def enterHandler(self, event):
        self.ctrlCliente.atualizaListaClientes()
        self.clienteNF = self.ctrlCliente.getCliente(
            int(self.limiteCadastraNotaFiscal.inputCpfCliente.get())
        )
        if self.clienteNF is not None:
            self.limiteAviso = LimiteAvisos("Cliente encontrado", self.clienteNF.nome)

        else:
            self.limiteAviso = LimiteAvisos(
                "CPF NÃO ENCONTRADO", "Faça o cadastro do cliente"
            )

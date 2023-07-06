import tkinter as tk
from tkinter import END, messagebox
import os.path
import pickle
import produto


class Cliente:
    def __init__(self, cpf, nome, endereco, email):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco
        self.__email = email

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def email(self):
        return self.__email


class LimiteCliente(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("250x100")
        self.title("Cliente")
        self.controle = controle

        self.frameCpf = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameEndereco = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCpf.pack()
        self.frameNome.pack()
        self.frameEndereco.pack()
        self.frameEmail.pack()
        self.frameButton.pack()

        self.labelCpf = tk.Label(self.frameCpf, text="Nro CPF: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelEndereco = tk.Label(self.frameEndereco, text="Endereco: ")
        self.labelEmail = tk.Label(self.frameEmail, text="Email: ")
        self.labelCpf.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelEndereco.pack(side="left")
        self.labelEmail.pack(side="left")

        self.inputCpf = tk.Entry(self.frameCpf, width=11)
        self.inputCpf.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")
        self.inputEndereco = tk.Entry(self.frameEndereco, width=20)
        self.inputEndereco.pack(side="left")
        self.inputEmail = tk.Entry(self.frameEmail, width=20)
        self.inputEmail.pack(side="left")

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

class ConsultaCliente(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("250x100")
        self.title("Cliente")
        self.controle = controle

        self.frameCpf = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameEndereco = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCpf.pack()
        self.frameNome.pack()
        self.frameEndereco.pack()
        self.frameEmail.pack()
        self.frameButton.pack()

        self.labelCpf = tk.Label(self.frameCpf, text="Nro CPF: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelEndereco = tk.Label(self.frameEndereco, text="Endereco: ")
        self.labelEmail = tk.Label(self.frameEmail, text="Email: ")
        self.labelCpf.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelEndereco.pack(side="left")
        self.labelEmail.pack(side="left")

        self.inputCpf = tk.Entry(self.frameCpf, width=11)
        self.inputCpf.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20, state="readonly")
        self.inputNome.pack(side="left")
        self.inputEndereco = tk.Entry(self.frameEndereco, width=20, state="readonly")
        self.inputEndereco.pack(side="left")
        self.inputEmail = tk.Entry(self.frameEmail, width=20, state="readonly")
        self.inputEmail.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraClientes:
    def __init__(self, str):
        messagebox.showinfo("Clientes Cadastrados: ", str)

class LimiteMostraFatura(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("250x200")
        self.title("Consultar Produto")
        self.controle = controle

        self.frameCodNum = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.dadosUm = tk.Frame(self)
        self.dadosDois = tk.Frame(self)

        self.frameCodNum.pack()
        self.frameButton.pack()
        self.dadosUm.pack(padx=10, pady=10)
        self.dadosDois.pack(padx=10, pady=10)

        self.labelCodNum = tk.Label(self.frameCodNum, text="Digite o CPF do Cliente")
        self.labelCodNum.pack(side="left")

        self.inputCodNum = tk.Entry(self.frameCodNum, width=10)
        self.inputCodNum.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaFaturamentoEnter)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerFaturamento)

        self.labelNome = tk.Label(self.dadosUm, text="Nome")
        self.labelNome.pack(side="left")

        self.inputNome = tk.Entry(self.dadosUm, width=10, state="disabled")
        self.inputNome.pack(side="left")

        self.labelQtde = tk.Label(self.dadosDois, text="Total")
        self.labelQtde.pack(side="left")

        self.inputQtde = tk.Entry(self.dadosDois, width=10, state="disabled")
        self.inputQtde.pack(side="left")

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteAlertaCliente:
    def __init__(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ControllerCliente:
    def __init__(self, controlador):
        self.controlador = controlador
        self.listaClientes = []
        self.listaProdutos = []

        if not os.path.isfile("Clientes.pickle"):
            self.listaClientes = []
        else:
            with open("Clientes.pickle", "rb") as f:
                self.listaClientes = pickle.load(f)

    def salvaCliente(self):
        with open("Clientes.pickle", "wb") as f:
            pickle.dump(self.listaClientes, f)

    def getCliente(self, cpf):
        for cl in self.listaClientes:
            if cl.cpf == cpf:
                return cl
        return None

    def cadastraCliente(self):
        self.limiteCliente = LimiteCliente(self)

    def limpaRegistroClientes(self):
        if os.path.isfile("Clientes.pickle"):
            os.remove("Clientes.pickle")
            self.limiteAlerta = LimiteAlertaCliente(
                "Sucesso", "Lista apagada com Sucesso"
            )

        else:
            self.limiteAlerta = LimiteAlertaCliente(
                "Atenção", "Não existe nenhum registro"
            )

    # cpf, nome, endereco, email
    def enterHandler(self, event):
        cpf = int(self.limiteCliente.inputCpf.get())
        nome = self.limiteCliente.inputNome.get()
        endereco = self.limiteCliente.inputEndereco.get()
        email = self.limiteCliente.inputEmail.get()

        cliente = self.getCliente(cpf)
        if cliente:
            self.limiteCliente.mostraJanela("Atenção", "Cliente já cadastrado")
            self.salvaCliente()
        else:
            cliente = Cliente(cpf, nome, endereco, email)
            self.listaClientes.append(cliente)
            self.salvaCliente()
            self.limiteCliente.mostraJanela("Sucesso", "Cliente cadastrado com sucesso")
            self.atualizaListaClientes()
            self.clearHandler(event)

    def consultaHandler(self, event):
        cpf = int(self.consultaCliente.inputCpf.get())
        cliente = self.getCliente(cpf)
        if cliente:
            self.consultaCliente.inputNome.config(state="normal")
            self.consultaCliente.inputNome.delete(0,END)
            self.consultaCliente.inputNome.insert(0, cliente.nome)
            self.consultaCliente.inputNome.config(state="readonly")

            self.consultaCliente.inputEndereco.config(state="normal")
            self.consultaCliente.inputEndereco.delete(0,END)
            self.consultaCliente.inputEndereco.insert(0, cliente.endereco)
            self.consultaCliente.inputEndereco.config(state="readonly")

            self.consultaCliente.inputEmail.config(state="normal")
            self.consultaCliente.inputEmail.delete(0,END)
            self.consultaCliente.inputEmail.insert(0, cliente.email)
            self.consultaCliente.inputEmail.config(state="readonly")
            self.atualizaListaClientes()
        else:
            self.consultaCliente.mostraJanela("Erro", "Cliente nao cadastrado")

    def clearHandler(self, event):
        self.limiteCliente.inputCpf.delete(0, len(self.limiteCliente.inputCpf.get()))
        self.limiteCliente.inputNome.delete(0, len(self.limiteCliente.inputNome.get()))
        self.limiteCliente.inputEndereco.delete(
            0, len(self.limiteCliente.inputEndereco.get())
        )
        self.limiteCliente.inputEmail.delete(
            0, len(self.limiteCliente.inputEmail.get())
        )

    def fechaHandler(self, event):
        self.limiteCliente.destroy()

    def mostraClientes(self):
        self.atualizaListaClientes()
        strClientesText = "CPF -- Nome\n"
        for cliente in self.listaClientes:
            strClientesText += str(cliente.cpf) + " -- " + cliente.nome + "\n"
        self.limiteLista = LimiteMostraClientes(strClientesText)

    def atualizaListaClientes(self):
        if not os.path.isfile("Clientes.pickle"):
            self.listaClientes = []
        else:
            with open("Clientes.pickle", "rb") as f:
                self.listaClientes = pickle.load(f)

    def consultarCliente(self):
        self.consultaCliente = ConsultaCliente(self)

    def consultaFaturamentoEnter(self, event):
        codigo = int(self.limiteConsultaFaturamento.inputCodNum.get())
        total = 0
        self.atualizaListaNf()
        for nf in self.listaNF:
            if nf.idCliente == codigo:
                total += nf.quantidade

        try:
            cliente = self.getCliente(codigo)
            if(cliente):
                valor = cliente.valorVenda * total
                self.limiteConsultaFaturamento.inputQtde.config(state="normal")
                self.limiteConsultaFaturamento.inputQtde.delete(0, END)
                self.limiteConsultaFaturamento.inputQtde.insert(0, valor)
                self.limiteConsultaFaturamento.inputQtde.config(state="readonly")
                self.limiteConsultaFaturamento.inputNome.config(state="normal")
                self.limiteConsultaFaturamento.inputNome.delete(0, END)
                self.limiteConsultaFaturamento.inputNome.insert(0, cliente.nome)
                self.limiteConsultaFaturamento.inputNome.config(state="readonly")
            else:
                self.limiteConsultaFaturamento.mostraJanela("Erro", "Cliente nao existente")
        except ValueError as error:
            self.limiteConsultaFaturamento.mostraJanela("Erro", "Cliente nao existente")

    def mostraFaturamento(self):
        self.limiteConsultaFaturamento = LimiteMostraFatura(self)

    def fechaHandlerFaturamento(self, event):
        self.limiteConsultaFaturamento.destroy()

    def atualizaListaNf(self):
        if not os.path.isfile("NotaFiscal.pickle"):
            self.listaNF = []
        else:
            with open("NotaFiscal.pickle", "rb") as f:
                self.listaNF = pickle.load(f)
    
    def atualizaListaProdutos(self):
        if not os.path.isfile("Produtos.pickle"):
            self.listaProdutos = []
        else:
            with open("Produtos.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)

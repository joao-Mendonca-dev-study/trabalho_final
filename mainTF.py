import tkinter as tk
from tkinter import messagebox
import produto as pd
import cliente as cl
import notaFiscal as nf


class LimitePrincipal:
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry("500x250")
        self.menubar = tk.Menu(self.root)
        self.clienteMenu = tk.Menu(self.menubar)
        self.produtoMenu = tk.Menu(self.menubar)
        self.nFMenu = tk.Menu(self.menubar)
        self.consultaMenu = tk.Menu(self.menubar)

        self.clienteMenu.add_command(
            label="Insere", command=self.controle.cadastraCliente
        )
        self.clienteMenu.add_command(
            label="Mostra", command=self.controle.mostraClientes
        )
        self.clienteMenu.add_command(
            label="Exclui registros", command=self.controle.excluiClientes
        )
        self.produtoMenu.add_command(
            label="Cadastrar", command=self.controle.cadastraProduto
        )
        self.produtoMenu.add_command(
            label="Limpar Estoque", command=self.controle.limpaEstoque
        )
        self.produtoMenu.add_command(
            label="Mostra", command=self.controle.mostraEstoque
        )
        self.consultaMenu.add_command(
            label="Produtos", command=self.controle.consultaProduto
        )
        self.consultaMenu.add_command(
            label="Clientes", command=self.controle.consultaCliente
        )
        self.consultaMenu.add_command(
            label="Faturamento por Produtos"
        )
        self.consultaMenu.add_command(
            label="Faturamento por Clientes"
        )
        self.consultaMenu.add_command(
            label="Faturamento no Periodo"
        )
        self.consultaMenu.add_command(
            label="Lucro no Periodo"
        )
        self.consultaMenu.add_command(
            label="Vendas para Cliente"
        )
        self.consultaMenu.add_command(
            label="Produtos mais Vendidos"
        )

        self.nFMenu.add_command(label="Insere", command=controle.cadastraNotaFiscal)
        self.nFMenu.add_command(label="Mostra")

        self.menubar.add_cascade(label="Cliente", menu=self.clienteMenu)
        self.menubar.add_cascade(label="Produto", menu=self.produtoMenu)
        self.menubar.add_cascade(label="Nota Fiscal", menu=self.nFMenu)
        self.menubar.add_cascade(label="Consulta", menu=self.consultaMenu)

        self.root.config(menu=self.menubar)


class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()

        self.limite = LimitePrincipal(self.root, self)
        self.ctrlProduto = pd.ControlProduto(self)
        self.ctrlCliente = cl.ControllerCliente(self)
        self.ctrlNotaFiscal = nf.ControllerCriaNotaFicasl(self)

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()

    def cadastraProduto(self):
        self.ctrlProduto.cadastraProduto()

    def limpaEstoque(self):
        self.ctrlProduto.limpaEstoque()

    def mostraEstoque(self):
        self.ctrlProduto.mostraProdutos()

    def cadastraCliente(self):
        self.ctrlCliente.cadastraCliente()

    def mostraClientes(self):
        self.ctrlCliente.mostraClientes()

    def excluiClientes(self):
        self.ctrlCliente.limpaRegistroClientes()

    def cadastraNotaFiscal(self):
        self.ctrlNotaFiscal.cadastraNotaFiscal()
    
    def consultaProduto(self):
        self.ctrlProduto.consultaProduto()
    
    def consultaCliente(self):
        self.ctrlCliente.consultarCliente()

if __name__ == "__main__":
    c = ControlePrincipal()

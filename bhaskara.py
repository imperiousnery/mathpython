import tkinter as tk
from tkinter import *
import numpy as np
from Style import fontes
from Style import colors
import time


class AppBhaskara():
    def __init__(self):
        self.root_bhaskara = tk.Tk()
        self.fonte_padrao = fontes.fonte_bhaskara_label
        self.fonte_btn = fontes.fonte_btn_main
        self.tela()
        self.frame_graph()
        self.widgets()
        self.canvas.bind("<Configure>", self.update_canvas)
        self.root_bhaskara.mainloop()

    def tela(self):
        self.root_bhaskara.title("Bhaskara")
        self.root_bhaskara.geometry("800x800")
        self.root_bhaskara.config(bg=colors.background1)

    def frame_graph(self):
        self.frm = Frame(self.root_bhaskara, bg="black")
        self.frm.place(relx=0.6, rely=0.05, relwidth=0.30, relheight=0.30)
        self.canvas = tk.Canvas(self.frm, bg="black")
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

    def criarEixos(self, event):
        self.canvas.delete("all")

        self.width = event.width
        self.height = event.height

        self.center_x = self.width / 2
        self.center_y = self.height / 2
        self.ponto = 5

        self.canvas.create_line(0, self.height / 2, self.width, self.height / 2, fill="green")
        self.canvas.create_line(self.width / 2, 0, self.width / 2, self.height, fill="green")
        self.canvas.create_oval(self.center_x - self.ponto, self.center_y - self.ponto,
                                self.center_x + self.ponto, self.center_y + self.ponto, fill="green")

    def update_canvas(self, event):
        self.criarEixos(event)
        self.canvas.delete("red")  # Clear the red dots before updating

        for x in range(20):
            self.y = (self.a) * (x ** 2) + (self.b * x) + (self.c)
            coord_x = self.center_x + x * (self.width / 20)
            coord_y = self.center_y - self.y * (self.height / 20)
            self.canvas.create_oval(coord_x - self.ponto, coord_y - self.ponto,
                                    coord_x + self.ponto, coord_y + self.ponto, fill="red")
        for x in range(20):
            x = -x
            self.y = (self.a) * (x ** 2) + (self.b * x) + (self.c)
            coord_x = self.center_x + x * (self.width / 20)
            coord_y = self.center_y - self.y * (self.height / 20)
            self.canvas.create_oval(coord_x - self.ponto, coord_y - self.ponto,
                                    coord_x + self.ponto, coord_y + self.ponto, fill="red")

    def widgets(self):
        self.Label_a = Label(self.root_bhaskara, text="a:", font=self.fonte_padrao, bg=colors.background1,
                             fg=colors.foreground1)
        self.Label_a.place(relx=0.05, rely=0.05)

        self.Label_b = Label(self.root_bhaskara, text="b:", font=self.fonte_padrao, bg=colors.background1,
                             fg=colors.foreground1)
        self.Label_b.place(relx=0.05, rely=0.15)

        self.Label_c = Label(self.root_bhaskara, text="c:", font=self.fonte_padrao, bg=colors.background1,
                             fg=colors.foreground1)
        self.Label_c.place(relx=0.05, rely=0.25)

        self.Entry_a = Entry(self.root_bhaskara, font=self.fonte_padrao, bg=colors.background2,
                             fg=colors.foreground1)
        self.Entry_a.place(relx=0.2, rely=0.05, relheight=0.1, relwidth=0.3)

        self.Entry_b = Entry(self.root_bhaskara, font=self.fonte_padrao, bg=colors.background2,
                             fg=colors.foreground1)
        self.Entry_b.place(relx=0.2, rely=0.15, relheight=0.1, relwidth=0.3)

        self.Entry_c = Entry(self.root_bhaskara, font=self.fonte_padrao, bg=colors.background2,
                             fg=colors.foreground1)
        self.Entry_c.place(relx=0.2, rely=0.25, relheight=0.1, relwidth=0.3)

        self.btnCalcular = Button(self.root_bhaskara, text="CALCULAR", command=self.bhaskara_calc, font=self.fonte_btn,
                                  bg=colors.background2, fg=colors.foreground2)
        self.btnCalcular.place(relx=0.2, rely=0.40, relheight=0.1, relwidth=0.3)

        self.lbl_resultado = Label(self.root_bhaskara, text="f(x) = ax^2+bx+c", font=self.fonte_padrao,
                                   bg=colors.background1, fg=colors.foreground2)
        self.lbl_resultado.place(relx=0.60, rely=0.40)

        self.lbl_footer = Label(self.root_bhaskara, text="Feito por: J.P. Martins\ntyr.mars@protonmail.com\n:D",
                                font=self.fonte_padrao, bg=colors.background1, fg=colors.foreground1)
        self.lbl_footer.place(relx=0.35, rely=0.80, relwidth=0.3)

    def bhaskara_calc(self):
        self.a = float(self.Entry_a.get())
        self.b = float(self.Entry_b.get())
        self.c = float(self.Entry_c.get())
        delta = (self.b ** 2) - 4 * (self.a) * (self.c)
        if delta < 0:
            print("Delta não possui valor real pois seu delta é menor que 0")
            self.lbl_resultado["text"] = f"[Delta não possui raiz!]"
            self.lbl_resultado["fg"] = "red"
            self.canvas.delete("all")
        else:
            raizQ_delta = delta ** (1 / 2)
            self.x1 = (-(self.b) + raizQ_delta) / (2 * (self.a))
            self.x2 = (-(self.b) - raizQ_delta) / (2 * (self.a))
            self.lbl_resultado["text"] = f"f(x) = {self.a}x^2+{self.b}x + {self.c}\n\nX' = {self.x1} | X'' = {self.x2} "
            self.lbl_resultado["fg"] = colors.foreground1
            print(self.x1, self.x2)


if __name__ == "__main__":
    # Função principal
    AppBhaskara()

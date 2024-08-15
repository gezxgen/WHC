import customtkinter as ctk


class Root(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x500+2000+300")
        self.title("WHC - Working hours calculator")

        self.input = Input(master=self, width=250, height=425)
        self.input.pack(side="top", anchor="w", padx=10, pady=10)


class Input(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


def main():
    root = Root()
    root.mainloop()

if __name__ == '__main__':
    main()

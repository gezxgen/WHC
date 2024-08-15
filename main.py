import customtkinter as ctk


class Button(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class Root(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x500+2000+300")
        self.title("WHC - Working hours calculator")
        self.resizable(False, False)

        self.submit = Button(self, text="Submit", command=Root.sub, corner_radius=15,
                             width=250, height=40)
        self.submit.place(relx=0.0, rely=1.0, x=10, y=-53)

        self.input = Frame(master=self, width=250, height=425, corner_radius=20)
        self.input.place(relx=0.0, rely=0.0, x=10, y=10, anchor="nw")

        self.output = Frame(master=self, width=170, height=425, corner_radius=20)
        self.output.place(relx=1.0, rely=0.0, x=-10, y=10, anchor="ne")

    @staticmethod
    def sub():
        print("was pressed")


def main():
    root = Root()
    root.mainloop()


if __name__ == "__main__":
    main()

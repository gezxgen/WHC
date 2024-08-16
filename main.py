import customtkinter as ctk
from datetime import datetime


class Textbox(ctk.CTkTextbox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class Switch(ctk.CTkSwitch):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


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

        self.mode = Switch(master=self, text="Dark Mode", command=Root.mod, font=("Arial", 18, "bold"))
        self.mode.place(x=280, y=455)
        self.mode.select()

        self.submit = Button(master=self, text="Submit", command=Root.sub, corner_radius=15,
                             width=250, height=40, font=("Arial", 25, "bold"), text_color="white")
        self.submit.place(relx=0.0, rely=1.0, x=10, y=-53)

        self.input = Frame(master=self, width=250, height=425, corner_radius=20)
        self.input.place(relx=0.0, rely=0.0, x=10, y=10, anchor="nw")

        self.output = Frame(master=self, width=170, height=425, corner_radius=20)
        self.output.place(relx=1.0, rely=0.0, x=-10, y=10, anchor="ne")

        self.textbox = Textbox(master=self.output, height=50, width=100, corner_radius=10, font=("Arial", 25, "bold"))
        self.textbox.place(anchor="n", x=85, y=50)
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", " " + datetime.now().strftime("%H:%M"))
        self.textbox.configure(state="disabled")


    @staticmethod
    def sub():
        print("Submit")

    @staticmethod
    def mod():
        ctk.set_appearance_mode("dark" if ctk.get_appearance_mode().lower() == "light" else "light")


def main():
    ctk.set_appearance_mode("dark")
    root = Root()
    root.mainloop()


if __name__ == "__main__":
    main()

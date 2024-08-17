import customtkinter as ctk
from datetime import datetime


class Root(ctk.CTk):
    def __init__(self):
        # Settings for the root window
        self.labels = []
        self.titles = ["Time entry", "Time now", "Time 8:24", "Time 9:00"]
        self.textboxes = []
        self.y_distances = [50, 150, 250, 350]
        super().__init__()
        self.geometry("450x500+2000+300")
        self.title("WHC - Working hours calculator")
        self.resizable(False, False)

        # Switch for Dark / Light mode
        self.mode = ctk.CTkSwitch(master=self, text="Dark Mode", command=Root.mod, font=("Arial", 18, "bold"))
        self.mode.place(x=280, y=455)
        self.mode.select()

        # Settings for submit button
        self.submit = ctk.CTkButton(master=self, text="Submit", command=Root.sub, corner_radius=15,
                             width=250, height=40, font=("Arial", 25, "bold"), text_color="white")
        self.submit.place(relx=0.0, rely=1.0, x=10, y=-53)

        # Settings for the frames
        self.input = ctk.CTkFrame(master=self, width=250, height=425, corner_radius=20)
        self.input.place(relx=0.0, rely=0.0, x=10, y=10, anchor="nw")
        self.output = ctk.CTkFrame(master=self, width=170, height=425, corner_radius=20)
        self.output.place(relx=1.0, rely=0.0, x=-10, y=10, anchor="ne")

        # Add output textboxes and labels
        for i, val in enumerate(self.y_distances):
            # Create output textboxes
            self.textbox = ctk.CTkTextbox(master=self.output, height=50, width=100, corner_radius=10,
                                   font=("Arial", 25, "bold"))
            self.textbox.place(anchor="n", x=85, y=val)
            self.textbox.delete("0.0", "end")
            self.textbox.insert("0.0", " " + datetime.now().strftime("%H:%M"))
            self.textbox.configure(state="disabled")
            self.textboxes.append(self.textbox)

            # Add titles to textboxes
            self.label = ctk.CTkLabel(master=self.output, text=self.titles[i], font=("Arial", 18, "bold"))
            self.label.place(anchor="n", x=85, y=val-30)
            self.labels.append(self.label)

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

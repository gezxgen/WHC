import customtkinter as ctk
from datetime import datetime


class Root(ctk.CTk):
    def __init__(self):
        # Settings for the root window
        super().__init__()
        self.geometry("460x500+2000+300")
        self.title("WHC - Working hours calculator")
        self.resizable(False, False)
        self.x = 0
        self.y = 0
        self.checkboxes = []
        self.labels = []
        self.titles = ["Time entry", "Time now", "Time 8:24", "Time 9:00",
                       "Start", "1. break", "2. break", "3. break", "4. break", "End"]
        self.textboxes = []
        self.y_distances = [50, 150, 250, 350]
        self.hours = [str(i).zfill(2) for i in range(24)]
        self.minutes = [str(i).zfill(2) for i in range(60)]
        self.values = [ctk.StringVar(value="00") for _ in range(24)]

        # Switch for Dark / Light mode
        self.mode = ctk.CTkSwitch(master=self, text="Dark Mode", command=Root.mod, font=("Arial", 18, "bold"))
        self.mode.place(x=290, y=455)
        self.mode.select()

        # Settings for submit button
        self.submit = ctk.CTkButton(master=self, text="Submit", command=self.sub, corner_radius=15,
                             width=260, height=40, font=("Arial", 25, "bold"), text_color="white")
        self.submit.place(relx=0.0, rely=1.0, x=10, y=-53)

        # Settings for the frames
        self.input = ctk.CTkFrame(master=self, width=260, height=425, corner_radius=20)
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
            self.textbox.insert("0.0", " 00:00")
            self.textbox.configure(state="disabled")
            self.textboxes.append(self.textbox)

            # Add titles to textboxes
            self.label = ctk.CTkLabel(master=self.output, text=self.titles[i], font=("Arial", 18, "bold"))
            self.label.place(anchor="n", x=85, y=val-30)
            self.labels.append(self.label)

        # Add drop-down menus
        for i in range(1, 7):
            # menus for hours left
            self.x = 10
            self.y = 50 if i == 1 else 50+60*(i-1)
            self.option_menu = ctk.CTkOptionMenu(master=self.input, anchor="n", height=25, width=45, values=self.hours,
                                                 variable=self.values[i-1], font=("Arial", 18, "bold"))
            self.option_menu.place(x=self.x, y=self.y)

            # menus for minutes left
            self.x = 70
            self.option_menu = ctk.CTkOptionMenu(master=self.input, anchor="n", height=25, width=45, values=self.minutes,
                                                 variable=self.values[i + 5], font=("Arial", 18, "bold"))
            self.option_menu.place(x=self.x, y=self.y)

            # checkboxes for breaks
            if i != 1 and i != 6:
                self.checkbox = ctk.CTkCheckBox(master=self.input, checkbox_height=18, checkbox_width=18,
                                                text="", variable=self.values[i+18])
                self.checkbox.place(x=15, y=self.y-28)
                self.checkboxes.append(self.checkbox)

                # Hyphens between breaks
                self.x = 130
                self.y = 50 if i == 1 else 50 + 60 * (i - 1)
                self.label = ctk.CTkLabel(master=self.input, text="-", font=("Arial", 20, "bold"))
                self.label.place(anchor="n", x=self.x, y=self.y - 3)
                self.labels.append(self.label)

                # menus for hours right
                self.x = 136
                self.option_menu = ctk.CTkOptionMenu(master=self.input, anchor="n", height=25, width=45, values=self.hours,
                                                     variable=self.values[i + 10], font=("Arial", 18, "bold"))
                self.option_menu.place(x=self.x, y=self.y)

                # menus for minutes right
                self.x = 195
                self.option_menu = ctk.CTkOptionMenu(master=self.input, anchor="n", height=25, width=45, values=self.minutes,
                                                     variable=self.values[i + 14], font=("Arial", 18, "bold"))
                self.option_menu.place(x=self.x, y=self.y)

            # labels of the breaks
            self.x = 30 if i == 1 or i == 6 else 70
            self.y = 50 if i == 1 else 50 + 60 * (i - 1)
            self.label = ctk.CTkLabel(master=self.input, text=self.titles[i+3], font=("Arial", 15, "bold"))
            self.label.place(anchor="n", x=self.x, y=self.y-30)
            self.labels.append(self.label)

    # Funciton that calculates all the time worked
    def get_time(self) -> int:
        time_start = 60 * int(self.values[0].get()) + int(self.values[6].get())
        time_end = 60 * int(self.values[5].get()) + int(self.values[11].get())
        return time_end - time_start - self.get_breakes()

    # Function that calculates the minutes of all the breakes
    def get_breakes(self) -> int:
        breaktimes: int = 0
        for i in range(4):
            if self.values[i+20].get() == "1":
                breaktimes += 60 * (int(self.values[i+12].get()) - int(self.values[i+1].get()))
                breaktimes += int(self.values[i+16].get()) - int(self.values[i+7].get())
        return breaktimes

    # Function that calculates the times after submission
    def sub(self):
        print("Submit")
        working_time: int = self.get_time()
        #self.textboxes
        #datetime.now().strftime("%H:%M")
        print(working_time)
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

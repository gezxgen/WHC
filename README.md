# WHC
Working hours calculator for lazy people (using customtkinter)

# Documentation: WHC - Working Hours Calculator

---

## Overview

The **WHC (Working Hours Calculator)** is a desktop application built using the `customtkinter` library. It allows users to input and calculate their working hours, including breaks. The app features a graphical user interface (GUI) for ease of use and toggles between Dark and Light modes.

---

## Features

- **Responsive GUI**: The application uses the `customtkinter` library to create a sleek and modern user interface.
- **Time Entry**: Users can enter times such as start, breaks, and end times of their working day.
- **Dark Mode Toggle**: A switch is provided to toggle between Dark Mode and Light Mode.
- **Submit Button**: The `Submit` button processes the data and performs the calculation for working hours.

---

## Components

The main window (`Root`) serves as the base for the application:
- **Size**: 460x500 pixels.
- **Title**: WHC - Working hours calculator.
- **Widgets**: 
  - Labels and textboxes for time input.
  - Switch for toggling between Dark Mode and Light Mode.
  - Submit button for processing the time entries.

```python
class Root(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("460x500+2000+300")
        self.title("WHC - Working hours calculator")
        self.resizable(False, False)

        # Switch for Dark / Light mode
        self.mode = ctk.CTkSwitch(master=self, text="Dark Mode", command=Root.mod, font=("Arial", 18, "bold"))
        self.mode.place(x=290, y=455)
        self.mode.select()

        # Submit Button
        self.submit = ctk.CTkButton(master=self, text="Submit", command=self.sub, corner_radius=15, width=260, height=40, font=("Arial", 25, "bold"), text_color="white")
        self.submit.place(relx=0.0, rely=1.0, x=10, y=-53)
```

Usage Instructions
Launch the Application: Start the program to open the main window.
Enter Time Data: Use the provided textboxes to input your work times, including start, breaks, and end times.
Toggle Dark Mode: Switch between dark and light modes using the toggle switch in the bottom-right corner.
Submit the Data: Once all the data is entered, click on the Submit button to calculate your working hours.
Screenshots
Below are some example screenshots of the application in action:




Future Improvements
Potential improvements could include:

Adding data validation for time entries.
Expanding the app's functionality to calculate overtime or track daily work summaries.
Adding a database to store and retrieve historical time entries.
Conclusion
The WHC - Working Hours Calculator is a helpful tool for professionals looking to track their working hours easily. Its simple yet functional design makes it user-friendly, while the mode switch adds a touch of customization.

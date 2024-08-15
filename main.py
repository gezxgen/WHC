import customtkinter as CTk

def main():
    print("Hello World!")
    root = CTk.CTk()
    root.geometry("450x500+2000+300")
    root.title("WHC - Working hours calculator")
    input = CTk.CTkFrame(master=root, width=250, height=425)
    input.pack(side="top", anchor="w", padx=10, pady=10)
    root.mainloop()

if __name__ == '__main__':
    main()

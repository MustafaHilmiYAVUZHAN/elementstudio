import customtkinter as tk,customtkinter
if __name__ == "__main__":
    root = customtkinter.CTk()
    root.title("Dynamic Table")
    deneme=tk.CTkScrollableFrame(root)
    deneme.pack()
    button=tk.CTkButton(deneme)
    button.place(rely=1,relx=0.52)
    button.place(rely=0.5,relx=0.52)
    root.mainloop()
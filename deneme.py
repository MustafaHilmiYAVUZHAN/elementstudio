import tkinter as tk
import customtkinter as tk,customtkinter

customtkinter.set_appearance_mode("System")  # Görünüm modunu ayarla: "System" (standart), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Temayı ayarla: "blue" (standart), "green", "dark-blue"

def create_table(root, *args):
    mainFrame=customtkinter.CTkScrollableFrame(root)
    mainFrame.place(relx=0.05,rely=0.05,relheight=0.9,relwidth=0.9)
    for arg in args:
        label_text, content = arg[0], arg[1]
        if isinstance(content, list):  # İçerik bir liste ise, bu bir çerçeve veya combobox olabilir
            if isinstance(content[0], list):  # İç içe çerçeve veya combobox
                frame_label = customtkinter.CTkFrame(mainFrame, width=300, corner_radius=10)
                frame_label.grid(row=len(mainFrame.grid_slaves()), column=0, padx=10, pady=5, sticky='ew')
                frame_text = tk.CTkLabel(frame_label,text=label_text)
                frame_text.grid(row=len(mainFrame.grid_slaves()), column=0, padx=5, pady=2, sticky='w')
                for index, item in enumerate(content):
                    if isinstance(item[1], list):  # Combobox
                        sub_label = customtkinter.CTkLabel(frame_label, text=item[0])
                        sub_label.grid(row=index, column=0, padx=5, pady=2, sticky='w')
                        combobox = customtkinter.CTkComboBox(frame_label, values=item[1])
                        combobox.grid(row=index, column=1, padx=5, pady=2, sticky='w')
                        combobox.set(item[1][0])  # Varsayılan olarak ilk öğeyi seç

                    else:  # Entry
                        sub_label = customtkinter.CTkLabel(frame_label, text=item[0])
                        sub_label.grid(row=index, column=0, padx=5, pady=2, sticky='w')
                        entry = customtkinter.CTkEntry(frame_label)
                        entry.grid(row=index, column=1, padx=5, pady=2, sticky='w')
                        entry.insert(0, item[1])  # Varsayılan değeri ekle

            else:  # Combobox
                label = customtkinter.CTkLabel(mainFrame, text=label_text)
                label.grid(row=len(mainFrame.grid_slaves()), column=0, padx=10, pady=5, sticky='w')
                combobox = customtkinter.CTkComboBox(mainFrame, values=content)
                combobox.grid(row=len(mainFrame.grid_slaves()) - 1, column=1, padx=10, pady=5, sticky='ew')
                combobox.set(content[0])  # Varsayılan olarak ilk öğeyi seç

        else:  # Entry
            label = customtkinter.CTkLabel(mainFrame, text=label_text)
            label.grid(row=len(mainFrame.grid_slaves()), column=0, padx=10, pady=5, sticky='w')
            entry = customtkinter.CTkEntry(mainFrame)
            entry.grid(row=len(mainFrame.grid_slaves()) - 1, column=1, padx=10, pady=5, sticky='ew')
            entry.insert(0, content)  # Varsayılan değeri ekle

# Örnek giriş verisi ile fonksiyonu test et
if __name__ == "__main__":
    root = customtkinter.CTk()
    root.title("Dynamic Table")
    
    

    create_table(root,
                 ["Name", ""],
                 ["Birth Date", [
                     ["Birth Day", ""],
                     ["Birth Month", ["January", "February", "March", "April"]],
                     ["Birth Year", "1990"]],
                  ],
                 ["Boy", "170"],
                 ["Where are you living", ["Turkey", "USA", "Germany", "France"]],
                 ["Occupation", ""]
                 )

    root.mainloop()

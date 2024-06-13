import tkinter as tk
import customtkinter as tk,customtkinter

customtkinter.set_appearance_mode("System")  # Görünüm modunu ayarla: "System" (standart), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Temayı ayarla: "blue" (standart), "green", "dark-blue"

def create_table(root, *args):
    for arg in args:
        label_text, content = arg[0], arg[1]
        if isinstance(content, list):  # İçerik bir liste ise, bu bir çerçeve veya combobox olabilir
            if isinstance(content[0], list):  # İç içe çerçeve veya combobox
                frame_label = customtkinter.CTkFrame(root, width=300, corner_radius=10)
                frame_label.grid(row=len(root.grid_slaves()), column=0, padx=10, pady=5, sticky='ew')
                frame_text = tk.CTkLabel(frame_label, text=label_text)
                frame_text.grid(row=0, column=0, padx=5, pady=2, sticky='w')
                frame_height = 0
                
                for index, item in enumerate(content):
                    if isinstance(item[1], list):  # Combobox
                        sub_label = customtkinter.CTkLabel(frame_label, text=item[0])
                        sub_label.place(relx=0.05, rely=frame_height + 0.02, anchor="nw")
                        combobox = customtkinter.CTkComboBox(frame_label, values=item[1])
                        combobox.place(relx=0.5, rely=frame_height + 0.02, anchor="nw")
                        combobox.set(item[1][0])  # Varsayılan olarak ilk öğeyi seç
                        frame_height += 0.1

                    else:  # Entry
                        sub_label = customtkinter.CTkLabel(frame_label, text=item[0])
                        sub_label.place(relx=0.05, rely=frame_height + 0.02, anchor="nw")
                        entry = customtkinter.CTkEntry(frame_label)
                        entry.place(relx=0.5, rely=frame_height + 0.02, anchor="nw")
                        entry.insert(0, item[1])  # Varsayılan değeri ekle
                        frame_height += 0.1

                frame_label.update_idletasks()
                frame_label.configure(height=frame_label.winfo_height(), width=frame_label.winfo_width())
            else:  # Combobox
                label = customtkinter.CTkLabel(root, text=label_text)
                label.grid(row=len(root.grid_slaves()), column=0, padx=10, pady=5, sticky='w')
                combobox = customtkinter.CTkComboBox(root, values=content)
                combobox.grid(row=len(root.grid_slaves()) - 1, column=1, padx=10, pady=5, sticky='ew')
                combobox.set(content[0])  # Varsayılan olarak ilk öğeyi seç

        else:  # Entry
            label = customtkinter.CTkLabel(root, text=label_text)
            label.grid(row=len(root.grid_slaves()), column=0, padx=10, pady=5, sticky='w')
            entry = customtkinter.CTkEntry(root)
            entry.grid(row=len(root.grid_slaves()) - 1, column=1, padx=10, pady=5, sticky='ew')
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

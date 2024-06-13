import tkinter
import customtkinter as tk,customtkinter

customtkinter.set_appearance_mode("System")  # Görünüm modunu ayarla: "System" (standart), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Temayı ayarla: "blue" (standart), "green", "dark-blue"

def create_table(root, *args):
    mainFrame=customtkinter.CTkScrollableFrame(root)
    #mainFrame.place(relx=0.05,rely=0.05,relheight=0.9,relwidth=0.9)
    for arg in args:
        label_text, content = arg[0], arg[1]
        if isinstance(content, list):  # İçerik bir liste ise, bu bir çerçeve veya combobox olabilir
            if isinstance(content[0], list):  # İç içe çerçeve veya combobox
                frame_label = customtkinter.CTkTabview(mainFrame,corner_radius=10,height=root.winfo_screenheight()/20*(len(content[0])),width=200)
                frame_label.grid(row=len(mainFrame.grid_slaves()), column=0, padx=0,columnspan=3, pady=0, sticky='w')
                frame_label.add(label_text,)
                
                for index, item in enumerate(content):
                    if isinstance(item[1], list):  # Combobox
                        sub_label = customtkinter.CTkLabel(frame_label.tab(label_text), text=item[0],width=150)
                        sub_label.grid(row=index, column=0, padx=5, pady=2, sticky='w')
                        combobox = customtkinter.CTkComboBox(frame_label.tab(label_text), values=item[1])
                        combobox.grid(row=index, column=1, padx=5, pady=2, sticky='e')
                        combobox.set(item[1][0])  # Varsayılan olarak ilk öğeyi seç

                    else:  # Entry
                        sub_label = customtkinter.CTkLabel(frame_label.tab(label_text), text=item[0],width=150)
                        sub_label.grid(row=index, column=0, padx=5, pady=2, sticky='w')
                        entry = customtkinter.CTkEntry(frame_label.tab(label_text))
                        entry.grid(row=index, column=1, padx=5, pady=2, sticky='e')
                        entry.insert(0, item[1])  # Varsayılan değeri ekle
                frame_label.update_idletasks()

            else:  # Combobox
                label = customtkinter.CTkLabel(mainFrame, text=label_text,width=150)
                label.grid(row=len(mainFrame.grid_slaves()), column=0, padx=10, pady=5, sticky='w')
                print(label_text)
                combobox = customtkinter.CTkComboBox(mainFrame, values=content)
                combobox.grid(row=len(mainFrame.grid_slaves()) - 1, column=1, padx=10, pady=5, sticky='ew')
                combobox.set(content[0])  # Varsayılan olarak ilk öğeyi seç

        else:  # Entry
            label = customtkinter.CTkLabel(mainFrame, text=label_text,width=150)
            label.grid(row=len(mainFrame.grid_slaves()), column=0, padx=10, pady=5, sticky='w')
            entry = customtkinter.CTkEntry(mainFrame)
            entry.grid(row=len(mainFrame.grid_slaves()) - 1, column=1, padx=10, pady=5, sticky='ew')
            entry.insert(0, content)  # Varsayılan değeri ekle
        return mainFrame

# Örnek giriş verisi ile fonksiyonu test et
if __name__ == "__main__":
    root = customtkinter.CTk()
    root.title("Dynamic Table")
    root.geometry("400x800")
    root.columnconfigure(0, weight=1)
    

    create_table(root,
                 
    ["Name", "Fatma"],
    
        ["Birth Date", [
            ["Day", "5"],
            ["Month", ["March","a","s","s"]],
            ["Year", "1988"]
        ]],
        ["Height (cm)", "160"],
        ["Weight (kg)", "55"],
        ["Where are you living", ["Turkey", "Germany", "USA", "Australia"]],
        ["Occupation", "Doctor"],
        ["Known Languages", ["Turkish", "German", "English", "French"]],
        ["Specialization", "Cardiology"]
    ,
    ["Hobbies", ["Reading", "Hiking", "Cooking"]],
    ["Education", [
        ["Degree", "Doctor of Medicine"],
        ["University", "Ankara University Medical School"]
    ]],
    ["Favorite Food", ["Kebab", "Sushi", "Salad"]],
    ["Music Genre", ["Classical", "Jazz", "Pop"]],
    ["Years of Experience", "10"]

                 )

    root.mainloop()

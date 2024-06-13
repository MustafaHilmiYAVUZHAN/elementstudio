import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Görünüm modunu ayarla: "System" (standart), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temayı ayarla: "blue" (standart), "green", "dark-blue"

def create_table(root, *args):
    scrool=ctk.CTkScrollableFrame(root)
    main_frame=ctk.CTkFrame(root)
    main_frame.place(rely=0.05,relx=0.05,relheight=0.9,relwidth=0.9)
    current_row = 0.5  # Başlangıç satırını ayarla
    row_lenght=0.05
    column_lenght=0.4
    start_column=0.1
    for arg in args:
        label_text, content = arg[0], arg[1]
        if isinstance(content, list):  # İçerik bir liste ise, bu bir çerçeve veya combobox olabilir
            if isinstance(content[0], list):  # İç içe çerçeve veya combobox
                frame_row_lenght=1/(len(content))
                frame_label = ctk.CTkTabview(main_frame,  corner_radius=10)
                frame_label.place(relx=start_column-0.05, rely=current_row * row_lenght,relwidth=0.90,relheight=(len(content)+0.8)*row_lenght)  # Frame'i yerleştir
                frame_label.add(label_text)

                for index, item in enumerate(content):
                    
                    if isinstance(item[1], list):  # Combobox
                        sub_label = ctk.CTkLabel(frame_label.tab(label_text), text=item[0])
                        sub_label.place(relx=0.05, rely=(index ) * frame_row_lenght)
                        combobox = ctk.CTkComboBox(frame_label.tab(label_text), values=item[1])
                        combobox.place(relx=0.50, rely=(index ) * frame_row_lenght)
                        combobox.set(item[1][0])  # Varsayılan olarak ilk öğeyi seç

                    else:  # Entry
                        sub_label = ctk.CTkLabel(frame_label.tab(label_text), text=item[0])
                        sub_label.place(relx=0.05, rely=(index) * frame_row_lenght)
                        entry = ctk.CTkEntry(frame_label.tab(label_text))
                        entry.place(relx=0.50, rely=(index ) * frame_row_lenght)
                        entry.insert(0, item[1])  # Varsayılan değeri ekle
                    current_row+=1
                current_row+=1

            else:  # Combobox
                label = ctk.CTkLabel(main_frame, text=label_text)
                label.place(relx=start_column, rely=current_row * row_lenght)
                print(content)
                combobox = ctk.CTkComboBox(main_frame, values=content)
                combobox.place(relx=start_column+column_lenght, rely=current_row * row_lenght)
                combobox.set(content[0])  # Varsayılan olarak ilk öğeyi seç
                current_row += 1

        else:  # Entry
            label = ctk.CTkLabel(main_frame, text=label_text)
            label.place(relx=start_column, rely=current_row * row_lenght)
            entry = ctk.CTkEntry(main_frame)
            entry.place(relx=start_column+column_lenght, rely=current_row * row_lenght)
            entry.insert(0, content)  # Varsayılan değeri ekle
            current_row += 1

# Örnek giriş verisi ile fonksiyonu test et
if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Dynamic Table")

    create_table(root,
                 
    
    ["Name", "Fatma"],
     
        ["Birth Date", [
            ["Day", "5"],
            ["Month", "March"],
            ["Year", "1988"],
            ["Month", "March"],
            ["Year", "1988"],
            ["Month", "March"],
            ["Year", "1988"],
            ["Month", "March"],
            ["Year", "1988"],
            ["Month", "March"],
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
        ["Years of Experience", "10"],["Name", "Fatma"],
     
        ["Birth Date", [
            ["Day", "5"],
            ["Month", "March"],
            ["Year", "1988"],
            ["Month", "March"],
            ["Year", "1988"],
            ["Month", "March"],
            ["Year", "1988"],
            ["Month", "March"],
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
        ["Years of Experience", "10"],["Name", "Fatma"],
     
        ["Birth Date", [
            ["Day", "5"],
            ["Month", "March"],
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
        ["Years of Experience", "10"],["Name", "Fatma"],
     
        ["Birth Date", [
            ["Day", "5"],
            ["Month", "March"],
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
        ["Years of Experience", "10"])

    root.mainloop()

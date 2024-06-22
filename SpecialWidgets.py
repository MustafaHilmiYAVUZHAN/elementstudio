import customtkinter as tk
import customtkinter
import pywinstyles
class YesNoDiolog:
    def __init__(self, title,label, yes_func=None, no_func=None):
        self.root = tk.CTkToplevel()
        self.root.title(title)
        tk.set_appearance_mode("System")
        
        self.yes_func = yes_func
        self.no_func = no_func
        self.label = tk.CTkLabel(self.root, text=label)
        self.label.pack(pady=10)
        self.root.wm_attributes("-topmost", True)
        tk.set_default_color_theme("extreme.json")
        pywinstyles.apply_style(self.root,"acrylic")
        self.yes_button = tk.CTkButton(self.root, text="Yes", command=self.on_yes_click)
        self.yes_button.pack(side=tk.LEFT, padx=10)

        self.no_button = tk.CTkButton(self.root, text="No", command=self.on_no_click)
        self.no_button.pack(side=tk.RIGHT, padx=10)

        self.result = None

    def on_yes_click(self):
        if self.yes_func:
            self.yes_func()
        self.result = True
        self.root.destroy()

    def on_no_click(self):
        if self.no_func:
            self.no_func()
        self.result = False
        self.root.destroy()
    def show(self):
        self.root.mainloop()
        return self.result

class AdjustableEntry:
    def __init__(self, root, label_text):
        self.root = root
        self.label_text = label_text
        tk.set_appearance_mode("System")
        tk.set_default_color_theme("extreme.json")

        self.SpecialEntryFrame = tk.CTkFrame(self.root,fg_color="#666666")

        self.label = tk.CTkLabel(self.SpecialEntryFrame, text=self.label_text,fg_color="#666666")
        self.label.place(rely=0.05,relx=0.05,relheight=0.9,relwidth=0.25)

        self.btn_add = tk.CTkButton(self.SpecialEntryFrame, text="+", width=10, height=10,command=self.add)
        self.btn_add.place(rely=0.2,relx=0.35,relheight=0.6,relwidth=0.15)


        self.entry = tk.CTkEntry(self.SpecialEntryFrame, width=30)
        self.entry.place(rely=0.05,relx=0.55,relheight=0.9,relwidth=0.2)

        self.btn_decrease = tk.CTkButton(self.SpecialEntryFrame, text="-", width=10, height=10, command=self.decrease)
        self.btn_decrease.place(rely=0.2,relx=0.8,relheight=0.6,relwidth=0.15)

        self.setValue("20")

    def getData(self):
        return self.entry.get()

    def setValue(self, value):
        self.entry.delete(0, 'end')  # Mevcut girişi temizler
        self.entry.insert(0, value)  # Yeni değeri ekler

    def add(self):
        current_value = self.getData()
        if current_value.isdigit():
            new_value = str(int(current_value) + 1)
            self.setValue(new_value)

    def decrease(self):
        current_value = self.getData()
        if current_value.isdigit():
            new_value = str(int(current_value) - 1)
            self.setValue(new_value)
        
class DynamicTable:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        tk.set_default_color_theme("extreme.json")
        self.mainFrame = customtkinter.CTkScrollableFrame(root)
        self.widgets = {}
        self.mainFrame.columnconfigure(2, minsize=10)
        self.framefont = tk.CTkFont(size=25)
    def add_row(self, label_text, content):
        if isinstance(content, list):
            if isinstance(content[0], list):
                inner_widgets = {}
                frame_label = customtkinter.CTkLabel(self.mainFrame,text=label_text,font=self.framefont)
                frame_label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=0, columnspan=3, pady=0)
                inner_widgets[label_text] = frame_label

                for index, item in enumerate(content):
                    if isinstance(item[1], list):
                        if len(item[1]) ==2 and isinstance(item[1][1], list):
                            label = customtkinter.CTkLabel(self.mainFrame, text="◆ "+item[0])
                            label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=10, pady=5, sticky='w')
                            entry = customtkinter.CTkEntry(self.mainFrame,width=80)
                            entry.grid(row=len(self.mainFrame.grid_slaves()) - 1, column=1, padx=5, pady=5, sticky='w')
                            entry.insert(0, item[1][0])
                            combobox = customtkinter.CTkComboBox(self.mainFrame, values=item[1][1], width=70)
                            combobox.grid(row=len(self.mainFrame.grid_slaves()) - 2, column=2, padx=5, pady=5, sticky='w')
                            #combobox.set(content[1][0])
                            inner_widgets[label_text] = (label, entry, combobox)
                        else:
                            
                            sub_label = customtkinter.CTkLabel(self.mainFrame, text="◆ "+item[0])
                            sub_label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=10, pady=5, sticky='w')
                            combobox = customtkinter.CTkComboBox(self.mainFrame, values=item[1],width=160)
                            combobox.grid(row=len(self.mainFrame.grid_slaves())-1, column=1,columnspan=2, padx=5, pady=2, sticky='w')
                            combobox.set(item[1][0])
                            inner_widgets[item[0]] = (sub_label, combobox)
                    else:
                        sub_label = customtkinter.CTkLabel(self.mainFrame, text="◆ "+item[0])
                        sub_label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=10, pady=5, sticky='w')
                        entry = customtkinter.CTkEntry(self.mainFrame,width=160)
                        entry.grid(row=len(self.mainFrame.grid_slaves())-1, column=1, columnspan=2, padx=5, pady=2, sticky='w')
                        entry.insert(0, item[1])
                        inner_widgets[item[0]] = (sub_label, entry)
                self.widgets[label_text] = inner_widgets
            else:
                if isinstance(content[0], str) and isinstance(content[1], list):
                    label = customtkinter.CTkLabel(self.mainFrame, text=label_text)
                    label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=5, pady=5, sticky='w')
                    entry = customtkinter.CTkEntry(self.mainFrame,width=80)
                    entry.grid(row=len(self.mainFrame.grid_slaves()) - 1, column=1, padx=5, pady=5, sticky='w')
                    entry.insert(0, content[0])
                    combobox = customtkinter.CTkComboBox(self.mainFrame, values=content[1], width=70)
                    combobox.grid(row=len(self.mainFrame.grid_slaves()) - 2, column=2, padx=5, pady=5, sticky='w')
                    combobox.set(content[1][0])
                    self.widgets[label_text] = (label, entry, combobox)
                else:
                    label = customtkinter.CTkLabel(self.mainFrame, text=label_text)
                    label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=5, pady=5, sticky='w')
                    combobox = customtkinter.CTkComboBox(self.mainFrame, values=content,width=160)
                    combobox.grid(row=len(self.mainFrame.grid_slaves()) - 1, column=1, columnspan=2, padx=5, pady=5, sticky='w')
                    combobox.set(content[0])
                    self.widgets[label_text] = (label, combobox)
        else:
            label = customtkinter.CTkLabel(self.mainFrame, text=label_text)
            label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=5, pady=5, sticky='w')
            entry = customtkinter.CTkEntry(self.mainFrame,width=160)
            entry.grid(row=len(self.mainFrame.grid_slaves()) - 1, column=1, columnspan=3, padx=5, pady=5,sticky='w' )
            entry.insert(0, content)
            self.widgets[label_text] = (label, entry)

    def find_widget(self, label_text):
        if label_text in self.widgets:
            return self.widgets[label_text]
        else:
            for widgets in self.widgets.values():
                keys = list(widgets.keys())
                print(widgets)
                if len(keys) > 1 and isinstance(widgets[keys[0]], str) and isinstance(widgets[keys[1]], list) and label_text in widgets:
                    pass
                elif isinstance(widgets, dict) and label_text in widgets:
                    return widgets[label_text]
        return None

    def destroy_widget(self, label_text):
        widget = self.widgets.pop(label_text, None)
        
        if widget:
            if isinstance(widget, dict):
                for inner_widget in widget.values():
                    if isinstance(inner_widget, tuple):
                        for w in inner_widget:
                            w.destroy()
                    else:
                        inner_widget.destroy()
            elif isinstance(widget, tuple):
                widget[1].destroy()
                widget[0].destroy()
                if len(widget)==3:
                    widget[2].destroy()

    def get_widget(self, label_text):
        widget = self.find_widget(label_text)
        if widget:
            if isinstance(widget, dict):
                entries = []
    
                for key, value in widget.items():
                    # value bir tuple ve ikinci elemanı customtkinter.CTkEntry mi?
                    if isinstance(value, tuple) and len(value)==3:
                        #print(value)
                        entry_value = value[1].get()+value[2].get()
                        entries.append((key, entry_value))
                    else :
                        entry_value = value[1].get()
                        entries.append((key, entry_value))
                
                return entries
            elif isinstance(widget, tuple):
                if len(widget)==2 and isinstance(widget[0], str) and isinstance(widget[1], list):
                    return widget[1].get()
                elif len(widget)==3:
                    return widget[1].get()+widget[2].get()
            elif isinstance(widget, customtkinter.CTkEntry):
                return widget.get()
        return None
    def all_data_in_wigdet(self):
        self.data_dict = {}
        for label_text, widget in self.widgets.items():
            if isinstance(widget, tuple):
                if len(widget) == 2:
                    self.data_dict[label_text] = widget[1].get()
                elif len(widget) == 3:
                    self.data_dict[label_text] = widget[1].get() + widget[2].get()
            elif isinstance(widget, dict):
                inner_dict = {}
                for sub_label, sub_widget in widget.items():
                    if isinstance(sub_widget, tuple) and len(sub_widget) == 3:
                        inner_dict[sub_label] = sub_widget[1].get() + sub_widget[2].get()
                    elif isinstance(sub_widget, tuple) and len(sub_widget) == 2:
                        inner_dict[sub_label] = sub_widget[1].get()
                self.data_dict[label_text] = inner_dict
            else:
                print(f"Unknown widget type for {label_text}: {type(widget)}")
        return self.data_dict

# Test için örnek kullanım
if __name__ == "__main__":
    root = customtkinter.CTk()
    root.title("Dynamic Table")
    root.geometry("400x800")
    root.columnconfigure(0, weight=1)

    table = DT(root)
    table.add_row("Name", "Fatma")
    table.add_row("Birth Date", [["Day", "5"], ["Month", ["March", "April"]], ["Year", "1988"]])
    table.add_row("Height", ["160",["cm","inch"]])
    table.add_row("Weight",  ["60",["kg","lb"]])
    table.add_row("Where are you living", ["Turkey", "Germany", "USA", "Australia"])
    table.add_row("Occupation", "Doctor")
    table.add_row("Known Languages", ["Turkish", "German", "English", "French"])
    table.add_row("Specialization", "Cardiology")
    table.add_row("Hobbies", ["Reading", "Hiking", "Cooking"])
    table.add_row("Education", [["Degree", "Doctor of Medicine"], ["University", ["Ankara University Medical School",["mezun","student"]]]])
    table.add_row("Favorite Food", ["Kebab", "Sushi", "Salad"])
    table.add_row("Music Genre", ["Classical", "Jazz", "Pop"])
    table.add_row("Years of Experience", "10")
    table.mainFrame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    # "Education" başlığı altındaki verileri almak için örnek kullanım
    """education_data = table.get_widget("Education")
    if education_data:
        for item in education_data:
            print(f"{item[0]}: {item[1]}")"""
    #print(table.widgets)
    #print(table.find_widget("Education"))
    """print(table.get_widget("Height"))
    print(table.get_widget("Name"))"""
    print(table.all_data_in_wigdet())
    print(table.get_widget("Education"))
    #print(table.widgets)
    ##table.destroy_widget("Name")
    ##table.destroy_widget("Education")

    root.mainloop()

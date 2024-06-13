# dynamic_table.py

import customtkinter as tk
import customtkinter

class DynamicTable:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.mainFrame = customtkinter.CTkScrollableFrame(root)
        self.mainFrame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
        self.widgets = {}

    def add_entry(self, label_text, content):
        if isinstance(content, list):
            if isinstance(content[0], list):
                inner_widgets = {}
                frame_label = customtkinter.CTkTabview(
                    self.mainFrame, corner_radius=10, height=self.root.winfo_screenheight() / 20 * (len(content[0])), width=200
                )
                frame_label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=0, columnspan=3, pady=0, sticky='w')
                frame_label.add(label_text)
                inner_widgets[label_text] = frame_label

                for index, item in enumerate(content):
                    if isinstance(item[1], list):
                        sub_label = customtkinter.CTkLabel(frame_label.tab(label_text), text=item[0], width=150)
                        sub_label.grid(row=index, column=0, padx=5, pady=2, sticky='w')
                        combobox = customtkinter.CTkComboBox(frame_label.tab(label_text), values=item[1])
                        combobox.grid(row=index, column=1, padx=5, pady=2, sticky='e')
                        combobox.set(item[1][0])
                        inner_widgets[item[0]] = (sub_label, combobox)
                    else:
                        sub_label = customtkinter.CTkLabel(frame_label.tab(label_text), text=item[0], width=150)
                        sub_label.grid(row=index, column=0, padx=5, pady=2, sticky='w')
                        entry = customtkinter.CTkEntry(frame_label.tab(label_text))
                        entry.grid(row=index, column=1, padx=5, pady=2, sticky='e')
                        entry.insert(0, item[1])
                        inner_widgets[item[0]] = (sub_label, entry)
                self.widgets[label_text] = inner_widgets
            else:
                label = customtkinter.CTkLabel(self.mainFrame, text=label_text, width=150)
                label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=10, pady=5, sticky='w')
                combobox = customtkinter.CTkComboBox(self.mainFrame, values=content)
                combobox.grid(row=len(self.mainFrame.grid_slaves()) - 1, column=1, padx=10, pady=5, sticky='ew')
                combobox.set(content[0])
                self.widgets[label_text] = combobox
        else:
            label = customtkinter.CTkLabel(self.mainFrame, text=label_text, width=150)
            label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=10, pady=5, sticky='w')
            entry = customtkinter.CTkEntry(self.mainFrame)
            entry.grid(row=len(self.mainFrame.grid_slaves()) - 1, column=1, padx=10, pady=5, sticky='ew')
            entry.insert(0, content)
            self.widgets[label_text] = entry

    def find_widget(self, label_text):
        if label_text in self.widgets:
            widget = self.widgets[label_text]
            if isinstance(widget, dict):
                for key, value in widget.items():
                    if isinstance(value, tuple):
                        return (key, value[1])
            elif isinstance(widget, customtkinter.CTkComboBox) or isinstance(widget, customtkinter.CTkEntry):
                return (label_text, widget)
        else:
            for widgets in self.widgets.values():
                if isinstance(widgets, dict) and label_text in widgets:
                    inner_widget = widgets[label_text]
                    if isinstance(inner_widget, tuple) and len(inner_widget) == 2:
                        return (label_text, inner_widget[1])
                    elif isinstance(inner_widget, customtkinter.CTkComboBox) or isinstance(inner_widget, customtkinter.CTkEntry):
                        return (label_text, inner_widget)
        return None

    def destroy_widget(self, label_text):
        widget_tuple = self.find_widget(label_text)
        if widget_tuple:
            label, widget = widget_tuple
            if isinstance(widget, customtkinter.CTkComboBox) or isinstance(widget, customtkinter.CTkEntry):
                widget.destroy()
            elif isinstance(widget, tuple) and len(widget) == 2 and isinstance(widget[1], customtkinter.CTkComboBox):
                widget[1].destroy()
            elif isinstance(widget, dict):
                for inner_widget in widget.values():
                    if isinstance(inner_widget, tuple) and len(inner_widget) == 2 and isinstance(inner_widget[1], customtkinter.CTkComboBox):
                        inner_widget[1].destroy()

            if isinstance(widget, dict):
                self.widgets[label_text] = None
            else:
                self.widgets.pop(label_text)

    def get_widget(self, label_text):
        widget_tuple = self.find_widget(label_text)
        if widget_tuple:
            label, widget = widget_tuple
            if isinstance(widget, customtkinter.CTkComboBox):
                return widget.get()
            elif isinstance(widget, customtkinter.CTkEntry):
                return widget.get()
            elif isinstance(widget, dict):
                result = []
                for key, value in widget.items():
                    if isinstance(value, tuple) and len(value) == 2:
                        result.append((key, value[1].get()))
                    elif isinstance(value, customtkinter.CTkComboBox):
                        result.append((key, value.get()))
                    elif isinstance(value, customtkinter.CTkEntry):
                        result.append((key, value.get()))
                return result
        return None

    def set_widget(self, label_text, value):
        widget_tuple = self.find_widget(label_text)
        if widget_tuple:
            label, widget = widget_tuple
            if isinstance(widget, customtkinter.CTkComboBox):
                widget.set(value)
            elif isinstance(widget, customtkinter.CTkEntry):
                widget.delete(0, tk.END)
                widget.insert(0, value)

    def clear_widgets(self):
        for widget in self.widgets.values():
            if isinstance(widget, customtkinter.CTkComboBox) or isinstance(widget, customtkinter.CTkEntry):
                widget.destroy()
            elif isinstance(widget, dict):
                for inner_widget in widget.values():
                    if isinstance(inner_widget, tuple) and len(inner_widget) == 2 and isinstance(inner_widget[1], customtkinter.CTkComboBox):
                        inner_widget[1].destroy()
        self.widgets.clear()

# Kütüphaneyi test etmek için örnek bir kod
if __name__ == "__main__":
    root = customtkinter.CTk()
    root.title("Dynamic Table")
    root.geometry("400x800")
    root.columnconfigure(0, weight=1)

    table = DynamicTable(root)
    table.add_entry("Name", "Fatma")
    table.add_entry("Birth Date", [["Day", "5"], ["Month", ["March", "April", "May"]], ["Year", "1988"]])
    table.add_entry("Height (cm)", "160")
    table.add_entry("Weight (kg)", "55")
    table.add_entry("Where are you living", ["Turkey", "Germany", "USA", "Australia"])
    table.add_entry("Occupation", "Doctor")
    table.add_entry("Known Languages", ["Turkish", "German", "English", "French"])
    table.add_entry("Specialization", "Cardiology")
    table.add_entry("Hobbies", ["Reading", "Hiking", "Cooking"])
    table.add_entry("Education", [["Degree", "Doctor of Medicine"], ["University", "Ankara University Medical School"]])
    table.add_entry("Favorite Food", ["Kebab", "Sushi", "Salad"])
    table.add_entry("Music Genre", ["Classical", "Jazz", "Pop"])
    table.add_entry("Years of Experience", "10")

    # Örnek olarak "Education" başlığı altındaki verileri alma ve yazdırma
    education_data = table.get_widget("Education")
    if education_data:
        print("Education:")
        for item in education_data:
            print(f"{item[0]}: {item[1]}")

    root.mainloop()

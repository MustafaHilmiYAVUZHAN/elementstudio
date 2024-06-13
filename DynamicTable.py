# dynamic_table.py

import customtkinter as tk
import customtkinter

class DT:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.mainFrame = customtkinter.CTkScrollableFrame(root)
        self.widgets = {}

    def add_row(self, label_text, content):
        if isinstance(content, list):
            if isinstance(content[0], list):
                inner_widgets = {}
                frame_label = customtkinter.CTkTabview(
                    self.mainFrame, corner_radius=10, height=self.root.winfo_screenheight() / 20 * (len(content[0])), width=200
                )
                frame_label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=0, columnspan=3, pady=0)
                frame_label.add(label_text)
                inner_widgets[label_text] = frame_label

                for index, item in enumerate(content):
                    if isinstance(item[1], list):
                        sub_label = customtkinter.CTkLabel(frame_label.tab(label_text), text=item[0], width=120)
                        sub_label.grid(row=index, column=0, padx=5, pady=2)
                        combobox = customtkinter.CTkComboBox(frame_label.tab(label_text), values=item[1])
                        combobox.grid(row=index, column=1, padx=5, pady=2, sticky='e')
                        combobox.set(item[1][0])
                        inner_widgets[item[0]] = (sub_label, combobox)
                    else:
                        sub_label = customtkinter.CTkLabel(frame_label.tab(label_text), text=item[0], width=120)
                        sub_label.grid(row=index, column=0, padx=5, pady=2)
                        entry = customtkinter.CTkEntry(frame_label.tab(label_text))
                        entry.grid(row=index, column=1, padx=5, pady=2, sticky='e')
                        entry.insert(0, item[1])
                        inner_widgets[item[0]] = (sub_label, entry)
                self.widgets[label_text] = inner_widgets
            else:
                label = customtkinter.CTkLabel(self.mainFrame, text=label_text, width=10)
                label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=10, pady=5)
                combobox = customtkinter.CTkComboBox(self.mainFrame, values=content)
                combobox.grid(row=len(self.mainFrame.grid_slaves()) - 1, column=1, padx=10, pady=5, sticky='ew')
                combobox.set(content[0])
                self.widgets[label_text] = (label, combobox)
        else:
            label = customtkinter.CTkLabel(self.mainFrame, text=label_text, width=10)
            label.grid(row=len(self.mainFrame.grid_slaves()), column=0, padx=10, pady=5)
            entry = customtkinter.CTkEntry(self.mainFrame)
            entry.grid(row=len(self.mainFrame.grid_slaves()) - 1, column=1, padx=10, pady=5, sticky='ew')
            entry.insert(0, content)
            self.widgets[label_text] = (label, entry)

    def find_widget(self, label_text):
        if label_text in self.widgets:
            return self.widgets[label_text]
        else:
            for widgets in self.widgets.values():
                if isinstance(widgets, dict) and label_text in widgets:
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

    def get_widget(self, label_text):
        widget = self.find_widget(label_text)
        if widget:
            if isinstance(widget, dict):
                return [(key, value[1].get()) for key, value in widget.items() if isinstance(value, tuple) and isinstance(value[1], customtkinter.CTkEntry)]
            elif isinstance(widget, tuple):
                return widget[1].get()
            elif isinstance(widget, customtkinter.CTkEntry):
                return widget.get()
        return None
    def get_all_ids(self):
        self.cursor.execute('''
            SELECT id_name FROM Data
        ''')
        return [row[0] for row in self.cursor.fetchall()]

    """    def set_widget(self, label_text, value):
        widget = self.find_widget(label_text)
        if widget:
            if isinstance(widget, dict):
                for key, w in widget.items():
                    if isinstance(w[1], customtkinter.CTkEntry):
                        w[1].delete(0, tk.END)
                        w[1].insert(0, value)
            elif isinstance(widget, customtkinter.CTkComboBox):
                widget.set(value)
            elif isinstance(widget, customtkinter.CTkEntry):
                widget.delete(0, tk.END)
                widget.insert(0, value)"""

    """def clear_widgets(self):
        for widget in self.widgets.values():
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
            else:
                widget.destroy()
        self.widgets.clear()"""

# Test için örnek kullanım
if __name__ == "__main__":
    root = customtkinter.CTk()
    root.title("Dynamic Table")
    root.geometry("400x800")
    root.columnconfigure(0, weight=1)

    table = DT(root)
    table.add_row("Name", "Fatma")
    table.add_row("Birth Date", [["Day", "5"], ["Month", ["March", "April", "May"]], ["Year", "1988"]])
    table.add_row("Height (cm)", "160")
    table.add_row("Weight (kg)", "55")
    table.add_row("Where are you living", ["Turkey", "Germany", "USA", "Australia"])
    table.add_row("Occupation", "Doctor")
    table.add_row("Known Languages", ["Turkish", "German", "English", "French"])
    table.add_row("Specialization", "Cardiology")
    table.add_row("Hobbies", ["Reading", "Hiking", "Cooking"])
    table.add_row("Education", [["Degree", "Doctor of Medicine"], ["University", "Ankara University Medical School"]])
    table.add_row("Favorite Food", ["Kebab", "Sushi", "Salad"])
    table.add_row("Music Genre", ["Classical", "Jazz", "Pop"])
    table.add_row("Years of Experience", "10")
    table.mainFrame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    # "Education" başlığı altındaki verileri almak için örnek kullanım
    education_data = table.get_widget("Education")
    if education_data:
        for item in education_data:
            print(f"{item[0]}: {item[1]}")

    print(table.get_widget("Name"))

    table.destroy_widget("Name")
    table.destroy_widget("Education")

    root.mainloop()

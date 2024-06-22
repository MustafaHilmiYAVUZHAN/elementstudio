import customtkinter as tk
from tkinter import filedialog, messagebox, simpledialog, Canvas
import os
import shutil
from DatabaseManager import DM
from DynamicTable import DT
from Property import CssPropertyManager as cssPM
from Property import DictToCSS as dtCSS
import pywinstyles
class ProjectApplication:
    def __init__(self, root):
        self.root = root
        tk.set_default_color_theme("extreme.json")
        self.root.title("Project Application")
        self.root.geometry("600x300")
        self.root.resizable(0, 0)
        pywinstyles.apply_style(self.root, "acrylic")
        # New Project Button
        self.Big_button_font = tk.CTkFont(size=20)
        self.new_project_button = tk.CTkButton(root, text="New Project", command=self.new_project, font=self.Big_button_font)
        self.new_project_button.place(relx=0.1, rely=0.2, relwidth=0.35, relheight=0.2)
        
        # Old Project Button
        self.old_project_button = tk.CTkButton(root, text="Old Project", command=self.old_project, font=self.Big_button_font)
        self.old_project_button.place(relx=0.1, rely=0.6, relwidth=0.35, relheight=0.2)
        
        # Recently Shown Projects
        self.Font_old_project_text = tk.CTkFont(family='Calibri', size=16, weight="normal")
        self.projects = self.read_project_names("data.txt")
        self.Label_old_document = tk.CTkLabel(root, text="Old Project", font=self.Font_old_project_text)
        self.Label_old_document.place(relx=0.65, rely=0.1)
        self.Font_old_project = tk.CTkFont(family='Arial', size=10, slant='italic')

        # Create a list of labels
        self.labels = []
        for i, (project, file_path) in enumerate(self.projects[:7]):
            label = tk.CTkLabel(root, text=project, cursor="hand2", font=self.Font_old_project, text_color="#888888")
            label.place(relx=0.65, rely=0.25 + i*0.09,relwidth=0.3)
            label.bind("<Button-1>", lambda event, file_path=file_path: self.open_project(file_path))
            self.labels.append(label)

    def read_project_names(self, file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
        projects = [line.strip().split(" - ") for line in lines]
        return projects

    def save_project_path(self, project_directory):
        project_name = os.path.basename(project_directory)
        # Read existing data
        with open("data.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        # Remove any existing line with the same project name
        lines = [line for line in lines if not line.startswith(f"{project_name} -")]
        # Add the new project to the beginning
        new_line = f"{project_name} - {project_directory}\n"
        lines.insert(0, new_line)
        # Trim the list if it exceeds 15 lines
        lines = lines[:15]
        # Write the updated data back to the file
        with open("data.txt", "w", encoding="utf-8") as file:
            file.writelines(lines)

    def check_project_content(self, project_directory):
        # Check the project directory content before opening the new window
        try:
            files = os.listdir(project_directory)
            return True  # No exception means the directory is accessible
        except FileNotFoundError:
            messagebox.showerror("Error", "Directory not found.")
            return False
        except PermissionError:
            messagebox.showerror("Error", "Permission denied.")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            return False

    def show_project_content(self, project_directory):
        # Add files and folders in the project directory to the Listbox
        try:
            files = os.listdir(project_directory)
            for file in files:
                self.file_listbox.insert("end", file)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while listing the directory: {e}")
            return False
    def add_selection(self):
        # Get the current selections
        html_element = self.optionmenu_for_html_element.get()
        align = self.align_values.index(self.optionmenu_for_align.get())+1
        valign = self.valign_values.index(self.optionmenu_for_valign.get())+1
        float_option = self.float_values.index(self.optionmenu_for_float.get())+1
        position = self.position_values.index(self.optionmenu_for_position.get())+1
        self.db_manager.insert_data("id",html_element, int(str(align)+ str(valign)+str(float_option)+str(position)),0,0,0,0,"class_defualt","")
        # Add selections to the list
        self.selections.append(["id",html_element, int(str(align)+ str(valign)+str(float_option)+str(position))])
        self.id_optionmenu.configure(values=self.db_manager.get_all_ids())
        self.id_optionmenu.update()

        # Print the current selections list (for debugging)
        print(self.selections)
    def open_new_window(self, project_directory):
        if self.check_project_content(project_directory):
            
            self.root = root

            self.root.withdraw()  # Hide the main window
            
            self.new_root = tk.CTkToplevel()
            
            self.new_root.title("Project Content")
            
            # Kenarlıkları ve başlık çubuğunu kaldır
            self.new_root.overrideredirect(True)
            
            screen_width = self.new_root.winfo_screenwidth()
            screen_height = self.new_root.winfo_screenheight()
            self.new_root.resizable(0, 0)
            
            # Pencere boyutunu ve konumunu ayarla
            window_width = int(screen_width // 5.6)  # Ekran genişliğinin altıda biri
            window_height = screen_height  # Ekran yüksekliği kadar
            
            # Pencereyi sol üst köşeye konumlandır
            self.new_root.geometry(f"{window_width}x{window_height}+0+0")
            self.new_root.protocol("WM_DELETE_WINDOW", self.new_root.destroy)
            pywinstyles.apply_style(self.new_root,"acrylic")
            self.frame1 = tk.CTkFrame(self.new_root)
            self.frame1.grid(row=0, column=0, padx=10, pady=10)
            
            self.font_for_optionmenu = ("Arial", 12)  # Assuming you have defined this font
            
            # Initialize list to store selections
            self.selections = []
            # Define values for option menus
            self.html_elements = ["Button", "Input", "Label"]
            self.align_values = ["center", "justify", "left", "right"]
            self.valign_values = ["baseline", "top", "middle", "bottom"]
            self.float_values = ["none", "left", "right"]
            self.position_values = ["absolute", "fixed", "static", "relative"]
            self.db_manager = DM('example_database.db')
            self.db_manager.create_table()
            # HTML Element Option Menu
            self.label_html_element = tk.CTkLabel(self.frame1, text="HTML Element")
            self.label_html_element.grid(row=0, column=0, padx=10, pady=10)

            self.optionmenu_for_html_element = tk.CTkOptionMenu(self.frame1, values=self.html_elements, font=self.font_for_optionmenu)
            self.optionmenu_for_html_element.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

            self.label_align = tk.CTkLabel(self.frame1, text="Align")
            self.label_align.grid(row=0, column=1, padx=10, pady=10)

            self.optionmenu_for_align = tk.CTkOptionMenu(self.frame1, values=self.align_values, font=self.font_for_optionmenu)
            self.optionmenu_for_align.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

            self.label_valign = tk.CTkLabel(self.frame1, text="VAlign")
            self.label_valign.grid(row=2, column=0, padx=10, pady=10)

            self.optionmenu_for_valign = tk.CTkOptionMenu(self.frame1, values=self.valign_values, font=self.font_for_optionmenu)
            self.optionmenu_for_valign.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

            self.label_float = tk.CTkLabel(self.frame1, text="Float")
            self.label_float.grid(row=2, column=1, padx=10, pady=10)

            self.optionmenu_for_float = tk.CTkOptionMenu(self.frame1, values=self.float_values, font=self.font_for_optionmenu)
            self.optionmenu_for_float.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

            self.label_position = tk.CTkLabel(self.frame1, text="Position")
            self.label_position.grid(row=4, column=0, padx=10, pady=10)

            self.optionmenu_for_position = tk.CTkOptionMenu(self.frame1, values=self.position_values, font=self.font_for_optionmenu)
            self.optionmenu_for_position.grid(row=5, column=0, padx=10, pady=10, sticky='ew')

            self.add_btn = tk.CTkButton(self.frame1, text="Add", command=self.add_selection)
            self.add_btn.grid(row=5, column=1, padx=10, pady=10)
            #######################
            self.id_optionmenu = tk.CTkOptionMenu(self.new_root,values=self.db_manager.get_all_ids())
            self.id_optionmenu.place(rely=0.3,relx=0.025,relheight=0.03,relwidth=0.95)
            # Sütun genişliklerini eşitleme
            self.frame1.grid_columnconfigure(0, weight=1)
            self.frame1.grid_columnconfigure(1, weight=1)
            self.element_property = tk.CTkTabview(self.new_root)
            self.element_property.place(rely=0.33,relx=0.0125,relheight=0.58,relwidth=0.975)
            self.element_property.add("css")           
            self.table = DT(self.element_property.tab("css"))
            self.css_property_manager = cssPM(self.table)
            self.css_property_manager.add_css_property()

            self.table.mainFrame.pack(side="bottom", fill="both", expand=True, pady=0, padx=0)
            self.update_btn = tk.CTkButton(self.new_root,text="update",command=lambda:print(self.table.all_data_in_wigdet()))
            self.update_btn.place(rely=0.92,relx=0.575,relwidth=0.4)
            print(self.table.all_data_in_wigdet())
            # Add a button to return to the main window
            back_button = tk.CTkButton(self.new_root, text="Back to Main Menu", command=self.back_to_main_menu,hover_color="black")
            back_button.place(rely=0.92,relx=0.025,relwidth=0.4)
            back_button = tk.CTkButton(self.new_root, text="Exit", command=lambda:exit(),hover_color="red")
            back_button.place(rely=0.92,relx=0.45,relwidth=0.1)
            print(dtCSS.dict_to_css(self.table.all_data_in_wigdet()))
            """ # Listbox to show project content
            self.file_listbox = Listbox(self.new_root)
            self.file_listbox.pack(fill="both", expand=True)

            if not self.show_project_content(project_directory):
                self.back_to_main_menu()"""

    def back_to_main_menu(self):
        self.new_root.destroy()  # Close the new window
        self.root.deiconify()    # Show the main window
        
        # Güncel projeleri yeniden yükle
        self.projects = self.read_project_names("data.txt")
        
        # Eski etiketleri temizle
        for label in self.labels:
            label.destroy()
        self.labels.clear()

        # Yeni etiketleri oluştur
        for i, (project, file_path) in enumerate(self.projects[:7]):
            label = tk.CTkLabel(self.root, text=project, cursor="hand2", font=self.Font_old_project, text_color="#888888")
            label.place(relx=0.65, rely=0.25 + i*0.09,relwidth=0.3)
            label.bind("<Button-1>", lambda event, file_path=file_path: self.open_project(file_path))
            self.labels.append(label)


    def create_project(self, target_directory):
        template_directory = "template_dir"  # Specify the path to the template directory
        try:
            # Copy the contents of the template directory to the target directory
            for item in os.listdir(template_directory):
                s = os.path.join(template_directory, item)
                d = os.path.join(target_directory, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)
            messagebox.showinfo("Success", "Project created.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while creating the project: {e}")

    def check_project(self, folder_path):
        required_files = ['option.txt', 'index.html']
        required_folders = ['src', 'data']

        missing_files = [file for file in required_files if not os.path.exists(os.path.join(folder_path, file))]
        missing_folders = [folder for folder in required_folders if not os.path.exists(os.path.join(folder_path, folder))]

        if missing_files or missing_folders:
            error_message = "Missing files: {}\nMissing folders: {}".format(", ".join(missing_files), ", ".join(missing_folders))
            messagebox.showerror("Error", error_message)
        else:
            print("Project is complete and ready.")

    def new_project(self):
        # Create a new project
        target_directory = filedialog.askdirectory()
        if target_directory:
            print("Selected target directory:", target_directory)
            if os.listdir(target_directory):  # If the target directory is not empty
                project_name = tk.CTkInputDialog(title="Project Name", text="Enter the project name:")
                pywinstyles.apply_style(project_name,"acrylic")
                if project_name:
                    target_directory = os.path.join(target_directory, project_name)
                    os.makedirs(target_directory, exist_ok=True)
            self.create_project(target_directory)
            self.save_project_path(target_directory)
            self.open_new_window(target_directory)

    def old_project(self):
        # Select an old project
        folder_path = filedialog.askdirectory()
        if folder_path:
            print("Selected folder path:", folder_path)
            self.check_project(folder_path)
            self.save_project_path(folder_path)
            self.open_new_window(folder_path)

    def open_project(self, file_path):
        print("Opened project file path:", file_path)
        self.save_project_path(file_path)
        self.open_new_window(file_path)

if __name__ == "__main__":
    root = tk.CTk()
    app = ProjectApplication(root)
    root.mainloop()

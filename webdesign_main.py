import customtkinter as tk
from tkinter import filedialog, messagebox, simpledialog, Canvas
import os
import shutil
from DatabaseManager import DM
from DatabaseManager import ValueParser as VP
from SpecialWidgets import DynamicTable as DT
from SpecialWidgets import AdjustableEntry as AE
from SpecialWidgets import AdjustableComboBox as AC
from SpecialWidgets import YesNoDiolog as YND
from Property import CssPropertyManager as cssPM
from WebCodeCreater import CSS
import ctypes
import pywinstyles
from json import dumps
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
        
        position = self.position_values.index(self.optionmenu_for_position.get())+1
        self.id_optionmenu.set(self.db_manager.insert_data(type=html_element,id_name=self.id_entry.get(),padding=int(str(position)),class_=self.optionmenu_for_class.get()))
        # Add selections to the list
        self.id_optionmenu.configure(values=self.db_manager.get_all_ids())
        
        self.id_optionmenu.update()
    
        # Print the current selections list (for debugging)

    def delete_id(self):
        index=self.db_manager.get_all_ids().index(self.id_optionmenu.get())
        self.db_manager.delete_data(self.id_optionmenu.get())
        self.id_optionmenu.configure(values=self.db_manager.get_all_ids())
        try:
            self.id_optionmenu.set(self.db_manager.get_all_ids()[index-1])
        except:
            self.id_optionmenu.set("")
        self.id_optionmenu.update()
    def update_sub_class_chooser(self,class_):
        self.list_sub_class_chooser=CSS.group_by_first_word(CSS.list_css_classes("styles.css"))[class_]
        if 1:
            if len(CSS.find_pseude_class(self.class_values,class_))>1:

                self.pseudo_classes=CSS.find_pseude_class(self.class_values,class_)
                print(self.pseudo_classes)
                self.pseudo_classes[self.pseudo_classes.index("")]=":normal"
                self.pseudo_class_chooser.configure(values=self.pseudo_classes)
                self.pseudo_class_chooser.update()
            else:
                self.pseudo_classes=[":normal"]
                self.pseudo_class_chooser.configure(values=self.pseudo_classes)
                self.pseudo_class_chooser.set(":normal")
                self.pseudo_class_chooser.update()
        self.list_sub_class_chooser[0]="Base"
        self.sub_class_chooser.configure(values=CSS.no_pseudo_class(self.list_sub_class_chooser))
        self.sub_class_chooser.set(self.list_sub_class_chooser[0])


    def update_pseudo_class_chooser(self,sub_class):
        
        self.pseudo_classes=CSS.find_pseude_class(self.list_sub_class_chooser,sub_class)
        self.pseudo_classes[self.pseudo_classes.index("")]=":normal"
        self.pseudo_class_chooser.configure(values=self.pseudo_classes)
        self.pseudo_class_chooser.set(self.pseudo_classes[0])
        if sub_class=="Base":
            self.update_sub_class_chooser(self.class_chooser.get())

    def update_class_tab(self,dict_=None):
        if isinstance(dict_,str):
            self.class_system()
            print("hi")
        else:
            try:
                self.table_for_class.mainFrame.destroy()
            except:
                pass
            self.table_for_class=DT(self.Class_shower,dict_)
            cssPM.add_css_property(self.table_for_class)
            self.table_for_class.mainFrame.grid(row=3,column=0,columnspan=2,sticky="nsew")
            

    def class_system(self,useless=None):
        class_=self.class_chooser.get()
        sub_class=self.sub_class_chooser.get()
        if sub_class=="Base":
            sub_class=""
        pseudo_class=self.pseudo_class_chooser.get()
        if pseudo_class==":normal":
            pseudo_class=""
        css=CSS.css_to_json("styles.css")
        css_code=CSS.return_css(css,class_,sub_class,pseudo_class)
        print(dumps(css_code,indent=2))
        print(type(css_code))
        self.update_class_tab(dict_=css_code)
    def open_new_window(self, project_directory=None,type="ClassShower"):
        if type=="ClassShower":
            self.Class_shower =tk.CTkToplevel()
            self.root = root

            self.root.withdraw()
            self.Class_shower.protocol("WM_DELETE_WINDOW", self.Class_shower.destroy)
            self.Class_shower.title("Classes")
            self.Class_shower.geometry("300x500")
            self.Class_shower.resizable(0, 0)
            pywinstyles.apply_style(self.Class_shower,"acrylic")
            self.class_values =CSS.filter_class(CSS.list_main(CSS.list_css_classes("styles.css")))
            self.class_chooser=tk.CTkOptionMenu(self.Class_shower,values= CSS.no_pseudo_class(self.class_values),command=self.update_sub_class_chooser)
            self.class_chooser.grid(row=0,column=0,pady=5,padx=5,sticky="nsew",columnspan=2)
            self.sub_class_chooser=tk.CTkOptionMenu(self.Class_shower,values=[""],command=self.update_pseudo_class_chooser)
            self.sub_class_chooser.grid(row=1,column=0,pady=5,padx=5,sticky="nsew",columnspan=2)
            self.pseudo_class_chooser=tk.CTkOptionMenu(self.Class_shower,values=[""])#,command=self.update_class_tab
            self.pseudo_class_chooser.grid(row=2,column=0,pady=5,padx=5,sticky="nsew",columnspan=2)
            self.update_table_button=tk.CTkButton(self.Class_shower,text="Get Class",command=self.class_system)
            self.update_table_button.grid(row=4,column=0,pady=5,padx=5,sticky="nsew")
            self.update_sub_class_chooser(self.class_chooser.get())
            self.update_pseudo_class_chooser(self.sub_class_chooser.get())
            self.update_sub_class_chooser(self.class_chooser.get())
            self.save_table_button=tk.CTkButton(self.Class_shower,text="Save Class")
            self.save_table_button.grid(row=4,column=1,pady=5,padx=5,sticky="nsew")
        if self.check_project_content(project_directory) and type=="NewProjectWindow":  
            self.root = root

            self.root.withdraw()  # Hide the main window
            self.new_root = tk.CTkToplevel()
            self.new_root.overrideredirect(True)
  

            screen_width = self.new_root.winfo_screenwidth()
            screen_height = self.new_root.winfo_screenheight()            
            
            
            self.new_root.title("Project Content")
            # Kenarlıkları ve başlık çubuğunu kaldır
            
            self.new_root.protocol("WM_DELETE_WINDOW", self.new_root.destroy)
            self.new_root.resizable(0, 0)
            
            # Pencere boyutunu ve konumunu ayarla
            window_width = int(screen_width // 5.5)  # Ekran genişliğinin altıda biri
            window_height = screen_height  # Ekran yüksekliği kadar
            
            # Pencereyi sol üst köşeye konumlandır
            self.new_root.geometry(f"{window_width}x{window_height}+0+0")
            pywinstyles.apply_style(self.new_root,"acrylic")
            self.frame1 = tk.CTkFrame(self.new_root)
            self.frame1.place(rely=0.015,relx=0.025,relheight=0.32,relwidth=0.95)
            
            self.font_for_optionmenu = ("Arial", 12)  # Assuming you have defined this font
            
            # Initialize list to store selections
            self.selections = []
            # Define values for option menus
            self.html_elements = ["Button", "Input", "Label"]
            self.position_values = ["absolute", "fixed", "static", "relative"]
            self.class_values = CSS.list_css_classes("style.css")
            self.db_manager = DM('example_database.db')
            self.db_manager.create_table()
            # HTML Element Option Menu
            self.label_html_element = tk.CTkLabel(self.frame1, text="HTML Element")
            self.label_html_element.grid(row=0, column=0, padx=10, pady=10)

            self.optionmenu_for_html_element = tk.CTkOptionMenu(self.frame1, values=self.html_elements, font=self.font_for_optionmenu)
            self.optionmenu_for_html_element.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

            self.label_id = tk.CTkLabel(self.frame1, text="Id")
            self.label_id.grid(row=0, column=1, padx=10, pady=10)
            
            self.id_entry = tk.CTkEntry(self.frame1)
            self.id_entry.insert(0, "id")
            self.id_entry.grid(row=1, column=1, padx=10, pady=10)

            self.label_class = tk.CTkLabel(self.frame1, text="Class")
            self.label_class.grid(row=2, column=0, padx=10, pady=10)

            self.optionmenu_for_class = tk.CTkOptionMenu(self.frame1, values=self.class_values, font=self.font_for_optionmenu)
            self.optionmenu_for_class.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

            self.label_position = tk.CTkLabel(self.frame1, text="Position")
            self.label_position.grid(row=2, column=1, padx=10, pady=10)

            self.optionmenu_for_position = tk.CTkOptionMenu(self.frame1, values=self.position_values, font=self.font_for_optionmenu)
            self.optionmenu_for_position.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

            

            self.add_btn = tk.CTkButton(self.frame1, text="Add", command=self.add_selection)
            self.add_btn.grid(row=6, column=0,columnspan=2, padx=10, pady=10,sticky="ew")
            #######################
            self.id_optionmenu = tk.CTkOptionMenu(self.new_root, values=self.db_manager.get_all_ids() or [""],command=self.update_for_new_id)
            self.id_optionmenu.place(rely=0.34,relx=0.05,relheight=0.03,relwidth=0.75)
            # Sütun genişliklerini eşitleme
            self.delete_btn = tk.CTkButton(self.new_root,text="×",fg_color="red",command=lambda:YND("deneme","?",yes_func=lambda:print("+"),no_func=self.delete_id))
            self.delete_btn.place(rely=0.34,relx=0.825,relheight=0.03,relwidth=0.125)
            ###########################################
            self.entry_x = AE(self.new_root, "x",buttons_func=lambda:self.db_manager.update_data(self.id_optionmenu.get(),x=self.entry_x.getDataWithUnit()))
            self.entry_x.SpecialEntryFrame.place(rely=0.38, relx=0.05, relheight=0.03, relwidth=0.9)
            self.entry_x.setValue(VP.get_number(self.db_manager.find_one_data(self.id_optionmenu.get(),"x")))
            self.entry_x.setUnit(VP.get_unit(self.db_manager.find_one_data(self.id_optionmenu.get(),"x")))

            self.entry_y = AE(self.new_root, "y",buttons_func=lambda:self.db_manager.update_data(self.id_optionmenu.get(),y=self.entry_y.getDataWithUnit()))
            self.entry_y.setValue(VP.get_number(self.db_manager.find_one_data(self.id_optionmenu.get(),"y")))
            self.entry_y.setUnit(VP.get_unit(self.db_manager.find_one_data(self.id_optionmenu.get(),"y")))
            self.entry_y.SpecialEntryFrame.place(rely=0.415, relx=0.05, relheight=0.03, relwidth=0.9)
            

            self.entry_width = AE(self.new_root, "width",buttons_func=lambda:self.db_manager.update_data(self.id_optionmenu.get(),width=self.entry_width.getDataWithUnit()))
            self.entry_width.setValue(VP.get_number(self.db_manager.find_one_data(self.id_optionmenu.get(),"width")))
            self.entry_width.setUnit(VP.get_unit(self.db_manager.find_one_data(self.id_optionmenu.get(),"width")))
            self.entry_width.SpecialEntryFrame.place(rely=0.45, relx=0.05, relheight=0.03, relwidth=0.9)

            self.entry_height = AE(self.new_root, "height",buttons_func=lambda:self.db_manager.update_data(self.id_optionmenu.get(),height=self.entry_height.getDataWithUnit()))
            self.entry_height.SpecialEntryFrame.place(rely=0.485, relx=0.05, relheight=0.03, relwidth=0.9)
            self.entry_height.setValue(VP.get_number(self.db_manager.find_one_data(self.id_optionmenu.get(),"height")))
            self.entry_height.setUnit(VP.get_unit(self.db_manager.find_one_data(self.id_optionmenu.get(),"height")))

            self.combobox_position = AC(self.new_root,"Position",values=self.position_values,buttons_func=lambda:self.db_manager.update_data(self.id_optionmenu.get(),padding=int(self.position_values.index(self.combobox_position.getData()))+1))
            self.combobox_position.SpecialComboBoxFrame.place(rely=0.520, relx=0.05, relheight=0.03, relwidth=0.440)
            self.combobox_Class = AC(self.new_root,"Class",values=self.class_values,buttons_func=lambda:self.db_manager.update_data(self.id_optionmenu.get(),class_=self.combobox_Class.getData()))
            self.combobox_Class.SpecialComboBoxFrame.place(rely=0.520, relx=0.51, relheight=0.03, relwidth=0.440)
            self.combobox_html_element = AC(self.new_root,"Type",values=self.html_elements,buttons_func=lambda:self.db_manager.update_data(self.id_optionmenu.get(),type=self.combobox_html_element.getData()))
            self.combobox_html_element.SpecialComboBoxFrame.place(rely=0.555, relx=0.05, relheight=0.03, relwidth=0.440)

            #########################################
            self.frame1.grid_columnconfigure(0, weight=1)
            self.frame1.grid_columnconfigure(1, weight=1)
            self.element_property = tk.CTkTabview(self.new_root)
            self.element_property.place(rely=0.63,relx=0.0125,relheight=0.28,relwidth=0.975)
            self.element_property.add("css")           
            self.table = DT(self.element_property.tab("css"),class_dict=CSS.stringtodict("""display: inline-block;
    background-color: #007bff;
    color: #fff;
    text-decoration: none;
    border-radius: 5px;"""))
            cssPM.add_css_property(self.table)


            self.table.mainFrame.pack(side="bottom", fill="both", expand=True, pady=0, padx=0)
            self.update_btn = tk.CTkButton(self.new_root,text="update",command=lambda:self.toplevel_update(project_directory))
            self.update_btn.place(rely=0.92,relx=0.575,relwidth=0.4)
            print(self.table.all_data_in_wigdet())
            # Add a button to return to the main window
            back_button = tk.CTkButton(self.new_root, text="Back to Main Menu", command=self.back_to_main_menu,hover_color="black")
            back_button.place(rely=0.92,relx=0.025,relwidth=0.4)
            back_button = tk.CTkButton(self.new_root, text="Exit", command=lambda:exit(),hover_color="red")
            back_button.place(rely=0.92,relx=0.45,relwidth=0.1)
            print(CSS.dict_to_css(self.table.all_data_in_wigdet()))
            """ # Listbox to show project content
            self.file_listbox = Listbox(self.new_root)
            self.file_listbox.pack(fill="both", expand=True)

            if not self.show_project_content(project_directory):
                self.back_to_main_menu()"""
    def update_for_new_id(self,id):
        self.entry_x.setValue(VP.get_number(self.db_manager.find_one_data(id,"x")))
        self.entry_x.setUnit(VP.get_unit(self.db_manager.find_one_data(id,"x")))
        self.entry_y.setValue(VP.get_number(self.db_manager.find_one_data(id,"y")))
        self.entry_y.setUnit(VP.get_unit(self.db_manager.find_one_data(id,"y")))
        self.entry_width.setValue(VP.get_number(self.db_manager.find_one_data(id,"width")))
        self.entry_width.setUnit(VP.get_unit(self.db_manager.find_one_data(id,"width")))
        self.entry_height.setValue(VP.get_number(self.db_manager.find_one_data(id,"height")))
        self.entry_height.setUnit(VP.get_unit(self.db_manager.find_one_data(id,"height")))
        self.combobox_Class.setValue(self.db_manager.find_one_data(id,"class"))
        self.combobox_position.setValue(self.position_values[self.db_manager.find_one_data(id,"padding")-1])
        self.combobox_html_element.setValue(self.db_manager.find_one_data(id,"type"))

    def toplevel_update(self,project_directory):
        from SpecialWidgets import DynamicTable as DT
        # def convert_to_id_css(element_type, element_id, avfp, x, y, width, height, element_class,extra_css):
        id= self.id_optionmenu.get()
        print(CSS.convert_to_id_css("",id,self.db_manager.find_one_data(id,"padding"),self.db_manager.find_one_data(id,"x"),self.db_manager.find_one_data(id,"y"),self.db_manager.find_one_data(id,"width"),self.db_manager.find_one_data(id,"height"),self.db_manager.find_one_data(id,"class"),"" ))

        self.back_to_main_menu()
        self.open_new_window(project_directory=project_directory)
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
            self.open_new_window(project_directory=target_directory)
    def old_project(self):
        # Select an old project
        folder_path = filedialog.askdirectory()
        if folder_path:
            print("Selected folder path:", folder_path)
            self.check_project(folder_path)
            self.save_project_path(folder_path)
            self.open_new_window(project_directory=folder_path)

    def open_project(self, file_path):
        print("Opened project file path:", file_path)
        self.save_project_path(file_path)
        self.open_new_window(project_directory=file_path)

if __name__ == "__main__":
    root = tk.CTk()
    app = ProjectApplication(root)
    root.mainloop()

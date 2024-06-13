import sqlite3
"""
    text-align: firstnumber
        center: 0  
        justify: 1
        left: 2
        right: 3
        


    vertical-align: secondnumber
        baseline: 0     
        top: 1   
        middle: 2   
        bottom: 3   

    float: 3. number
        none: 0   
        left: 1 
        right: 2    


    position: 4.number
        absolute: 0 
        fixed: 1    
        static: 2   
        relative: 3   

"""
class DatabaseManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.connect()

    def connect(self):
        self.connection = sqlite3.connect(self.file_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Data(
                number INTEGER PRIMARY KEY,
                id_name TEXT UNIQUE,
                type TEXT,
                padding INTEGER,
                x TEXT,
                y TEXT,
                width TEXT,
                height TEXT,
                class TEXT
            )
        ''')
        self.connection.commit()

    def generate_unique_id_name(self, id_name):
        original_id_name = id_name
        count = 1
        while True:
            self.cursor.execute('''
                SELECT COUNT(*) FROM Data WHERE id_name=?
            ''', (id_name,))
            if self.cursor.fetchone()[0] == 0:
                break
            id_name = f"{original_id_name}{count:03}"
            count += 1
        return id_name

    def insert_data(self, id_name, type, padding, x, y, width, height, class_):
        id_name = self.generate_unique_id_name(id_name)
        self.cursor.execute('''
            INSERT INTO Data (id_name, type, padding, x, y, width, height, class)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id_name, type, padding, x, y, width, height, class_))
        self.connection.commit()
        print(f"Inserted data with id_name: {id_name}")

    def delete_data(self, id_name):
        self.cursor.execute('''
            DELETE FROM Data WHERE id_name=?
        ''', (id_name,))
        self.connection.commit()

    def find_data(self, id_name):
        self.cursor.execute('''
            SELECT * FROM Data WHERE id_name=?
        ''', (id_name,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.connection.close()
    

def convert_to_css(element_type, element_id, avfp, x, y, width, height,element_class):
    avfp=str(avfp)
    align,valign,floating,position=avfp[0],avfp[1],avfp[2],avfp[3]
    css_template = f"""#{element_id} {{
    text-align: {align};
    vertical-align: {valign};
    float: {'none' if floating == '0' else 'left' if floating == '1' else 'right'};
    position: {'absolute' if position == '0' else 'fixed' if position == '1' else 'static' if position == '2' else 'relative'};
    left: {x}px;
    top: {y}px;
    width: {width}px;
    height: {height}px}}"""
    return css_template,element_class

# Usage example
if __name__ == "__main__":
    db_manager = DatabaseManager('example_database.db')
    db_manager.create_table()

    # Attempt to insert data

    db_manager.insert_data('button', 'BTN', 3120, '20', '30', '120', '220', 'example_class_3')
    db_manager.insert_data('button', 'BTN', 3220, '20', '30', '120', '220', 'example_class_3')
    db_manager.insert_data('button', 'BTN', 3021, '20', '30', '120', '220', 'example_class_3')
    db_manager.insert_data('button', 'BTN', 3120, '20', '30', '120', '220', 'example_class_3')
    db_manager.insert_data('button', 'BTN', 3023, '20', '30', '120', '220', 'example_class_3')

    # Find data
    data = db_manager.find_data('button')
    if data:
        print("Found data:", data)
    else:
        print("No data found.")
    print(type(db_manager.find_data('button')))
    _,element_type, element_id, avfp, x, y, width, height,element_class=list(data)
    css_code,_ = convert_to_css(element_type, element_id, avfp, x, y, width, height,element_class)
    print(css_code)
    # Delete data
    db_manager.delete_data('button')

    db_manager.close_connection()

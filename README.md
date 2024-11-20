uml = Digraph("UML Diagram for Animal Management System")

# Define nodes for each class with attributes and methods
uml.node("Animal", '''<<class>> Animal
------------------------
- id: str
- name: str
- much: str
- dep_numb: str''')

uml.node("Cow", '''<<class>> Cow
------------------------
- a_name1: str
------------------------
+ from_input(): classmethod''')

uml.node("Chicken", '''<<class>> Chicken
------------------------
- a_name: str
------------------------
+ from_input(): classmethod''')

uml.node("Database", '''<<class>> Database
------------------------
- conn: sqlite3.Connection
------------------------
+ methods for DB operations''')

# Add inheritance relationships
uml.edge("Animal", "Cow", arrowhead="empty")
uml.edge("Animal", "Chicken", arrowhead="empty")

# Show association between Database and other classes
uml.edge("Cow", "Database", label="uses", style="dashed")
uml.edge("Chicken", "Database", label="uses", style="dashed")

# Render the UML diagram
uml.render("/mnt/data/animal_management_system_uml", format="png", cleanup=True)
"/mnt/data/animal_management_system_uml.png"

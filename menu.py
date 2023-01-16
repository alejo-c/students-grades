from terminal_functions import clear, pause
from database_operations import execute
from types_convertion import is_valid_type, convert_to

DATABASE_NAME = 'studentsgrades.db'
CRUD_OPTIONS: dict = {
    '1': 'create',
    '2': 'read',
    '3': 'read all',
    '4': 'update',
    '5': 'delete',
    '6': 'exit',
}
CRUD_OPERATIONS: dict = {
    'create': 'INSERT INTO {} VALUES(NULL, {})',  # TABLE, VALUES
    'read': 'SELECT * FROM {} {}',  # TABLE, WHERE
    'read all': 'SELECT * FROM {}',  # TABLE
    'update': 'UPDATE {} SET {}',  # TABLE, WHERE
    'delete': 'DELETE FROM {} {}',  # TABLE, WHERE
}
TABLE_OPTIONS: dict = {
    '1': 'grades',
    '2': 'students',
    '3': 'subjects',
    '4': 'back',
}
OBJECTS_FIELDS: dict = {
    'subject': {'name': 'str'},
    'student': {'name': 'str', 'lastname': 'str'},
    'grade': {'student': 'int', 'subject': 'int', 'value': 'float'},
}


def capture_object(new_object_type: str) -> dict:
    new_object = {}
    err_msg = '*Error* The field [{}({})] is empty or the type is invalid'
    print(f'\nCreate new {new_object_type.capitalize()}...')

    for field_name, field_type in OBJECTS_FIELDS[new_object_type].items():
        while True:
            value = input(f'Enter {field_name.capitalize()} [{field_type}]: ')

            if value != '' and is_valid_type(value, field_type):
                value = convert_to(value, field_type)
                break

            pause(err_msg.format(field_name, field_type))

        new_object[field_name] = value

    pause(f'\n{new_object_type.capitalize()} created successfully.')
    return new_object


def capture_id(object_type: str) -> str:
    return input(f'Enter {object_type} id: ')


def get_extra(operation: str, object_type: str) -> str:
    where = ''
    if operation != 'create':
        where = f' WHERE id = {capture_id(object_type)}'

    if operation in ('create', 'update'):
        new_object = capture_object(object_type)
        items = [f'"{v}"' for v in new_object.values()]

        if operation == 'update':
            items = [f'{k} = "{v}"' for k, v in new_object.items()]

        return ', '.join(items) + where  # Create or update return
    return where  # Read or Delete return


def traspose_matrix(matrix):
    return list(map(list, zip(*matrix)))


def display_table(object_type: str, data: list) -> None:
    if data == []:
        pause(f'There is no records in table {object_type.capitalize()}s...\n')
        return

    header = ['Id']
    header.extend([i.capitalize() for i in OBJECTS_FIELDS[object_type].keys()])
    table = [header]

    table.extend([[str(j) for j in i] for i in data])
    sizes = [len(max(i, key=len)) + 2 for i in traspose_matrix(table)]
    print(f'Displaying {object_type.capitalize()}(s)...\n')

    for record in table:
        for i in range(len(record)):
            print(f'{record[i]:<{sizes[i]}}', end='')
        print()
    pause()


def operate(operation: str, table: str) -> None:
    object_type = table[:-1]
    extra = ''
    if operation != 'read all':
        extra = get_extra(operation, object_type)

    expression = CRUD_OPERATIONS[operation].format(table, extra)
    output = execute(DATABASE_NAME, expression)

    if 'read' in operation:
        display_table(object_type, output)


# Menu template
def menu_tpl(title: str, options: dict) -> str or None:
    clear()
    menu = [f'{k}. {v.capitalize()}\n' for k, v in options.items()]
    try:
        menu_option = input(f"{title}\n{''.join(menu)}>> ")
        return options[menu_option]
    except:
        pass


def main_menu() -> None:
    crud_menu_tit = '- STUDENTS GRADES MODULE -\nSelect option...'

    while (crud_opt := menu_tpl(crud_menu_tit, CRUD_OPTIONS)) != 'exit':
        if crud_opt == None:
            pause('*Error* The option is invalid, please try again...')
            continue

        table_menu_tit = f'- SELECT TABLE [{crud_opt}] -'

        while (table_opt := menu_tpl(table_menu_tit, TABLE_OPTIONS)) != 'back':
            if table_opt == None:
                pause('*Error* The option is invalid, please try again...')
                continue

            operate(crud_opt, table_opt)

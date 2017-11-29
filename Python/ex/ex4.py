#-*-coding:utf-8-*-
import sys,shelve
def store_person(db):
    """
    query use for data and store it in the sheft object
    :param db:
    :return:
    """
    pid=input('Enter unique ID num:')
    person={}
    person['name']=input('Enter name:')
    person['age']=input('Enter age:')
    person['phone']=input('Enter phone:')

    db[pid]=person

def lookup_person(db):
    """
    Query use for ID and desired field,and fetch the corresponding data from
    the sheft object
    :param db:
    :return:
    """
    pid=input('Enter ID number')
    field=input('Would you like to know?(name,age,phone)')
    field.strip().lower()
    print(field.capitalize()+':',db[pid][field])


def print_help():
    print("The available command are:")
    print("store: Store information for a person.")
    print("lookup:Look up a person from ID num")
    print("quit:Save changes and exit")
    print("?:Print this message")

def enter_command():
    cmd=input('Enter command(? for help):')
    cmd.strip().lower()
    return cmd

def main():
    database=shelve.open('database.dat')
    try:
        while True:
            cmd=enter_command()
            if cmd=='store':
                store_person(database)
            elif cmd=='lookup':
                lookup_person(database)
            elif cmd=='?':
                print_help()
            elif cmd=='quit':
                return
    finally:
        database.close()
if __name__=='__main__':
    main()
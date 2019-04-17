import sqlite3

make = sqlite3.connect('IoTDatabase.db')
do = make.cursor()

tables = ['soilMoisture','soilTemp','atmosphericTemp','humidity','soilpH']

def create_table():
    for x in tables:
        #do.execute('''CREATE TABLE IF NOT EXISTS %s(id INT NOT NULL AUTO INCREMENT,date TEXT, reading REAL)'''%x)
        do.execute('CREATE TABLE IF NOT EXISTS %s(id integer not null primary key autoincrement, date TEXT, reading REAL)'%x)
    
def data_entry():
    make.commit()
    do.close()
    make.close()
    
if __name__ == '__main__':
    create_table()
    data_entry()

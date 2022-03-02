import mysql.connector as msql

db = msql.connect(
    host='localhost',
    user='root',
    password='',
    database='stuff',
)
cr = db.cursor()
table = "test"

###
# MORE TESTING 
###

having = "artist"
thistag = "'Arti'"
optquotes = r"'{thistag}'"

col2add = ""
col2addafter = ""

rows = r"ALTER TABLE test ADD COLUMN ble VARCHAR(255) AFTER artist"
rows = r"ALTER TABLE test ADD COLUMN id2 INTEGER AUTO_INCREMENT PRIMARY KEY AFTER id"
addcol = r"ALTER TABLE test ADD COLUMN {} AFTER {}".format(
    col2add, col2addafter)
# col2addafter =
# delcol = r"ALTER TABLE test DROP COLUMN id"
# print(rows)
# cr.execute(rows)

link = []
tag = "eloe"
link.append(tag)
# link.append('muk')
# print(link)

# Add Following Tags


populink = r"INSERT INTO test (name) VALUES (%s)"
# cr.execute(populink, link)
# db.commit()

ins = r"INSERT INTO test (name, artist, ble) VALUES (%s, %s, %s)"
record = ("Jonn", "Arti", 6)
# cr.execute(ins, record)
# db.commit()

# Show Records
showrecs = "SELECT * FROM {} WHERE {} = {}".format(table, having, thistag)
showrecs = "SELECT * FROM Test WHERE artist = 'Arti'"
# cr.execute(showrecs)
# recs = cr.fetchone()
# print(recs)


def showtables(x):
    for i in x:
        if i <= 1:
            print(i)
        else:
            for i in x:
                print(i)


# showtables()
###

showrecs = r"ALTER TABLE test ADD COLUMN munk VARCHAR(255)"
# cr.execute(showrecs)
showrecs = r"ALTER TABLE test ADD COLUMN cat VARCHAR(255)"
# cr.execute(showrecs)

columns = []


def showcols():
    col = r"DESC {}".format(table)
    cr.execute(col)
    result = cr.fetchall()
    for i in result:
        columns.append(i[0])


showcols()
print(columns)


def showlastcol():
    col = r"DESC {}".format(table)
    cr.execute(col)
    result = cr.fetchall()
    return(result[-1][0])


lastcol = showlastcol()

print(lastcol)

# Last ID


def showlastid():
    getlastid = r"SELECT LAST_INSERT_ID()"
    cr.execute(getlastid)
    lastid = list(cr.fetchall()[0])[0]
    return(lastid)


lastid = showlastid()

print(lastid)

# Auto Add Tags to their Classes

# INSERT INTO `table_name`(column_1,column_2,...) VALUES (value_1,value_2,...)

# UPDATE employees SET lastname = 'Hill', email = 'mary.hill@classicmodelcars.com' WHERE  employeeNumber = 1056


def IsNotNull(value):
    isnotnull = "SELECT * FROM Test WHERE {} IS NOT NULL"
    try:
        cr.execute(isnotnull.format(value))
    except Exception:
        return False
    else:
        # testing
        print("coucou")
        return True
        # If link exists try adding tags to existing record
        # Add Main Tags
    finally:
        pass

# TESTING
value = "ble"
test = IsNotNull(value)
if test == True:
    print("hoooray")
else:
    print("that")

# isnotnull = "SELECT * FROM Test WHERE {} IS NOT NULL"
# cr.execute(isnotnull.format(value))
# res = cr.fetchone()
# print(res)

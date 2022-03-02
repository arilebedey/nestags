import mysql.connector as msql

db = msql.connect(
    host='localhost',
    user='root',
    password='',
    database='stuff',
)

cr = db.cursor()
table = "Test"

# TESTING SCRIPT

showrecs = "SELECT * FROM Test HAVING id2 = 5"


def DoesColExist(value):
    cr.execute("SELECT * FROM Test WHERE {} IS NOT NULL".format(value))
    return(cr.fetchone)


# LATER Check which of following is better for DoesColExist()
showrecs = "SELECT EXISTS(SELECT * FROM Test WHERE ble IS NOT NULL)"
showrecs = "SELECT * FROM Test WHERE ble IS NOT NULL LIMIT 0, 1"

showrecs = r"ALTER TABLE test ADD COLUMN Link VARCHAR(255)"


# cr.execute(showrecs)
# db.commit()

link = "id2"
llink = []
llink.append(link)
# print(link)
# Check Link existence
populink = r"INSERT INTO Test (Link) VALUES ('{}')".format(link)
# cr.execute(populink)

showrecs = "SELECT * FROM Test WHERE Link = 122"
# cr.execute(showrecs)

# recs = cr.fetchall()
# for i in recs:
#     print(i)

dic = {}
cr.execute("select * from test")
dic['table'] = cr.fetchall()
# print(dic['table'])
for row in range(len(dic['table'])):
    print(dic['table'][row])
# print dic['table'][row]['colum']

# recs = cr.fetchone()
# print(recs)


columns = []


def showcols():
    col = r"DESC {}".format(table)
    cr.execute(col)
    result = cr.fetchall()
    for i in result:
        columns.append(i[0])


# showcols()
# print(columns)


def AddTag(table, value):
    try:
        addcol = r"ALTER TABLE {} ADD COLUMN {} VARCHAR(255)".format(
            table, value)
        cr.execute(addcol)
    except Exception:
        return False


def IsNotNull(table, value):
    isnotnull = r"SELECT * FROM {} WHERE {} IS NOT NULL".format(table, value)
    try:
        # print(isnotnull)
        cr.execute(isnotnull)
    except Exception as e:
        print(e)
        return False
    else:
        return True
        # If link exists try adding tags to existing record
        # Add Main Tags


# tags = ["what"]

# showrecs = "SELECT * FROM Test WHERE Link = 122"
# cr.execute(showrecs)

# recs = cr.fetchall()
# for i in recs:
#     print(i)


# value = "name"
# INN = IsNotNull(table, value)
# if INN == False:
#     print("No existo")
# else:
#     print("exists")

# print(DoesColExist("id2"))


# Sub Query
# SELECT * FROM whateverTable WHERE location IN (SELECT location FROM whateverTable)

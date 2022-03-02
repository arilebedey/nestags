# Check Tag & Return all/some info about it


# Check mult Tags & Return all/some info about it (esp. artist & song)

# Import
import mysql.connector as msql

db = msql.connect(
    host='localhost',
    user='root',
    password='',
    database='stuff',
)

###
# WORKING SCRIPT (MAIN)
###


cr = db.cursor(buffered=True)
table = "test"
textlog = []
# Get & Split Tags
tags = input("Enter your data: ")
tags = tags.split(' ')
elems = len(tags)
#!Evalute Last tag for accidental NoneType because of <space>


def showlastid():
    getlastid = r"SELECT LAST_INSERT_ID()"
    cr.execute(getlastid)
    lastid = list(cr.fetchall()[0])[0]
    return(lastid)

# Define Main Variables: AfterSplit,
# Define Main Function
# ALTER TABLE test ADD history_new VARCHAR(60) To Add Column At The End Of Table


isnotnull = "SELECT * FROM Test WHERE {} IS NOT NULL"

# Link  # !Keep Only YT Link
link = str.format(tags[0])
# Check Link existence
showrecs = "SELECT * FROM {} WHERE linkid = {}".format(table, link)
populink = r"INSERT INTO Test (Link) VALUES ('{}')".format(link)
cr.execute(populink)
# ID
lastid = showlastid()
# Check Tags Existence
## showrecs = "SELECT * FROM {} WHERE {} = {}".format(table, having, thistag)


def IsNotNull(table, value):
    isnotnull = "SELECT * FROM {} WHERE {} IS NOT NULL".format(table, value)
    try:
        cr.execute(isnotnull)
    except Exception as e:
        return False
    else:
        return True
        # If link exists try adding tags to existing record
        # Add Main Tags
    finally:
        pass
        # Add Tag to List of To-Check Tags for parent tag existence & Execute it in separate script upon desire , make list of Checked Tags in Meta Table


def AddTag(table, value):
    try:
        addcol = r"ALTER TABLE {} ADD COLUMN {} VARCHAR(255)".format(
            table, value)
        cr.execute(addcol)
    except Exception:
        return False
    else:
        db.commit()


def GetInsS():
    values = []
    into = []
    for i in range(0, elems):
        into.append(tags[i])
        values.append("%s")
        # Add tags with "," in between
        # Add appropriate number of "%s"
    into = ', '.join(into)
    values = ', '.join(values)
    insert = "\"INSERT INTO {} ({}) VALUES ({})\"".format(table, into, values)
    return(insert)


def GetUpdtS():
    updtvalues = []
    for i in range(1, elems):
        updtvalues.append(tags[i] + " = 'Yes'")
        # Add tags with "," in between
        # Add appropriate number of "%s"
    updtvalues = ', '.join(updtvalues)
    update = "UPDATE {} SET {} WHERE Link = '{}'".format(
        table, updtvalues, link)
    return(update)


value = link
INN = IsNotNull(table, value)
if INN == False:
    a = 0
    AddTag(table, value)
else:
    a = 1

print(a)


def Main():
    for i in range(1, elems):
        value = tags[i]
        INN = IsNotNull(value, table)
        if INN == False:
            try:
                AddTag(table, value)
            except Exception as exp:
                print("INN2 ") + print(exp)
                # Make Insert STTMT with appropriate f-loop (for n tags make n %s's)

                # At the end of Rec-Сreation, Check if Rec is complete
                # Add to tag tag with id row
            else:
                pass
    if a == 0:
        insert = GetInsS()
        try:
            cr.execute(insert)
        except Exception as excep:
            print(excep)
        else:
            db.commit()
    if a == 1:
        update = GetUpdtS()
        try:
            print(update)
            cr.execute(update)
        except Exception as excep:
            print("a=1, err:")
            print(excep)
        else:
            db.commit()


def showrow():
    for srows in cr:
        print(srows)


def showall():
    cr.execute("SELECT * FROM Test")
    output = cr.fetchall()
    for i in output:
        print(i)


showall()

showrecs = "SELECT * FROM Test WHERE Link = 122"
# cr.execute(showrecs)

# recs = cr.fetchall()
# for i in recs:
#     print(i)

# For each tag check existence
# Create row
existencedict = {}


# Make classes for links and diff tag classes

# Make ifs for success affirmation

# Add Tags to Tag Table with Uncategorized/Categoric rows !

# Return Tags & info as dicts w/ lists

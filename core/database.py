try:
    con = lite.connect('db/database.db')
    cur = con.cursor()                  
	cur.execute("INSERT INTO Shell VALUES(1,'xxx','xxx','xxx')")
except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)

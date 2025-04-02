# import psycopg2

# conn = psycopg2.connect("dbname=france user=postgres")
# cur = conn.cursor()
# cur.execute("CREATE TABLE fib (id integer PRIMARY KEY, fib_n varchar);")


a=0
b=1
i = 0
while i<=11:
    if a == 8:
        break
        
    print(a, end = " ")
    a,b = b, a+b
    i+= 1

print("end")
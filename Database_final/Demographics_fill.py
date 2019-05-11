import csv
import psycopg2
import psycopg2.extras
conn_string = "host='localhost' dbname='demo' user='demo' password='demo'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
file1 = open(r'C:\Users\aayus\Desktop\New folder (2)\Data bases\Project\cc-est2017-alldata2015AllPop.csv', 'r', encoding='ISO-8859-1')
file2 = open(r'C:\Users\aayus\Desktop\New folder (2)\Data bases\Project\Table_10_Offenses_Known_to_Law_Enforcement_by_State_by_Metropolitan_and_Nonmetropolitan_Counties_2015 (1).csv', 'r', encoding='ISO-8859-1')
reader1 = csv.reader(file1)
reader2 = csv.reader(file2)
#cursor.execute("INSERT INTO female_demos VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(reader1[1][0],reader1[1][1],reader1[1][2],reader1[1][3],row[15],row[17],row[19],row[21],))
for row in reader1:
    cursor.execute("INSERT INTO IDcodes VALUES (%s,%s,%s,%s)",(row[1],row[2],row[3],row[4],))
    cursor.execute("INSERT INTO female_demos VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(row[3],row[4],row[11],row[13],row[15],row[17],row[19],row[21],))
    cursor.execute("INSERT INTO male_demos VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(row[3], row[4], row[10], row[12], row[14], row[16], row[18], row[20],))
    cursor.execute("INSERT INTO non_hispanic_demos VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[3], row[4], row[34], row[35], row[36], row[37], row[38], row[39],row[40],row[41],row[42],row[43],row[44],row[45],))
    cursor.execute("INSERT INTO hispanic_demos VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[3], row[4], row[58], row[59], row[60], row[61], row[62], row[63],row[64],row[65],row[66],row[67],row[68],row[69],))
for row1 in reader2:
    if(row1[0] != ''):
        for i in range(4,14):
            if not (row1[i] != ''):
                row1[i] = None
        cursor.execute("INSERT INTO violent_crimes VALUES (%s,%s,%s,%s,%s,%s,%s)", (row1[0], row1[2], row1[4], row1[5],row1[6],row1[7],row1[8],))
        cursor.execute("INSERT INTO property_crimes VALUES (%s,%s,%s,%s,%s,%s)", (row1[0], row1[2], row1[10], row1[11], row1[12], row1[13],))
conn.commit()
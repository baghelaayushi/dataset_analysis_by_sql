import psycopg2
import psycopg2.extras

class DemoData:

    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)

    # This procedure is called via app.py, it calls the respective function for each query
    def execution(self,table, query):
        if query == "1":
            return self.find_violent_crimes(table)
        if query == "2":
            return self.find_property_crimes(table)
        if query == "3":
            return self.total_state_crimes(table)
        if query == "4":
            return self.particular_violent_crime(table)
        if query == "5":
            return self.population_and_crimes(table)
        if query == "6":
            return self.particular_table_data(table)
        if query == '7':
            return self.hispanic_two_or_more_races(table)
        if query == '8':
            return self.non_hispanic_alphabetically(table)
        if query == '10':
            return self.insert_into_violent_crimes(table)
        if query == '11':
            return self.update_violent_crimes(table)

        else:
            return [0]

    def check_connectivity(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM violent_crimes LIMIT 1")
        records = cursor.fetchall()
        return len(records) == 1

    def particular_violent_crime(self,table):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if table[1] == "murder":
            cursor.execute("SELECT state,county,murder  From violent_crimes WHERE state = %s",(table[0],))
        if table[1] == "rape_revised":
            cursor.execute("SELECT state,county,rape_revised  From violent_crimes WHERE state = %s",(table[0],))
        if table[1] == "rape_legacy":
            cursor.execute("SELECT state,county,rape_legacy  From violent_crimes WHERE state = %s",(table[0],))
        if table[1] == "robbery":
            cursor.execute("SELECT state,county,robbery  From violent_crimes WHERE state = %s",(table[0],))
        if table[1] == "assault":
            cursor.execute("SELECT state,county,assault  From violent_crimes WHERE state = %s",(table[0],))
        records = cursor.fetchall()
        return records

    def particular_table_data(self,table):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if table[0] == "property_crimes":
            cursor.execute("SELECT state,count(burglary) FROM property_crimes GROUP BY state")
        if table[0] == "violent_crimes":
            cursor.execute("SELECT state,count(rape) FROM violent_crimes GROUP BY state")
        if table[0] == "MALE_demos":
            cursor.execute("SELECT * FROM male_demos ORDER BY state,county")
        if table[0] == "FEMALE_demos":
            cursor.execute("SELECT * FROM female_demos ORDER BY state,county")
        if table[0] == "Non_Hispanic_Demos":
            cursor.execute("SELECT * FROM non_hispanic_demos ORDER BY state,county")
        if table[0] == "Hispanic_Demos":
            cursor.execute("SELECT * FROM hispanic_demos ORDER BY state,county")
        records = cursor.fetchall()
        return records

    def hispanic_two_or_more_races(self,table):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM Hispanic_Demos WHERE Hisp_Two_Or_More_Races_FEMALE > %s ORDER BY State, County",(int(table[0]),))
        records = cursor.fetchall()
        return records

    def population_and_crimes(self,table):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT j1.state,j1.county,burglary,white_only_male FROM (SELECT state,county,burglary FROM property_crimes WHERE  burglary > %s) as j1 join (SELECT State, County, white_only_male FROM male_demos where white_only_male > %s) as j2 ON J1.State = J2.State AND J1.County = J2.County ORDER BY J1.State, J1.County",(int(table[0]),int(table[1]),))
        records = cursor.fetchall()
        return records


    def total_state_crimes(self,table):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT violent_crimes.state, SUM(COALESCE(murder, 0) + COALESCE(rape_revised, 0)+COALESCE(rape_legacy, 0)+COALESCE(robbery, 0)+COALESCE(assault, 0)+COALESCE(burglary, 0) + COALESCE(larceny, 0)+COALESCE(vehicle, 0)+COALESCE(arson, 0)) From violent_crimes,property_crimes WHERE violent_crimes.state = %s and violent_crimes.county = property_crimes.county and property_crimes.state = violent_crimes.state GROUP BY violent_crimes.state",(table[0],))
        records = cursor.fetchall()
        return records

    def find_violent_crimes(self, table):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT state,county, (COALESCE(murder, 0) + COALESCE(rape_revised, 0)+COALESCE(rape_legacy, 0)+COALESCE(robbery, 0)+COALESCE(assault, 0)) as total From violent_crimes WHERE state = %s and county = %s", (table[0],table[1],))
        records = cursor.fetchall()
        return records

    def find_property_crimes(self, table):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT state,county, (COALESCE(burglary, 0) + COALESCE(larceny, 0)+COALESCE(vehicle, 0)+COALESCE(arson, 0)) as total From property_crimes WHERE state = %s and county = %s", (table[0],table[1],))
        records = cursor.fetchall()
        return records

    def male_population(self,table):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT state,county,white_only_male From male_demos WHERE state = %s", (table,))
        records = cursor.fetchall()
        return records

    def non_hispanic_alphabetically(self,table):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        like_pattern = '{}%'.format(table[0])
        cursor.execute('SELECT state,SUM(non_hisp_two_or_more_races_male),SUM(non_hisp_two_or_more_races_female) FROM non_hispanic_demos WHERE state ILIKE %s GROUP BY state', (like_pattern,))
        records = cursor.fetchall()
        return records

    def insert_into_violent_crimes(self,table):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cursor.execute("INSERT INTO violent_crimes VALUES(%s,%s,%s,%s,%s,%s,%s)",(table[0],table[1],table[2],table[3],table[4],table[5],table[6]))
            records = cursor.rowcount
        except:
            records = 0
        self.conn.commit()
        if records == 0:
            return ["you don't have the privelege"]
        else:
            return ['the row has been updated']

    def update_violent_crimes(self,table):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cursor.execute("Update violent_crimes SET murder = (%s) WHERE state = (%s) AND county = (%s)",(int(table[2]),table[0],table[1]))
            records = cursor.rowcount
        except:
            records = 0
        self.conn.commit()
        if records == 0:
            return ["you don't have the privelege"]
        else:
            return ['the row has been updated']




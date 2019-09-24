import psycopg2

def select_all(table_name):
  conn = psycopg2.connect(dbname= 'db', user= 'grok')
  cursor = conn.cursor()
  
  cursor.execute('SELECT * FROM {}'.format(table_name))
  return cursor.fetchall()


#print(select_all('Star'))
#print(select_all('Planet'))

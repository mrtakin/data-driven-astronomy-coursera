import psycopg2
import numpy as np

def column_stats(table, column):
  conn = psycopg2.connect(dbname= 'db', user= 'grok')
  cursor = conn.cursor()
  
  cursor.execute('SELECT {} FROM {}'.format(column, table))
  data = np.array(cursor.fetchall())
  
  return (np.mean(data), np.median(data))
  
#print(column_stats('Star', 't_eff'))

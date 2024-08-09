import streamlit as st
import MySQLdb

# Establishing a connection to the MySQL database
con = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='bunny',
    db='secretkeys'
)

# Creating a cursor object to interact with the database
cor = con.cursor()

# Executing a query to fetch data from the "secret" table
cor.execute("SELECT * FROM secret;")

# Fetching one record from the result set
r = cor.fetchone()

# Closing the database connection
con.close()

# Displaying the fetched data using Streamlit
st.write(r)

# Assigning the fetched values to variables
api_key = r[0]
access_id = r[1]
app_pass = r[2]
app_email = r[3]

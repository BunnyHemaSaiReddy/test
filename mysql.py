import streamlit as st
import mysql.connector
con = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            passwd='bunny',
            auth_plugin='mysql_native_password',
            database='secretkeys'
            
)

cor=con.cursor()
cor.execute("select * from secret;")
r=cor.fetchone()
con.close()
st.write(r)
api_key=r[0]
access_id= r[1]
app_pass=r[2]
app_email=r[3]

import mysql.connector

# Connect to RDS
conn = mysql.connector.connect(
    host="studentdb.c67yg4okchsr.us-east-1.rds.amazonaws.com",
    user="admin",
    password="iamPrathyusha",
    database="University"
)
cursor = conn.cursor()

# Insert Data
cursor.execute("INSERT INTO Students VALUES (2, 'Jane Smith', 22, 'Mathematics')")
conn.commit()

# Fetch Data
cursor.execute("SELECT * FROM Students")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()

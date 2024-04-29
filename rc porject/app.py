from flask import Flask, request, render_template
import os
import pyodbc

app = Flask(__name__)

# Connection string
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:rc-cloud-server.database.windows.net,1433;Database=RC_cloud_database;UID=Saket;PWD=RC@12345678;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'

def get_conn():
    conn = pyodbc.connect(connection_string)
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        paper_no = int(request.form['paper_no'])
        student_id = int(request.form['student_id'])
        question_no = int(request.form['question_no'])
        answer = request.form['answer']

        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO test4 (paper_no, student_id, question_no, answer) VALUES (?,?,?,?)",
            paper_no,
            student_id,
            question_no,
            answer,
        )
        conn.commit()
        return 'Data uploaded successfully!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
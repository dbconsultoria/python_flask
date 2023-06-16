import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/prods')
def emp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM mariadbproject.tbproducts")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/insert', methods=['POST'])
def create_emp():
    try:        
        _json = request.json
        _descricao = _json['descricao']
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO mariadbproject.tbcategories(description) VALUES(%s)"
            bindData = (_descricao)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Category added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Erro ao executar a query: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()
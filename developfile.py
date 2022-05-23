import pymysql
from flaskconnection import app
from sqlconnection import mysql
from flask import jsonify
from flask import request

@app.route("/")
def demo():
     return jsonify("YOUR MYSQL DATABASE CONNECTED")

@app.route('/datas')
def get():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id,first name,last name,password,conform password,dob,gender,mobile number,email,state,country,pincode FROM ourmedia")
        rows = cursor.fetchall()
        respone = jsonify(rows)
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/datas/<int:id>')
def id(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id,first name,last name,password,conform password,email,state,country,pincode FROM ourmedia WHERE id =%s",id)
        rows= cursor.fetchone()
        respone = jsonify(rows)
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/datas', methods=['POST'])
def add():
    try:
        json1 = request.json
        firstname1 = json1['first name']
        lastname1 = json1['last name']
        password1=json1['password']
        cpassword1=json1['conform password']
        dob1=json1['dob']
        gender1=json1['gender']
        mu1=json1['mobile number']
        e1=json1['email']
        s1=json1['state']
        c1=json1['country']
        pc1=json1['pincode']

        if firstname1 and lastname1 and password1 and cpassword1 and dob1 and gender1 and mu1 and e1 and  s1 and c1 and pc1 and request.method == 'POST':
          sql = "INSERT INTO ourmedia(id,first name,last name,password,conform password,dob,gender,mobile number,email,state,country,pincode) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
          user = (firstname1, lastname1, password1, cpassword1, dob1, gender1, mu1, e1, s1, c1, pc1 )
          conn = mysql.connect()
          cursor = conn.cursor()
          cursor.execute(sql,user)
          conn.commit()
          respone = jsonify('added successfully!')
          return respone
        else:
          return "not_found()"

    except Exception as e:
           print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/datas',methods=['PUT'])
def update():
    try:
        json1 = request.json
        id1 = json1['id']
        firstname1 = json1['first name']
        lastname1 = json1['last name']
        password1 = json1['password']
        cpassword1 = json1['conform password']
        dob1 = json1['dob']
        gender1 = json1['gender']
        mu1 = json1['mobile number']
        e1 = json1['email']
        s1 = json1['state']
        c1 = json1['country']
        pc1 = json1['pincode']
        if id1 and firstname1 and lastname1 and password1 and cpassword1 and dob1 and gender1 and mu1 and e1 and  s1 and c1 and pc1 and request.method == 'PUT':
            sql= "UPDATE ourmedia SET first name=%s, last name=%s, password=%s,conform password=%s, dob=%s, gender=%s,mobile number=%s, email=%s,state=%s,country=%s,pincode=%s WHERE id=%s"
            user = (firstname1, lastname1, password1, cpassword1, dob1, gender1, mu1, e1, s1, c1, pc1 )
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql,user)
            conn.commit()
            respone = jsonify('updated successfully!')
            return respone
        else:
            return "not_found()"
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/datas/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ourmedia WHERE id =%s", (id,))
        conn.commit()
        respone = jsonify('deleted successfully!')
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run(debug=True,port=5004)


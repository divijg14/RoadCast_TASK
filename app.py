import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


"""
    API to get data from postgres database
"""
@app.route("/postgres")
def get_postgres():
    try:
        from models import Employees
        dbb = db.get_engine(app, 'mysql') 
        employees=Employees.query.all()
        return  jsonify([e.serialize() for e in employees])
    except Exception as e:
	    return(str(e))


"""
    API to get data from mysql database
"""
@app.route("/mysql")
def get_mysql():
    try:
        from models import Jobs
        jobs=Jobs.query.all()
        return  jsonify([e.serialize() for e in jobs])
    except Exception as e:
	    return(str(e))

if __name__ == "__main__":    
    app.run(debug=True,host='0.0.0.0',port=8080)

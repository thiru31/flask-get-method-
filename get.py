from flask import *  
app = Flask(__name__)  
  
  
@app.route('/login',methods = ['GET'])  
def login():  
      uname=request.args.get('uname')  
      passwrd=request.args.get('pass')  
      if uname=="thirumalai" and passwrd=="pass":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  
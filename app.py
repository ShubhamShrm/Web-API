# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:22:08 2021

@author: shubham.sharma1
"""

from flask import *  

app = Flask(__name__)  
  
@app.route('/')  
def message():  
      return render_template('hello.html')  

@app.route('/passwordcheck', methods = ['POST'])
def password():
      x= request.form['password']
      if x == '1234':
            return('hey')
      else:
            return('Invalid')



if __name__ == '__main__':  
   app.run(debug = True, host='0.0.0.0')  


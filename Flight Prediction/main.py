from flask import Flask,render_template,request
import pickle
app=Flask(__name__)

@app.route('/',methods=['GET'])
def HomePage():
 return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def index():
 if request.method=='POST':
  try:
   month = int(request.form['month'])
   day   = int(request.form['day'])
   schdl_dep = float(request.form['schdl_dep'])
   dep_delay = float(request.form['dep_delay'])
   schdl_arriv = float(request.form['schdl_arriv'])
   divrtd = int(request.form['divrtd'])
   cancld = int(request.form['cancld'])
   air_sys_delay = float(request.form['air_sys_delay'])
   secrty_delay = float(request.form['secrty_delay'])
   airline_delay = float(request.form['airline_delay'])
   late_air_delay = float(request.form['late_air_delay'])
   wethr_delay  = float(request.form['wethr_delay'])

   print('HI')
   filename = 'finalized_model.sav'
   loaded_model = pickle.load(open(filename, 'rb'))


   import numpy as np
   prediction=loaded_model.predict([[month,day,schdl_dep,dep_delay,schdl_arriv,divrtd,cancld,air_sys_delay,secrty_delay,
                                     airline_delay,late_air_delay,wethr_delay]])
   for i in prediction:
    if i==1:
     prediction='will be'
    else:
     prediction='wont get'


   return render_template('results.html',prediction=prediction)
  except Exception as e:
    print('The Exception message is: ',e)
    return 'something is wrong'
 else:
  return render_template('index.html'),

if __name__ == "__main__":
    app.run()

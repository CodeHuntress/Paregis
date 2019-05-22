# html un pitona kopums noziimee, ka taa ir vieta, kur "savienojas" jeb python skripts komunicee ar html lapu.
#
# -*- coding: utf-8 -*-
from flask import Flask,request, render_template
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

 
app = Flask(__name__)
import random 

#--------------------------------- laikapstakli un ... nez :D

siti = ["Sodien bus daudzsolosa diena, lai redzetu skolenu paveikto!", "Jus ieintereses kads projekts!", "Interesantus darbus ir sagadajusi radoso industriju klase!", "10.klases projekti jus patikami parsteigs!"]
laiks = ["saulains", "vejains", "apmacies"]
laiks2 = ["labs", "slikts", "nu taads", "janciigs", "traks"]
laiks3 = ["labs", "slikts", "nu taads", "janciigs", "traks"]
laiks4 = ["labs", "slikts", "nu taads", "janciigs", "traks"]

# -------------------------- horoskopi :D -------------------------

auns = ["Sodien JUs uzzinasiet daudz jauna!", "Sodienas izstade Jus atradisiet, ko interesantu!", "Jums noteikti vajadzetu apskatit blakus esosa galda projektu!", "Zvaignes saka, ka Jums vajadzetu apskatit projektu 'Recognizer'!", "Jums noteikti jaapskata vel citi projekti!"]
versis = ["Jus atradisiet daudz interesanta pie 10.klasu galdiem!", "Jums noderetu apskatit kulturas novirziena projektus!", "Kafijas biezumos ir teikts, ka Jums noteikti ir jaapskata datu bazes!", "Jums noteikti vajadzetu apskatit blakus esosa galda projektu!", "Jums noteikti ir jaapskata 10.klases izveidota spele!"]
dvini = ["Debesis saka, ka Jums deretu apskatit 10.klases portfolio darbus!", "Jums noteikti vajadzetu apskatit blakus esosa galda projektu!", "Jums noderetu apskatit Arduino projektus!", "Sodien Jus uzzinasiet daudz jauna!", "Sodienas izstade Jus atradisiet, ko interesantu!"]
vezis = ["Datu baze 'Skolotaja paligs' Jums dos lielisku piemeru par musu apgutajam zinsaanam!", "Jums noderetu apskatit kulturas novirziena projektus!", "Zvaignes saka, ka Jums vajadzetu apskatit projektu 'Recognizer'!", "Kafijas biezumos ir teikts, ka Jums noteikti ir jaapskata datu bazes!", "Jus atradisiet daudz interesanta pie 10.klasu galdiem!"]
lauva = ["Jums noteikti ir jaapskata 10.klases izveidota spele!", "Veja dzirdams, ka Jums noteikti jaapskata projekts 'Tomati'!", "Jums noteikti vajadzetu apskatit blakus esosa galda projektu!", "Jums noderetu apskatit Arduino projektus!", "Debesis saka, ka Jums deretu apskatit 10.klases portfolio darbus!"]
jaunava = ["Sodienas izstade Jus atradisiet, ko interesantu!", "Jums noderetu apskatit kulturas novirziena projektus!", "Debesis saka, ka Jums deretu apskatit 10.klases portfolio darbus!", "Datu baze 'Skolotaja paligs' Jums dos lielisku piemeru par musu apgutajam zinsaanam!", "Zvaignes saka, ka Jums vajadzetu apskatit projektu 'Recognizer'!"]
svari = ["Jums noderetu apskatit kulturas novirziena projektus!", "Jus atradisiet daudz interesanta pie 10.klasu galdiem!", "Jums noderetu apskatit Arduino projektus!", "Veja dzirdams, ka Jums noteikti jaapskata projekts 'Tomati'!", "Jums noteikti vajadzetu apskatit blakus esosa galda projektu!"]
skorpions = ["Debesis saka, ka Jums deretu apskatit 10.klases portfolio darbus!", "Jus atradisiet daudz interesanta pie 10.klasu galdiem!", "Kafijas biezumos ir teikts, ka Jums noteikti ir jaapskata datu bazes!", "Jums noteikti jaapskata vel citi projekti!", "Datu baze 'Skolotaja paligs' Jums dos lielisku piemeru par musu apgutajam zinsaanam!"]
strelnieks = ["Sodienas izstade Jss atradsiet, ko interesantu!", "Jums noderetu apskatit kulturas novirziena projektus!", "Zvaignes saka, ka Jums vajadzetu apskatit projektu 'Recognizer'!", "Jus atradisiet daudz interesanta pie 10.klasu galdiem!", "Jums noderetu apskatit Arduino projektus!"]
mezazis = ["Jums noteikti jaapskata vel citi projekti!", "Veja dzirdams, ka Jums noteikti jaapskata projekts 'Tomati'!", "Jums noteikti ir jaapskata 10.klases izveidota spele!", "Datu baze 'Skolotaja paligs' Jums dos lielisku piemeru par musu apgutajam zinasanam!", "Kafijas biezumos ir teikts, ka Jums noteikti ir jaapskata datu bazes!"]
udensvirs = ["Sodienas izstade Jus atradisiet, ko interesantu!", "Debesis saka, ka Jums deretu apskatit 10.klases portfolio darbus!", "Jums noteikti vajadzetu apskatit blakus esosa galda projektu!", "Datu baze 'Skolotaja paligs' Jums dos lielisku piemeru par musu apgutajam zinsaanam!", "Jums noteikti ir jaapskata 10.klases izveidota spele!"]
zivis = ["Kafijas biezumos ir teikts, ka Jums noteikti ir jaapskata datu bazes!", "Zvaignes saka, ka Jums vajadzetu apskatit projektu 'Recognizer'!", "Jums noderetu apskatit kulturas novirziena projektus!", "Jums noderetu apskatit Arduino projektus!", "Debesis saka, ka Jums deretu apskatit 10.klases portfolio darbus!"]



# __________________________________________ sakuma laba ar sensoriem un attelu ________	

app.add_url_rule('/images/<path:filename>', endpoint='images', view_func=app.send_static_file)
@app.route("/")
def hello():
  
  # __________________________________________ sesors, ja kada no tiem, c = ej prom preteji c = staavi tur!  ________
  
              while True:
                             GPIO.output(17,GPIO.LOW)
                             GPIO.output(27,GPIO.LOW)
                             GPIO.output(22,GPIO.LOW)
   
   #___________________________________________--  html un pitona kopums
   
                             templateData = {
                                             'time':random.choice(siti),
     
                              
                              
      
      
      
            
                                
      }
 
   
  
                    

                             return render_template('main.html', **templateData)
                            
          
               
               
               
               
               
                # ______________________________________ astotaa lapa_________________________--  
               
@app.route('/astotais', methods=['GET', 'POST'])
def astotais():
         rez = 1
         global rez

  # ______________________________________ formas nolasissana ___________________________________-- 
        
         g='ok' 
         if request.method == 'POST':
                                     rez = request.form['expression']
                                     
                                     return pare()
         else:
              g='ok'
         
               
                                     
# ______________________________________ html un pitona kopums_________________________-- 
                                     
              templateData = {
                                   'aha': g                                 
                  }         
              return render_template('astotais.html', **templateData)
              
              
              
                 # ______________________________________ paregojums_________________________--               
                            

@app.route('/pare')
def pare():

#________________________________________ atkariiba no 8. lapaa formaa ievadiita, izvelk listi_______________
# 

        global rez      
        if rez=='1':
                    p=random.choice(auns)
        
        elif rez =='2':
                       p=random.choice(versis)
        elif rez =='3':
                       p=random.choice(dvini) 
        elif rez =='4':
                       p=random.choice(vezis)                             
        elif rez =='5':
                       p=random.choice(lauva)
        elif rez =='6':
                       p=random.choice(jaunava)              
        elif rez =='7':
                       p=random.choice(svari)
        elif rez =='8':
                       p=random.choice(skorpions)
        elif rez =='9':
                       p=random.choice(strelnieks) 
        elif rez =='10':
                       p=random.choice(mezazis)
        elif rez =='11':
                       p=random.choice(udensvirs)
        elif rez =='12':
                       p=random.choice(zivis)                                                                                      
        else:
             p="jaamaacaas lasiit!!!"
        
        
           
  
  # ______________________________________ html un pitona kopums_________________________-- 
                      
        templateData = {
                                                           'pare': p
                  }         
        return render_template('pare.html', **templateData)
        
        
              
              
@app.route('/mees')
def mees():

#________________________________________ atkariiba no par lapaa ar bildi_______________
# 

       
        
        
           
  
  # ______________________________________ html un pitona kopums_________________________-- 
                      
        templateData = {
                                                       
                  }         
        return render_template('par.html', **templateData)
        
        
              
              
      

                                     
  # ______________________________________ devitaaa lapa___________________________
                                     


                       
@app.route('/devitais')
def devitais():
#laiks = ["saulains", "vejains", "apmacies"]

                global v
    
                v=random.choice(laiks)
                if v=='saulains':
                                  GPIO.output(17,GPIO.HIGH)
                                  GPIO.output(27,GPIO.HIGH)
                                  GPIO.output(22,GPIO.HIGH)
                
               	                   
                                  return desmit()
                elif v=='apmacies':
                                  GPIO.output(17,GPIO.HIGH)
                                  GPIO.output(27,GPIO.LOW)
                                  GPIO.output(22,GPIO.LOW)
                                   
                                  return desmit()
                else : 
                       GPIO.output(17,GPIO.LOW)
                       GPIO.output(27,GPIO.LOW)
                       GPIO.output(22,GPIO.LOW)
                
                      
                       return desmit()
         
  
  # ______________________________________ html un pitona kopums_________________________-- 
                      
                       templateData = {
                                                            'nez':v,
                                                            
                  }         
                       return render_template('devitais.html', **templateData)
                       
                       
                       
@app.route('/desmit')
def desmit():
#laiks = ["saulains", "vejains", "apmacies"]

                global v
    
                
         
  
  # ______________________________________ html un pitona kopums_________________________-- 
                      
                templateData = {
                                                            'nez':v,
                                                            
                  }         
                return render_template('devitais.html', **templateData)                      
                  

                                   

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

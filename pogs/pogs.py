from flask import Flask, render_template


app = Flask(__name__)
import random 
siti = ["karoti", "amuru", "fizikas bibeli", "depresiju"]


@app.route("/")
def hello():
  
   
   templateData = {
     
      'time': random.choice(siti)
      }
   return render_template('main.html', **templateData)



   

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

from flask import *
from fileinput import filename
from rembg import remove
from PIL import Image

app = Flask(__name__)

@app.route("/")
def upload_file():
  return render_template("exemplo.html")

@app.route('/uploader', methods = ['POST'])
def uploader():
  if request.method == 'POST':
     f = request.files['file']
     f.save(f.filename)
     output_path = 'static/teste.png'
     input = Image.open(f.filename)
     output = remove(input)
     output.save(output_path)
     return render_template("link.html")

##Colocar o site no ar
if __name__ == "__main__":
  app.run(debug=True)  

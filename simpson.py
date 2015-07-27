from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    f = subprocess.check_output(['/usr/games/fortune'])
    c = subprocess.check_output(['/usr/games/cowsay', f.decode('ascii')]).decode('ascii')
    
    return '<pre>{}</pre>'.format(c)

if __name__ == '__main__':
    app.run()    

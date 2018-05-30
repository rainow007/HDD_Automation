from app import app
from flask_bootstrap import Bootstrap
app.config['SECRET_KEY'] = 'Life is short,You need Taffy!'
bootstrap = Bootstrap(app)
<<<<<<< HEAD
app.run(debug=True)
=======
# app.run(debug=True)
>>>>>>> the lastst version on 2018/05

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

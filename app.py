from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy 

app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SECRET_KEY']='289d7e3be191adcbd50ada7d932870f84cdf74806358e6bb3ee80f0a49471514'
app.config['SQLALCHEMY_ECHO']=True
app.config['SQLALCHEMY_TRACK_MODIFICATION']=True 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

class Members(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    desc=db.Column(db.String(100))

    def __repr__(self):
        return 'User name is:{}'.format(self.name)

@app.route('/<int:page>')
def index(page):
    # page=request.args.get('page',1,type=int)
    members=Members.query.paginate(per_page=5,page=page,error_out=False)
    return render_template('index.html',members=members)

if __name__=='__main__':
    app.run(debug=True) 

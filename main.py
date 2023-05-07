from flask import Flask,render_template,request,url_for,redirect
from solve import Solve
app=Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
board=[]
previos=[]
text="Suduko"
@app.route("/")

def home():
    
    return render_template("index.html",text=text, board=board,previos=previos)

@app.route("/solve",methods=["POST"])
def solve():
    sudoarray=[]
    global text
    if request.method=="POST":
        
        for i in range(9):
            dd=[]
            
            for j in range(9):

                dd.append(request.form[f"{i}{j}"])
                
            sudoarray.append(dd)
    global previos
    previos= sudoarray
    #error is hear
    sudoko=Solve(sudoarray)
    if sudoko.solve():
        global board
        board=sudoko.board
        text="Suduko"
        return redirect(url_for("home"))
    board=previos
    
    text="fail"
    return redirect(url_for("home"))


if __name__=="__main__":
    app.run( debug=True)

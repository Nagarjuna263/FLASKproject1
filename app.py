from flask import Flask,render_template



FAI=Flask(__name__)



@FAI.route('/hai')
def hai():
    return 'this is first flask project'

@FAI.route('/wish')
def wish():
    return render_template('wish.html')

@FAI.route('/luck/<name>')
def luck(name):
    return f'this is mr/ms {name}'


if __name__=='__main__':
    FAI.run(debug=True)
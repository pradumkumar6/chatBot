from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


@app.route('/')
def abc():
    return render_template('newcha.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        ques = request.form['ques']
        print(' ' + ques)
        return render_template("age.html", ques=ques)
    return render_template('newcha.html')


if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, request

app = Flask(__name__)

#仮データ
tasks = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('title')
        if task:
            tasks.append(task)
    else:   
        #パラメータ取得
        task = request.args.get('title')
        
    return render_template('index.html', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)
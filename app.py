from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        sex = request.form.get('sex')
        hobbys = request.form.getlist('hobby')
        city = request.form.get('city')
        goods = request.form.getlist('good')
        more = request.form.get('more')
        print(
            f'username:{username} '
            f'password:{password} '
            f'sex:{sex} '
            f'hobby:{hobbys} '
            f'city:{city} '
            f'goods:{goods} '
            f'more:{more}'
        )
        return '注册成功'



if __name__=='__main__':
    app.run()
from flask import flash, redirect, render_template, url_for
from app import app
from app.forms import SegitigaForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SegitigaForm()
    if form.validate_on_submit():
        match form.tipe.data:
            case 'ganjil':
                for n in range(form.number.data):
                    if n % 2 != 0:
                        flash(n)
            case 'prima':
                for num in range(1, form.number.data+1):
                    flag = False
                    elif num > 1:
                        for i in range(2, num):
                            if (num % i) == 0:
                                flag = True
                                break
                    if not flag:
                        flash(num)
                        
            case _:
                number = [*str(form.number.data)]
                for n in range(len(number)):
                    flash(number[n] + ''.join(['0' for i in range(n+1)]))

        redirect(url_for('index'))
    return render_template('index.html', form=form)

import csv

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/')
def home():
    return render_template('index.html')


# def write_to_txt(data):
#     with open('database.txt', mode='a') as database_txt:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         txt_writer = database_txt.write(
#             f'Email: {email}\nSubject: {subject}\nMessage: {message}\n\n')


def write_to_csv(data):
    with open('database.csv', newline='\n', mode='a') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database_csv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_txt(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not saved to database.'
    else:
        return redirect('/error.html')

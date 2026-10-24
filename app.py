from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Sangeetha Sree Selva Kumar! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    return render_template('favorite-course.html',
                           subject=subject,
                           course_number=course_number)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    submitted = request.method == 'POST'
    return render_template('contact.html',
                           submitted=submitted,
                           form=request.form)

if __name__ == '__main__':
    app.run()
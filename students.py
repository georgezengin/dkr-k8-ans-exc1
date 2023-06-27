from flask import Flask, request

app = Flask(__name__)
@app.route('/welcome', methods=['GET'])
def getstudents():
    if request.method == 'GET':
        return '<h1> hodi say\'s hi</h1>'

@app.route('/gz', methods=['GET'])
def getstudentsgz():
    if request.method == 'GET':
        return '<h1> george say\'s hi</h1>'

@app.route('/')
def getstudentsroot():
    if request.method == 'GET':
        return '<h1>wazzzzaaaaaaaaaap!?</h1>'

def main():
    app.run(host="0.0.0.0", port=5200, debug=True)


if __name__ == '__main__':
    main()

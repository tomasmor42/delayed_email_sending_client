from flask import Flask, render_template, request, jsonify
from service import add_email_to_emails, get_last_tasks

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    return render_template("send_email.html")

@app.route("/response", methods=['POST'])
def send_email():
    text = request.form.get('text')
    timer = int(request.form.get('timer'))
    add_email_to_emails(text, timer)
    return jsonify({"text":text, "timer": timer}), 201

@app.route("/last_tasks", methods=['GET'])
def last_tasks():
    emails = get_last_tasks()
    return render_template("last_emails_list.html", emails=emails)

if __name__ == '__main__':
    app.run(debug=True)
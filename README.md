# delayed_email_sending_client

This is a minilalistic service that sends emails with a delay. 
To start it locally you have to: 
* clone repo this repo, cd to the folder delayed_email_sending_client
* create a virtual environment `python -m venv venv` 
* set env variable SENDGRID_API_KEY with your sendgrid key
* install requirements from requirements.txt `pip install -r requirements.txt`
* then you can start it with `python app.py`

If you go to main url (localhost:5000/ in default settings) you'll see a form where you can enter a text and delay (in seconds) you want to have for your email. In this repo outgoing and incoming email addresses are dummy, feel free to update them. 
If you go to url /last_tasks you'll see a list of last 10 scheduled emails. 

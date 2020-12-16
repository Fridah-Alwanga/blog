export SECRET_KEY='fridah'

export MAIL_USERNAME='fridahalwanga6@gmail.com'
export MAIL_PASSWORD='38642204'

python3 manage.py server

heroku config:set MAIL_PASSWORD='38642204'
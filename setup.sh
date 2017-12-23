pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python create_user.py
echo "User: admin Password: demodemo"
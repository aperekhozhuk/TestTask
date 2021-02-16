python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python project/manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(username='$SUPERUSER_NAME').exists() or User.objects.create_superuser(username='$SUPERUSER_NAME', password='$SUPERUSER_PASSWORD')" | python project/manage.py shell

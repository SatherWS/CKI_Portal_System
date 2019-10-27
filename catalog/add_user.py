from django.contrib.auth.models import User

user = User.objects.create_user('test_user2', 'random@email.com', 'fakepassword')

user.first_name = 'John'
user.last_name = 'Wick'
user.save()
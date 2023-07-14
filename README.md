# django-rest-registration-nested-register-serializer

This repository contains a minimal Django project reproducing issue [#259 of the django-rest-registration project](https://github.com/apragacz/django-rest-registration/issues/259).

This issue prevents using a custom [register serailizer](https://django-rest-registration.readthedocs.io/en/latest/detailed_configuration/register.html#register-serializer-class) that contains a [nested serializer](https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects).

To reproduce the issue, follow these steps:

1.  Clone this repository
2.  Initialize a virtual environment:

        cd $THIS_REPO
        pipenv install

3.  Run the database migrations:

        cd $THIS_REPO
        cd nested_register_serializer
        ./manage.py migrate

4.  Run the Django development server:

        ./manage.py runserver

5.  Invoke the register endpoint:

        curl -i localhost:8000/accounts/register/ \
             --json '{"username":"user1", "password":"user1-password", "password_confirm":"user1-password", "primary_channel": {"name":"user1-channel"}}'

This results in a 500 error response with the message:

    ValueError at /accounts/register/
    Cannot assign "OrderedDict([('name', 'user1-channel')])": "User.primary_channel" must be a "Channel" instance.

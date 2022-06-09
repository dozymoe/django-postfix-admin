--------------------
Django Postfix Admin
--------------------

Manages postfix + dovecot setup with Django website.

This is a complete website, not modular or modules only. I will try to make one
later.

Setup
-----

    > git clone https://github.com/dozymoe/django-postfix-admin-web --recursive --shallow-submodules
    > cd django-postfix-admin-web
    > ln -s runner-development.json etc/runner.json
    > ./run setup

check ./etc/ for configuration
check ./var/runit/ for example of running as a service

    > ./run waf
    > ./run django-manage --project=web migrate

need to create Django site that matches your server hostname

    > ./run django-manage shell
    > > from django.contrib.sites.models import Site
    > > site = Site.objects.all()[0]
    > > site.domain = '127.0.0.2'
    > > site.name = "My Mail Server"
    > > site.save()
    > > quit

create admin user

    > ./run django-manage createsuperuser

you need to create your own ./etc/runner-VARIANT.json and all the files that
look like ./\*-VARIANT*

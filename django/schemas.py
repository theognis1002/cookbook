# in myapp/apps.py

from django.db.backends.signals import connection_created


class MyappConfig(AppConfig):
    name = "myapp"

    def ready(self):
        from myapp.schema_manager import new_connection

        connection_created.connect(new_connection)


# myapp/schema_manager.py


def new_connection(sender, connection, **kwargs):
    search_path = ["public"] + get_current_schemas()  # fetch the active schemas

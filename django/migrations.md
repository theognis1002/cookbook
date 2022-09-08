Short answer

`python manage.py migrate --fake` does not apply the migration
`python manage.py migrate --fake-initial` might, or might not apply the migration

## Longer answer:

`--fake`: Django keeps a table called django_migrations to know which migrations it has applied in the past, to prevent you from accidentally applying them again. All `--fake` does is insert the migration filename into that table, without actually running the migration. This is useful if you manually changed the database schema first, and the models later, and want to bypass django's actions. However, during that step you are on your own, so take care that you don't end up in an inconsistent state.

`--fake-initial`: depends on the state of the database

all of the tables already exist in the database: in that case, it works like `--fake`. Only the names of the tables are checked, not their actual schema, so, again, take care
none of the tables already exist in the database: in that case, it works like a normal migration
some of the table already exist: you get an error. That's not supposed to happen, either you take care of the database, or django does.
Note that, `--fake-initial` is only taken into account if the migration file has initial=True in its class, otherwise the flag is ignored. Also, this is the only documented usage of initial=True in migrations.

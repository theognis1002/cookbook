from django.db.models import F

"""
class F¶
An F() object represents the value of a model field, transformed value of a model field, or annotated column. It makes it possible to refer to model field values and perform database operations using them without actually having to pull them out of the database into Python memory.

Instead, Django uses the F() object to generate an SQL expression that describes the required operation at the database level.

"""

reporter = Reporters.objects.get(name="Tintin")
reporter.stories_filed = F("stories_filed") + 1
reporter.save()

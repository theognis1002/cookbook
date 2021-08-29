"""
Complex lookups with Q objects¶
"""
from django.db.models import Q

Q(question__startswith="Who") | Q(question__startswith="What")
"""This is equivalent to the following SQL WHERE clause:

WHERE question LIKE 'Who%' OR question LIKE 'What%'"""

Poll.objects.get(
    Q(question__startswith="Who"),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
)
"""
… roughly translates into the SQL:

SELECT * from polls WHERE question LIKE 'Who%'
    AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')
"""
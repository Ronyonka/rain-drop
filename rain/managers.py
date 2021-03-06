from django.db.models import QuerySet, Manager
import datetime

date_start, date_end = datetime.datetime.today().replace(month=1, day=1), datetime.datetime.today()


class GenericQuerySet(QuerySet):
    def filter_by_date(self, date_start, date_end):
        return self.filter(date__range=[date_start, date_end])


class GeneralManager(Manager):
    def get_queryset(self):
        return GenericQuerySet(self.model, using=self._db)
from datetime import datetime
from django.db.models import Q
from functools import reduce
import operator

from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from scraper.models.eksisozlukbot import Entry
from scraper.serializers.entries import EksiSozlukEntrySerializer


class EksiSozlukEntryViewSet(GenericViewSet):
    serializer_class = EksiSozlukEntrySerializer
    queryset = Entry.objects.all()

    def get_queryset(self):
        title = self.request.query_params.get('title')
        after_ts = self.request.query_params.get('after_ts')
        before_ts = self.request.query_params.get('before_ts')

        if not title:
            raise ValidationError('Please provide title in the query!')

        filter_params = [Q(title__icontains=title)]
        try:
            if after_ts:
                filter_params += [Q(created_date__gte=datetime.utcfromtimestamp(int(after_ts)))]            
            if before_ts:
                filter_params += [Q(created_date__lt=datetime.utcfromtimestamp(int(before_ts)))]
        except:
            raise ValidationError('Please provide integer value')
        return self.queryset.filter(reduce(operator.and_, filter_params)).order_by('-created_date')

    def list(self, request: Request, *args, **kwargs) -> Response:
        """Return a list of entries whose title contains title given in the query.
        Parameters:
            title: string - Which title entries will be returned from
            after_ts: int - Timestamp which will be used for getting entries created after this timestamp (in seconds)
            before_ts: int - Timestamp which will be used for getting entries created before this timestamp (in seconds)
        """
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(
            data={'count': queryset.count(), 'results': serializer.data},
            status=HTTP_200_OK,
        )

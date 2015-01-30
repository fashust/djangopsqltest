
import time

from django.http import HttpResponse

from .models import PoolTestModels


def pooling_test(request):

    start_time = time.time()
    for i in xrange(100000):
        PoolTestModels.objects.create(name=str(i))
    end_time = time.time()

    return HttpResponse("Operation took {}".format(end_time - start_time))

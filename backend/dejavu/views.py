from rest_framework.response import Response
from rest_framework.views import APIView
from dejavu.serializers import DaySerializer
from dejavu.models import Day


class DayApiView(APIView):

    def get(self, request):
        """
            Returns days list
        """
        days = Day.objects.all()
        serialized = DaySerializer(days, many=True)
        return Response(serialized.data)

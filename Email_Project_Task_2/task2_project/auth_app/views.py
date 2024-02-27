from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
import logging

logger = logging.getLogger('mylogger')

@api_view(http_method_names=['POST'])
def user(request):
    if request.method == 'POST':
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            logger.info('the emp is created')
            return Response(data=serializer.data, status=201)
        except:
            logger.error('this data saved with errprs')
            return Response(data= serializer.errors, status=400)
        
    

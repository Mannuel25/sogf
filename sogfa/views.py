from rest_framework import viewsets
from .serializers import BookSerializer, MessageSerializer
from .models import Books, Messages
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import FileResponse
import pywhatkit

class BooksViewset(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class MessagesViewset(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer


@api_view(['GET'])
def download_message(request, pk):
    try:
        msg = Messages.objects.get(id=pk)
        response = FileResponse(open(str(msg.message), 'rb'), as_attachment=True,)
        msg.no_of_downloads += 1
        msg.save()
        response['status_code'] = status.HTTP_200_OK
        return response
    except Messages.DoesNotExist:
        return Response({"download" : "failed"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def download_book(request, pk):
    try:
        book = Books.objects.get(id=pk)
        pywhatkit.sendwhatmsg_instantly('+2348152823306', f"Good day, please I'd love to get {str(book.title).title()} by {str(book.author).title()}")
        book.no_of_requests += 1
        book.save()
        return Response({"request_sent" : "true"}, status=status.HTTP_200_OK)
    except Books.DoesNotExist:
        return Response({"request_sent" : "false"}, status=status.HTTP_404_NOT_FOUND)

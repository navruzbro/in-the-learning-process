from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

#from rest_framework.viewsets import ModelViewset

# Create your views here.
# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#API by funcsion (odatda ishlatilmaydi lekin qib kuramiz)
# @api_view(['GET'])
# def book_list_view(request, *args, **kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
# DELETE UPDATE

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer



# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#second part ||
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#simple and long view...
class BookListApiView(APIView):#GET
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        
        data = {
            "status":"True",
            "books":serializer_data
        }
        return Response(data)

#create   
class BookCreateApiView(APIView):#post
    
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception = True):
            books = serializer.save() 
            data = {"status": "book saved to the database",
                    "books": data }
            return Response(data)
        else:
            return Response(
                {
                    "status":False,
                    "message":"serializer is not valid"
                }, status = status.HTTP_400_BAD_REQUEST
            )
class BookDetailApiView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer_data = BookSerializer(book).data 

        data = {
            "status": True,
            "book":serializer_data
        }
        return Response(data)
    
class BookDeleteApiView(APIView):
    
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(
                {
                    "status":True,
                    "message":"Successfully deleted"
                },status = status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    "status":False,
                    "message":"Book is not found"
                },status = status.HTTP_400_BAD_REQUEST
            )
class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data 
        serializer = BookSerializer(instance = book, data = data, partial = True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()  
        return Response(
            {
                "status":True,
                "message":f"Book {book_saved} updated successfully"
            }, status = status.HTTP_200_OK
        )

#viewset ---
# class BookViewset(ModelViewset):
#     queryset  = Book.objects.all()
#     serializer_class =  BookSerializer
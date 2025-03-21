from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from main.models import *
from main.serializers import *


# class QoshiqchiAPIView(APIView):
#     def get(self, request):
#         qoshiqchilar = Qoshiqchi.objects.all()
#         serializer = QoshiqchiSerializer(qoshiqchilar, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = QoshiqchiPostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
# class QoshiqchiRetrieveUpdateDeleteAPIView(APIView):
#     def get(self, request, pk):
#         qoshiqchilar = Qoshiqchi.objects.get(pk=pk)
#         serializer = QoshiqchiSerializer(qoshiqchilar)
#         return Response(serializer.data)
#     def put(self, request, pk):
#         qoshiqchilar = Qoshiqchi.objects.get(pk=pk)
#         serializer = QoshiqchiSerializer(qoshiqchilar, data=request.data)
#         if serializer.is_valid():
#             qoshiqchilar.save()
#             res = {
#                 'success': True,
#                 'massage': 'Qo\'shiqchi muvaffaqiyatli o\'zgartirildi!',
#                 'data': serializer.data
#             }
#             return Response(res, status=200)
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, pk):
#         qoshiqchilar = Qoshiqchi.objects.get(pk=pk)
#         qoshiqchilar.delete()
#         return Response({"success": True, "massage": "Qo\'shiqchi o'chirildi!"}, status=204)

class MyPageNumberPegination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100

class QoshiqchiModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    filter_backends = [SearchFilter,OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['tugilgan_yil']
    search_fields = ['ism', 'davlat']
    ordering_fields = ['ism']
    pagination_class = MyPageNumberPegination

    def get_serializer_class(self):
        if self.action == 'albom_qoshish':
            return AlbomSerializer
        return QoshiqchiSerializer

    @action(detail=True, methods=['get'])
    def albomlar(self, request, pk):
        qoshiqchi = get_object_or_404(Qoshiqchi, pk=pk)
        a = qoshiqchi.alboms.all()
        serializer = AlbomSerializer(a, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['post'])
    def albom_qoshish(self, request, pk):
        qoshiqchi = get_object_or_404(Qoshiqchi, pk=pk)
        albom_serializer = AlbomSerializer(data=request.data)
        if albom_serializer.is_valid():
            albom_serializer.save()
            albom = albom_serializer.instance
            qoshiqchi.albom.add(albom)
            return Response({'success': True, 'message': "Albom yaratildi!"}, status=201)
        return Response(albom_serializer.errors, status=400)


class AlbomModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    filter_backends = [SearchFilter,OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['sana']
    search_fields = ['nom']
    ordering_fields = ['nom']
    pagination_class = MyPageNumberPegination

    def get_serializer_class(self):
        if self.action == 'jadvallar':
            return JadvalSerializer
        return AlbomSerializer

    @action(detail=True, methods=['get'])
    def jadvallar(self, request, pk):
        albom = get_object_or_404(Albom, id=pk)
        a = albom.jadval.all()
        serializer = AlbomSerializer(a, many=True)
        return Response(serializer.data)


class JadvallarModelViewSet(ModelViewSet):
    queryset = Jadval.objects.all()
    filter_backends = [SearchFilter,OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['davomiylik']
    search_fields = ['nom', 'janr']
    ordering_fields = ['nom']
    pagination_class = MyPageNumberPegination

    def get_serializer_class(self):
        return JadvalSerializer



from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.serializers import CountrySerializer, CitySerializer
from api.models import Country, City


class CountryViewSet(ViewSet):

    def list(self, request):
        queryset = Country.objects.order_by('pk')
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Country.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CountrySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            return Response(status=404)
        serializer = CountrySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CityViewSet(ViewSet):

    def list(self, request):
        queryset = City.objects.order_by('pk')
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = City.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CitySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response(status=404)
        serializer = CitySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

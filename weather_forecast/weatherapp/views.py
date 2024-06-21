import json
import logging

from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import OpenWeatherMapData, UserQuery
from .serializers import UserQuerySerializer
from .weather_service import OpenWeathermapService

logger = logging.getLogger('default')


class WeatherApi(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserQuerySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # save the user request
            user_query: UserQuery = serializer.save()
            # query the database for the weather data
            open_weather_map_data: OpenWeatherMapData = OpenWeatherMapData.objects.filter(
                lat=user_query.lat, lon=user_query.lon).first()

            if not open_weather_map_data:
                success, response = self._fetch_weather_data(user_query)
                if success:

                    return Response(data=response, status=status.HTTP_200_OK)
                else:
                    if response:
                        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(data=dict(error='Failed to connect weather service'),
                                        status=status.HTTP_503_SERVICE_UNAVAILABLE)
            else:
                # check if the cache time is over
                if open_weather_map_data.is_old_data():
                    success, response = self._fetch_weather_data(user_query)
                    if success:
                        data = self._get_response_data(user_query, response=response)
                        return Response(data=data, status=status.HTTP_200_OK)
                    else:
                        if response:
                            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response(data=dict(error='Failed to connect weather service'),
                                            status=status.HTTP_503_SERVICE_UNAVAILABLE)
                else:
                    data = self._get_response_data(user_query, weather_data=open_weather_map_data)
                    return Response(data=data, status=status.HTTP_200_OK)

    def _fetch_weather_data(self, user_query: UserQuery):
        weather_service = OpenWeathermapService(lat=user_query.lat, lon=user_query.lon)
        success, response = weather_service.fetch_data()
        if success:
            # save the weather data
            obj, created = OpenWeatherMapData.objects.update_or_create(
                lat=user_query.lat, lon=user_query.lon,
                defaults=dict(timestamp=timezone.now(), response=json.dumps(response))
            )
            if created:
                logger.info("Created new cache entry")
            else:
                logger.info("Updated cache data")

        return success, response

    def _get_response_data(self, user_query: UserQuery, response=None, weather_data: OpenWeatherMapData = None):
        if weather_data:
            weather_data = json.loads(weather_data.response)
            return weather_data.get(user_query.detailing_type)
        else:
            return response.get(user_query.detailing_type)

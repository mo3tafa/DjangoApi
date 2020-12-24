from django.shortcuts import render
from json import JSONEncoder
from django.http import JsonResponse
from django.db import connections
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class Post(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.list_view(request)
        else:
            return JsonResponse(
                status=405,
                data={
                    'status': 'error', 'message': 'Method Not Allowed'
                }
            )

    def list_view(self, request):
        try:
            cursor = connections['postgres'].cursor()
            # cursor.execute('''SELECT * FROM public."api_post" LIMIT 5''')
            cursor.execute(
                '''SELECT * FROM api_post'''
            )
            row = self._dictfetchall(cursor)
            cursor.close()
            return JsonResponse(data=row, encoder=JSONEncoder, safe=False)
        except Exception as e:
            raise e

    def _dictfetchall(self, cursor):
        """Return all row from a cursor as a dict"""
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


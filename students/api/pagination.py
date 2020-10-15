from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StudentsRatingsPagination(PageNumberPagination):

    page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'students': self.page.paginator.count,
            'grade': self.request.user.grade,
            'ratings': data
        })

from rest_framework.response import Response


def response(status: bool, message: str, data=None, http_status=200):

    return Response(
        {
            "status": status,
            "message": message,
            "data": data,
        },
        status=http_status
    )

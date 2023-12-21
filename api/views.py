from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from datetime import datetime


# Create your views here.
@api_view(["GET"])
def get_popular_funds(request):
    api_url = "https://groww.in/v1/api/data/mf/web/v1/collection"

    params = {
        "actTime": datetime.now().timestamp() * 1000,
        "cid": "popular_direct_mf",
        "doc_required": False,
    }

    try:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()

            return Response({"success": True, "result": data})
        else:
            return Response(
                {"error": f"Failed to fetch data. Status code: {response.status_code}"},
                status=response.status_code,
            )
    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=500)


@api_view(["GET"])
def get_meta_data(request):
    api_url = "https://groww.in/v1/api/data/mf/web/v1/scheme/meta_data"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            data_field = data.get("data", {})

            return Response({"success": True, "result": data_field})

        else:
            return Response(
                {"error": f"Failed to fetch data. Status code: {response.status_code}"},
                status=response.status_code,
            )
    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=500)

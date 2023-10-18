from typing import List
from ninja import NinjaAPI



api = NinjaAPI()

@api.get("/transactions")
def todos(request):
    return "list all transactions"
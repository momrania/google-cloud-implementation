
import logging
import os
from pathlib import Path
from concurrent import futures

import grpc

import demo_pb2
import demo_pb2_grpc
from agent import recommend

BASE = "https://openrouter.ai/api/v1"
KEY = os.environ.get("OPENROUTER_API_KEY", "LOLOLLOLOL")
HEADERS = {"Authorization": f"Bearer {KEY}"}

#We should pick a model so that we can remove these from the args list
MODEL = None
CALLS = 0
COST = 0.0
BUDGET = 50
PORT = 8080

BASE_DIR = Path(__file__).resolve().parent.parent
logging.basicConfig( level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


class RecommendationService(demo_pb2_grpc.RecommendationServiceServicer):
    def ListRecommendations(self, request, context):
        product_ids = recommend(user_id=request.user_id,excluded_ids=request.product_ids)
        response=demo_pb2.ListRecommendationsResponse()
        response.product_ids.extend(product_ids)
        return response

def main():

  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  demo_pb2_grpc.add_RecommendationServiceServicer_to_server(RecommendationService(),server)
  server.add_insecure_port(f"[::]:{PORT}")
  server.start()
  logger.info(f"started  V2 server on port {PORT}")
  server.wait_for_termination()
  logger.info(f"stopped server on port {PORT}")






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

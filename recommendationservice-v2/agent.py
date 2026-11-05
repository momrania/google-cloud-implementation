import grpc
import demo_pb2
import demo_pb2_grpc
import logging

from tools import get_products

logger = logging.getLogger(__name__)

def recommend(user_id,excluded_ids):
    #this is the entry point for the ai agent
    logger.info(f"USER_ID:{user_id}")
    logger.info(f"EXCLUDE_IDS:{excluded_ids}")
    products = get_products()

    excluded = set(excluded_ids)
    recommended = [ product.id for product in products if product.id not in excluded ]

    logger.info(f"recommendedation received")
    return recommended[:5]
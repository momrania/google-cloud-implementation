import os
import grpc
import logging

import demo_pb2_grpc
import demo_pb2

logger = logging.getLogger(__name__)

def get_products():

    address = os.getenv("PRODUCT_CATALOG_SERVICE_ADDR", "localhost:3550")

    logger.info(f"Setting up connection")
    with grpc.insecure_channel(address) as channel:
        stub = demo_pb2_grpc.ProductCatalogServiceStub(channel)
        response = stub.ListProducts(demo_pb2.Empty(),timeout=10)
        logger.info(f"Retrieved products")
        return list(response.products)
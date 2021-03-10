from concurrent import futures
import random

import grpc

import recommendpb.recommend_pb2_grpc as recommend_pb2_grpc
from recommendpb.recommend_pb2 import RecommendResponse

from .database import books_by_genre


class RecommendationService(recommend_pb2_grpc.RecommendationServicer):
    def Recommend(self, request, context):
        if request.genre not in books_by_genre:
            context.abort(grpc.StatusCode.NOT_FOUND, "Genre not found")

        books = books_by_genre[request.genre]
        num_results = min(request.max_results, len(books))
        books_to_recommend = random.sample(books, num_results)

        return RecommendResponse(recommendations=books_to_recommend)


def serve():
    print()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommend_pb2_grpc.add_RecommendationServicer_to_server(
        RecommendationService(), server)

    server.add_insecure_port("0.0.0.0:50051")
    print("Request received")
    server.start()
    server.wait_for_termination()


def run_server():
    print("Starting Server ....")
    serve()

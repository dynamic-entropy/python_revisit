import grpc
import os
import recommendpb.recommend_pb2_grpc as recommend_pb2_grpc
from recommendpb.recommend_pb2 import BookGenre, BookRecommendation, RecommendRequest


def rclient():

    # get hostname from environment
    recommendation_host = os.getenv("RECOMMENDATION_HOST", "localhost")

    # channel to a server
    channel = grpc.insecure_channel(f"{recommendation_host}:50051")

    client = recommend_pb2_grpc.RecommendationStub(channel)

    request = RecommendRequest(
        user_id="1", genre=BookGenre.SCIENCE_FICTION, max_results=3
    )

    response = client.Recommend(request)

    return response.recommendations

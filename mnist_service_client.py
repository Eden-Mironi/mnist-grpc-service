import grpc
from mnist_service_pb2 import DataRequest
from mnist_service_pb2_grpc import MnistServiceStub

def run():
    # Create a gRPC channel to connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Get the MNIST service
        stub = MnistServiceStub(channel)
        request = DataRequest()
        response_iterator = stub.GetTrainingSamples(request)

        # Process and handle the streamed MNIST samples
        for response in response_iterator:
            print(f"Received sample - Label: {response.label}")

if __name__ == '__main__':
    run()

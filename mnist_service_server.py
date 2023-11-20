import grpc
from concurrent import futures
import tensorflow as tf
from mnist_service_pb2 import Sample
from mnist_service_pb2_grpc import MnistServiceServicer, add_MnistServiceServicer_to_server

class MnistServiceImpl(MnistServiceServicer):
    def GetTrainingSamples(self, request, context):
        # Load MNIST dataset
        (train_images, train_labels), _ = tf.keras.datasets.mnist.load_data()

        # Normalize image data to range [0, 1]
        train_images = train_images / 255.0

        # Flatten images and convert labels to int64
        train_images = train_images.reshape((-1, 28 * 28))
        train_labels = train_labels.astype('int64')

        # Iterate through the dataset and stream samples
        for image, label in zip(train_images, train_labels):
            # Convert image data to bytes
            image_data = image.tobytes()

            # Yield Sample
            yield Sample(image=image_data, label=label)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MnistServiceServicer_to_server(MnistServiceImpl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

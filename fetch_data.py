from sklearn.datasets import fetch_olivetti_faces
from sklearn.datasets import fetch_lfw_people

if __name__ == "__main__":
    fetch_olivetti_faces()

    print("Loading Labeled Faces Data (~200MB)")
    fetch_lfw_people(min_faces_per_person=70, resize=0.4)
    print("=> Success!")

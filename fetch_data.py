import os
import urllib
import zipfile


def check_sentiment140(datasets_folder):
    print("Checking availability of the sentiment 140 dataset")
    archive_path = os.path.join(datasets_folder, SENTIMENT140_ARCHIVE_NAME)
    sentiment140_path = os.path.join(datasets_folder, 'sentiment140')
    train_path = os.path.join(sentiment140_path,
                              'training.1600000.processed.noemoticon.csv')
    test_path = os.path.join(sentiment140_path,
                             'testdata.manual.2009.06.14.csv')

    if not os.path.exists(archive_path):
        print("Downloading dataset from %s (77MB)" % SENTIMENT140_URL)
        opener = urllib.urlopen(SENTIMENT140_URL)
        open(archive_path, 'wb').write(opener.read())
    else:
        print("Found archive: " + archive_path)

    if not os.path.exists(sentiment140_path):
        print("Extracting %s to %s" % (archive_path, sentiment140_path))
        zf = zipfile.ZipFile(archive_path)
        zf.extractall(sentiment140_path)
    print("Checking that the sentiment 140 CSV files exist...")
    assert os.path.exists(train_path)
    assert os.path.exists(test_path)
    print("=> Success!")


if __name__ == "__main__":
    from sklearn.datasets import fetch_olivetti_faces
    fetch_olivetti_faces()
    print "Loading Labeled Faces Data (~200MB)"
    from sklearn.datasets import fetch_lfw_people
    fetch_lfw_people(min_faces_per_person=70, resize=0.4)

    print("=> Success!")

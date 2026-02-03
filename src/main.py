from dotenv import load_dotenv
load_dotenv()


from src.logs.samples import SAMPLE_LOG
from src.analysis.classifier import LogClassifier


def main():
    classifier = LogClassifier()
    result = classifier.classify(SAMPLE_LOG)

    print("\n=== Log Analysis Result ===")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()

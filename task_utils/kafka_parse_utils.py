import globals
import subprocess


def send_to_topic(topic, value):
    print("####################################")
    print(topic)
    subprocess.call(["python3", "task_utils/kafka_send.py", str(topic), str(value)])


def send_to_kafka_topics(group, pk):
    print("in send ################")
    print(group)
    print(pk)
    if group == "image" or group == "document":
        print("in image")
        print(globals.image_captioning_containers)
        if globals.image_captioning_containers is not None:
            print("in caption")
            for container in globals.image_captioning_containers:
                print(container)
                send_to_topic(topic=container, value=pk)

        if globals.ocr_containers is not None:
            for container in globals.ocr_containers:
                print(container)
                send_to_topic(topic=container, value=pk)
        if globals.object_detection_containers is not None:
            for container in globals.object_detection_containers:
                print(container)
                send_to_topic(topic=container, value=pk)
        if globals.scene_recognition_containers is not None:
            for container in globals.scene_recognition_containers:
                print(container)
                send_to_topic(topic=container, value=pk)
        if globals.image_recognition_containers is not None:
            for container in globals.image_recognition_containers:
                print(container)
                send_to_topic(topic=container, value=pk)
        if globals.image_search_containers is not None:
            for container in globals.image_search_containers:
                print(container)
                send_to_topic(topic=container, value=pk)

    elif group == "audio" or group == "video":
        if globals.sound_classification_containers is not None:
            for container in globals.sound_classification_containers:
                print(container)
                send_to_topic(topic=container, value=pk)
        if globals.audio_fingerprinting_containers is not None:
            for container in globals.audio_fingerprinting_containers:
                print(container)
                send_to_topic(topic=container, value=pk)
        if globals.speech_to_text_containers is not None:
            for container in globals.speech_to_text_containers:
                print(container)
                send_to_topic(topic=container, value=pk)

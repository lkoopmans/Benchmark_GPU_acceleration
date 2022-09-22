from lib import FishDetection
import time
import numpy as np

t0 = time.time()
fish_detection = FishDetection('videos/GX010150.MP4')

fish_detection.path_to_weights = 'yolo_weights/Jack_detect2.pt'
fish_detection.image_size_detection = '1280'
fish_detection.confidence = '0.8'
fish_detection.save_images = True
fish_detection.time_interval_between_frames = 2  # in sec
fish_detection.number_of_label_classes = 1
fish_detection.trimmed_clips_output_path = 'results/Jack_clips/'

fish_detection.extract_frames_from_video()
fish_detection.run_detector()

tf = time.time() - t0

with open('results/Benchmark_object_detection_GPU.txt', 'w') as f:
    f.write('1064 images have been extracted and analyzed: ' + str(np.round(tf, 1))+'s')
    f.write('\n')


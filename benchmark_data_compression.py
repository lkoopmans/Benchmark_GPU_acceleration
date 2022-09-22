import numpy as np
import time
import os
import subprocess

ts = time.time()

subprocess.run('ffmpeg -i videos/GX010150.MP4 -vcodec libx264 -crf 20 -preset ultrafast videos/264_ultra.MP4', shell=True)
t1 = time.time() - ts

subprocess.run('ffmpeg -i videos/GX010150.MP4 -vcodec libx264 -crf 20 -preset veryfast videos/264_very.MP4', shell=True)
t2 = time.time() - ts

subprocess.run('ffmpeg -i videos/GX010150.MP4 -vcodec libx264 -crf 20 -preset medium videos/264_medium.MP4', shell=True)
t3 = time.time() - ts

subprocess.run('ffmpeg -i videos/GX010150.MP4 -vcodec libx264 -crf 20 -preset slower videos/264_slower.MP4', shell=True)
t4 = time.time() - ts

subprocess.run('ffmpeg -i videos/GX010150.MP4 -c:v libx265 -crf 20 -preset ultrafast -c:a aac -b:a 128k '
               'videos/265_ultrafast.MP4', shell=True)
t5 = time.time() - ts

subprocess.run('ffmpeg -i videos/GX010150.MP4 -c:v libx265 -crf 20 -preset medium -c:a aac -b:a 128k '
               'videos/265_medium.MP4 ', shell=True)
t6 = time.time() - ts

with open('results/Benchmark_data_compression_GPU.txt', 'w') as f:
    f.write('h.264 preset ultrafast: ' + str(np.round(t1, 3))+'s')
    f.write('\n')
    f.write('h.264 preset veryfast: ' + str(np.round(t2-t1, 3))+'s')
    f.write('\n')
    f.write('h.264 preset medium: ' + str(np.round(t3-t2, ))+'s')
    f.write('\n')
    f.write('h.264 preset slower: ' + str(np.round(t4-t3, ))+'s')
    f.write('\n')
    f.write('h.265 preset ultrafast: ' + str(np.round(t5-t4, 3))+'s')
    f.write('\n')
    f.write('h.265 preset medium: ' + str(np.round(t6-t5, 3))+'s')
    f.write('\n')


os.remove('videos/output1.MP4')
os.remove('videos/output2.MP4')
os.remove('videos/output3.MP4')
os.remove('videos/output4.MP4')
os.remove('videos/output5.MP4')
os.remove('videos/output6.MP4')




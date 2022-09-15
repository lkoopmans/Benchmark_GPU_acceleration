from lib import ImageProcessingFunctions as ip
import numpy as np
import time
import os
import subprocess

ts = time.time()

path_to_videos = 'videos'

vid_names = ['GX010150.MP4']
output_base_name = os.path.splitext(vid_names[0])[0]

ip.cut_video(path_to_videos + '/' + vid_names[0], path_to_videos + '/' + output_base_name + '_cut1.MP4', 2, 520)
t1 = time.time()-ts

ip.cut_video(path_to_videos + '/' + vid_names[0], path_to_videos + '/' + output_base_name + '_cut2.MP4', 2, 520)
t2 = time.time()-ts

ip.cut_video(path_to_videos + '/' + vid_names[0], path_to_videos + '/' + output_base_name + '_cut3.MP4', 2, 520)
t3 = time.time()-ts

filenames = np.sort(os.listdir(path_to_videos))

with open('merge_list.txt', 'w') as f:
    for line in filenames:
        if 'MP4' in line:
            f.write('file \'' + path_to_videos + '/' + line + '\'')
            f.write('\n')

subprocess.run('ffmpeg -loglevel error -f concat -safe 0 -i merge_list.txt -c:v libx264 -c:a aac -preset'
               ' ultrafast  result.MP4', shell=True)

t4 = time.time()-ts

with open('results/Benchmark_cut_and_merge_GPU.txt', 'w') as f:
    f.write('First cut: ' + str(np.round(t1, 3))+'s')
    f.write('\n')
    f.write('Second cut: ' + str(np.round(t2, 3))+'s')
    f.write('\n')
    f.write('Third cut: ' + str(np.round(t3, ))+'s')
    f.write('\n')
    f.write('Merged: ' + str(np.round(t4, 3))+'s')
    f.write('\n')

os.remove('merge_list.txt')
os.remove('result.MP4')
os.remove(path_to_videos + '/' + output_base_name + '_cut1.MP4')
os.remove(path_to_videos + '/' + output_base_name + '_cut2.MP4')
os.remove(path_to_videos + '/' + output_base_name + '_cut3.MP4')
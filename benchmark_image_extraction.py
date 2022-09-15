import numpy as np
import time
import subprocess

ts = time.time()
subprocess.run('ffmpeg -i videos/GX010150.MP4 -vf fps=1/2 images/out%d.jpg', shell=True)
t1 = time.time() - ts

with open('results/Benchmark_image_extraction_GPU.txt', 'w') as f:
    f.write('Extracting 1062 images in: ' + str(np.round(t1, 3))+'s')
    f.write('\n')

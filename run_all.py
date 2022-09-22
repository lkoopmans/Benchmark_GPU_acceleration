import subprocess
import os
import torch

# Run requirements
subprocess.run('pip install -r requirements.txt', shell=True)

if not os.path.exists('videos'):
    os.mkdir('videos')

if not os.path.exists('images'):
    os.mkdir('images')

print('Cuda available:', torch.cuda.is_available())
if torch.cuda.is_available():
    print('Cuda device:', torch.cuda.get_device_name(0))


'''# Run benchmark tests
subprocess.run('python benchmark_cut_and_merge_files.py', shell=True)
subprocess.run('python benchmark_data_compression.py', shell=True)
subprocess.run('python benchmark_image_extraction.py', shell=True)
subprocess.run('python benchmark_object_detection.py', shell=True)'''

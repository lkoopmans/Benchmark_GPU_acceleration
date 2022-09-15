import subprocess

subprocess.run('python benchmark_cut_and_merge_files.py', shell=True)
subprocess.run('python benchmark_data_compression.py', shell=True)
subprocess.run('python benchmark_image_extraction.py', shell=True)
subprocess.run('python benchmark_object_detection.py', shell=True)
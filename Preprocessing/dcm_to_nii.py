import os

root = 'D:/imgdatatest/part1/'
pat_list = sorted(os.listdir(root))

for pat_dir in pat_list:
	pat_path = os.path.join(root,pat_dir)
	series_list = os.listdir(pat_path)
	for series in series_list:
		series_path = os.path.join(pat_path,series)
		try:
			os.system(f'D:\soft\dcm2niix\dcm2niix_win\dcm2niix.exe -f "%s_%d" -x i -y n -p n -z n -b n -o "{pat_path}" "{series_path}"')
			print(series_path + 'successed!')
		except:
			print('FAILED: '+series_path)
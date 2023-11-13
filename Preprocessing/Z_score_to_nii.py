import nibabel as nib
import numpy as np
import glob

#test_vol_names = glob.glob('E:/question/part2/*/*.nii.gz')
test_vol_names = glob.glob('C:/Users/Thinkbook15/Desktop/20180619001188zhaoshuyano/*.nii.gz')

#print(test_vol_names)


for name in test_vol_names:
    #print(name)
    #加载图片
    X = nib.load(str(name))

    #把仿射矩阵和头文件都存下来
    affine = X.affine.copy()
    hdr = X.header.copy()
    
    #取数据
    X_data = X.get_fdata()  
    
    #Z-score标准化
    Y_data = (X_data - np.mean(X_data)) / np.std(X_data)
    
    #形成新的nii文件
    new_nii = nib.Nifti1Image(X_data, affine, hdr)
    
    #改名
    read_path_final = name
    save_path_final = read_path_final.replace('.nii.gz', '_Zscore.nii.gz')
    
    #保存nii文件，后面的参数是保存的文件名
    nib.save(new_nii, save_path_final)


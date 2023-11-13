import os
import numpy as np
import SimpleITK as sitk
import glob

dir_path = sorted(glob.glob('/data_raid5_21T/xiong/imgdatatest/part2/*/*.nii'))

import SimpleITK as sitk
def BiasFiledCorrect(image):
    # mask_image = sitk.Cast(mask, sitk.sitkUInt8)
    mask_image = sitk.OtsuThreshold(image, 0, 1, 200)
    input_image = sitk.Cast(image, sitk.sitkFloat32)
    corrector = sitk.N4BiasFieldCorrectionImageFilter()
    output_image = corrector.Execute(input_image,mask_image)
    output_image = sitk.Cast(output_image, sitk.sitkInt16)
    return output_image

def N4biasField(dir_path):
    index = 1
    for name in dir_path:
        read_path_final = name
        save_path_final = read_path_final.replace('.nii', '_N4.nii')
        temp_name = name.split('.')
        print(save_path_final)
        inputImage = sitk.ReadImage(read_path_final)
        img1 = BiasFiledCorrect(inputImage)
        sitk.WriteImage(img1,save_path_final)

        # outputImage_to_N4 = sitk.Cast(inputImage, sitk.sitkFloat32)
        # corrector = sitk.N4BiasFieldCorrectionImageFilter()
        # output = corrector.Execute(outputImage_to_N4, outputImage_to_N4 != 0)
        # output = sitk.Cast(output, sitk.sitkInt16)
        # sitk.WriteImage(output, save_path_final)
        index = index+1

    
if __name__ == '__main__':
    N4biasField(dir_path)



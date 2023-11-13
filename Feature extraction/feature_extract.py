import os
from radiomics import featureextractor
import pandas as pd
import SimpleITK as sitk
params = 'E:/exampleMR_1mm.yaml'
extractor = featureextractor.RadiomicsFeatureExtractor(params)

#   淋巴结特征
Q=1
def saved_preprocessed(savedImg, origin, direction, xyz_thickness, saved_name):
    newImg = sitk.GetImageFromArray(savedImg, isVector=False)
    newImg.SetOrigin(origin)
    newImg.SetDirection(direction)
    newImg.SetSpacing((xyz_thickness[0], xyz_thickness[1], xyz_thickness[2]))
    sitk.WriteImage(newImg, saved_name, True)
if __name__ == '__main__':
    PathRoot = 'E:/6T1+C_mask+nii/MRIimgdata/part2/'
    save_path = 'E:/feature_output'
    table = pd.DataFrame()
    for i in os.listdir(PathRoot):
        for j in os.listdir(os.path.join(PathRoot, i)):
            if 'T1+C_N4_Zscore' in j:
                main_path = os.path.join(PathRoot, i, j)
                print(main_path)
                ori_img0 = sitk.ReadImage(main_path)
                ori_img = sitk.GetArrayFromImage(ori_img0)
            if 'T1+C_mask' in j:
                mask_path = os.path.join(PathRoot, i, j)
                mask0 = sitk.ReadImage(mask_path)
                mask = sitk.GetArrayFromImage(mask0)

        if ori_img.shape == mask.shape :#or ori_img0.GetSpacing() != mask0.GetSpacing() or ori_img0.GetDirection() != mask0.GetDirection() or ori_img0.GetOrigin() != mask0.GetOrigin():
            # print(j.split('_')[0], main_path.split('/')[-3])
        # saved_preprocessed(mask, ori_img0.GetOrigin(), ori_img0.GetDirection(), ori_img0.GetSpacing(), label_path)
            try:
                featureVector = extractor.execute(main_path, mask_path)
                #print(featureVector)
                aFeature = pd.Series(featureVector)
                aFeature = aFeature.to_frame()
                aFeature.loc[-1] = mask_path.split('/')[-1].split('\T1+C')[0]  ##加ID
                print(mask_path.split('/')[-1].split('\T1+C')[0])
                #print(type(aFeature))
                table = pd.concat([table, aFeature.T], ignore_index=True)
                #table = table.append(aFeature.T)
                print('FINISH',Q)
                Q+=1
            except:
                print(mask_path)
    drop_dp = table.filter(regex=('diagnostics.*'))  #####
    table = table.drop(drop_dp.columns, axis=1)
    pd.DataFrame(table).to_csv(save_path + '/第一批part2_feature.csv')

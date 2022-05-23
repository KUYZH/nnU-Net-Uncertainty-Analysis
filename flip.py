import SimpleITK as sitk
import numpy as np
itk_img = sitk.ReadImage('BraTS20_Validation_003.nii.gz')
img = sitk.GetArrayFromImage(itk_img)
print("img shape:",img.shape)
print(img[75,130,100])
temp =0
for k in range(155):
  for i in range(240):
    for j in range(120):
      temp = img[k,i,j]
      img[k,i,j] = img[k,i,(239-j)]
      img[k,i,(239-j)] = temp
print(np.unique(img))
print(img[75,130,100])
print(img[75,130,139])

img1 = sitk.GetImageFromArray(img)
sitk.WriteImage(img1,'BraTS20_Validation_003_final.nii.gz')
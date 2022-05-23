import SimpleITK as sitk
import numpy as np
itk_img = sitk.ReadImage('BraTS20_Validation_002.nii.gz')
img = sitk.GetArrayFromImage(itk_img)
print("img shape:",img.shape)
print(img[75,130,100])
temp =0
for k in range(155):
  for j in range(240):
    for i in range(120):
      temp = img[k,i,j]
      img[k,i,j] = img[k,(239-i),j]
      img[k,(239-i),j] = temp
print(np.unique(img))
print(img[75,130,100])
print(img[75,109,100])

img1 = sitk.GetImageFromArray(img)
sitk.WriteImage(img1,'BraTS20_Validation_002_final.nii.gz')
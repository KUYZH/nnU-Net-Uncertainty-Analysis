import SimpleITK as sitk
from matplotlib import pyplot as plt

img1 = sitk.ReadImage('BraTS20_Validation_001.nii.gz')
img2 = sitk.ReadImage('BraTS20_Validation_002_final.nii.gz')
img3 = sitk.ReadImage('BraTS20_Validation_003_final.nii.gz')
#img4 = sitk.ReadImage('BraTS20_Validation_001.nii.gz')
#img5 = sitk.ReadImage('BraTS20_Validation_075_04.nii.gz')
#img = (itk_img1-itk_img2)+(itk_img1-itk_img3)+(itk_img1-itk_img4)+(itk_img1-itk_img5)+(itk_img2-itk_img3)+(itk_img2-itk_img4)+(itk_img2-itk_img5)+(itk_img3-itk_img4)+(itk_img3-itk_img5)+(itk_img4-itk_img5)
itk_img1 = sitk.GetArrayFromImage(img1)
itk_img2 = sitk.GetArrayFromImage(img2)
itk_img3 = sitk.GetArrayFromImage(img3)
#itk_img4 = sitk.GetArrayFromImage(img4)
#itk_img5 = sitk.GetArrayFromImage(img5)

mean = (itk_img1+itk_img2+itk_img3)/3

x1 = (itk_img1-mean)**2
x2 = (itk_img2-mean)**2
x3 = (itk_img3-mean)**2
#x4 = (itk_img4-mean)**2
#x5 = (itk_img5-mean)**2
var = (x1+x2+x3)/3

mean1 = sitk.GetImageFromArray(mean)
var1 = sitk.GetImageFromArray(var)
sitk.WriteImage(var1,'varcontrast.nii.gz')
sitk.WriteImage(mean1,'meancontrast.nii.gz')
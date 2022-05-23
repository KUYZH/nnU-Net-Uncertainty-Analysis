import SimpleITK as sitk
import numpy as np
itk_img = sitk.ReadImage('BraTS20_Validation_002_t1.nii.gz')
img = sitk.GetArrayFromImage(itk_img)
print("img shape:",img.shape)
print(img[75,130,0])
temp =0
imgs = img
for k in range(155):
  for j in range(240):
    for i in range(60): 
      imgs[k,120-i,j] = img[k,120-2*i,j]
      imgs[k,120+i,j] = img[k,120+2*i,j]
    imgs[k,0:63,j]= 0
    imgs[k,175:240,j]=0

for k in range(155):
  for i in range(240):
    for j in range(60): 
      imgs[k,i,120-j] = img[k,i,120-2*j]
      imgs[k,i,120+j] = img[k,i,120+2*j]
    imgs[k,i,0:63]= 0
    imgs[k,i,175:240]=0
    
for j in range(240):
  for i in range(240):     
    for k in range(38):
    

      imgs[77-k,i,j] = img[77-2*k,i,j]
      imgs[77+k,i,j] = img[77+2*k,i,j]
    imgs[0:43,i,j]= 0
    imgs[113:155,i,j]=0
    
      #img[k,i,j] = img[k,i,(239-j)]
      #if j <60:
        #img[k,i,60+j] = img[k,i,2*j]
        
      #else:
        #img[k,i,60+j] = img[k,i,2*j]
      
print(np.unique(img))
print(img[75,130,0])
print(img[75,130,60])

img1 = sitk.GetImageFromArray(imgs)
sitk.WriteImage(img1,'test.nii.gz')
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from . models import Contact,img_upload
from .forms import ImageFrom
def index(request):
    if request.method == 'POST':
        name= request.POST["name"]
        email=request.POST["email"]
        ship=request.POST["ship"]
        pro=request.POST["pro"]
        context = Contact(name=name,email=email,ship=ship,pro=pro)
        context.save()
    return render(request,'app/index.html')
    

# Create your views here.
def uploader(request):
    if request.method == 'POST':
        form = ImageFrom(request.POST,request.FILES)
        if form.is_valid():
           form.save()
    form=ImageFrom
    return render(request,"app/test.html",{"form":form})






# import tensorflow 
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.layers import GlobalMaxPooling2D
# from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
# import pickle


# import numpy as np
# from numpy.linalg import norm
# from sklearn.neighbors import NearestNeighbors
# import cv2

# model = ResNet50(weights = 'imagenet',include_top=False, input_shape= (224,224,3))
# model.trianable=False
# model = tensorflow.keras.Sequential([
#     model,
#     GlobalMaxPooling2D()
# ])


# img = image.load_img('samples/bag.jpg', target_size = (224,224))
# img_array = image.img_to_array(img)
# expanded_img_array = np.expand_dims(img_array, axis = 0)
# preprocessed_img = preprocess_input(expanded_img_array)
# result = model.predict(preprocessed_img).flatten()
# normal_result = result/norm(result)


# def generate_img (details_file, names_file,n):
#     features_list = pickle.load(open(details_file, 'rb'))
#     filenames = pickle.load(open(names_file ,'rb'))

#     neighbors = NearestNeighbors(n_neighbors = n , algorithm = 'brute', metric = 'euclidean')
#     neighbors.fit(features_list)

#     distances , indices = neighbors.kneighbors([normal_result])
    
#     for file in indices[0][1:len(indices[0])]:
#         temp_img = cv2.imread(filenames[file])
#         cv2.imshow('output',cv2.resize(temp_img,(100,100)))
#         cv2.waitKey(0)
                                     
# generate_img('feature_details.pkl','filenames.pkl',5)

# # flag = input("enter w for women, m  for men, else o ",)


# if flag=='w':
#     generate_img('feature_details_jeans.pkl','filenames_jeans.pkl',2)
#     generate_img('feature_details_sandals.pkl','filenames_sandals.pkl',2)
#     generate_img('feature_details_spec.pkl','filenames_spec.pkl',2)
# else:
#     if flag=='m':
#         generate_img('feature_details_mensjeans.pkl','filenames_mensjeans.pkl',2)
#         generate_img('feature_details_shoe.pkl','filenames_shoe.pkl',2)
#         generate_img('feature_details_spec.pkl','filenames_spec.pkl',2)

    
    
    
    
        
            

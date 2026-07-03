from utils import *
from preprocess import *
from train import *

input_data = [7.3,0.65,0.0,1.2,0.065,15.0,21.0,0.9946,3.39,0.47,10.0]

input_data_as_numpy_arrray = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_arrray.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 1):
    print('Good Quality Wine')
else:
    print('Bad Quality Wine')

Loss: 0.552
Accuracy: 0.768
F1[A]: 0.6170212765957447
F1[~]: 0.48520710059171596
F1[N]: 0.8876712328767123
F1[O]: 0.5519630484988453
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv1d_21 (Conv1D)           (None, 8996, 32)          192       
_________________________________________________________________
activation_21 (Activation)   (None, 8996, 32)          0         
_________________________________________________________________
max_pooling1d_19 (MaxPooling (None, 4498, 32)          0         
_________________________________________________________________
conv1d_22 (Conv1D)           (None, 4494, 32)          5152      
_________________________________________________________________
activation_22 (Activation)   (None, 4494, 32)          0         
_________________________________________________________________
max_pooling1d_20 (MaxPooling (None, 2247, 32)          0         
_________________________________________________________________
conv1d_23 (Conv1D)           (None, 2243, 32)          5152      
_________________________________________________________________
activation_23 (Activation)   (None, 2243, 32)          0         
_________________________________________________________________
max_pooling1d_21 (MaxPooling (None, 1121, 32)          0         
_________________________________________________________________
conv1d_24 (Conv1D)           (None, 1117, 32)          5152      
_________________________________________________________________
activation_24 (Activation)   (None, 1117, 32)          0         
_________________________________________________________________
max_pooling1d_22 (MaxPooling (None, 558, 32)           0         
_________________________________________________________________
conv1d_25 (Conv1D)           (None, 554, 32)           5152      
_________________________________________________________________
activation_25 (Activation)   (None, 554, 32)           0         
_________________________________________________________________
max_pooling1d_23 (MaxPooling (None, 277, 32)           0         
_________________________________________________________________
conv1d_26 (Conv1D)           (None, 273, 32)           5152      
_________________________________________________________________
activation_26 (Activation)   (None, 273, 32)           0         
_________________________________________________________________
max_pooling1d_24 (MaxPooling (None, 136, 32)           0         
_________________________________________________________________
dropout_7 (Dropout)          (None, 136, 32)           0         
_________________________________________________________________
conv1d_27 (Conv1D)           (None, 132, 32)           5152      
_________________________________________________________________
activation_27 (Activation)   (None, 132, 32)           0         
_________________________________________________________________
max_pooling1d_25 (MaxPooling (None, 66, 32)            0         
_________________________________________________________________
conv1d_28 (Conv1D)           (None, 62, 32)            5152      
_________________________________________________________________
activation_28 (Activation)   (None, 62, 32)            0         
_________________________________________________________________
max_pooling1d_26 (MaxPooling (None, 31, 32)            0         
_________________________________________________________________
dropout_8 (Dropout)          (None, 31, 32)            0         
_________________________________________________________________
conv1d_29 (Conv1D)           (None, 27, 32)            5152      
_________________________________________________________________
activation_29 (Activation)   (None, 27, 32)            0         
_________________________________________________________________
max_pooling1d_27 (MaxPooling (None, 13, 32)            0         
_________________________________________________________________
dropout_9 (Dropout)          (None, 13, 32)            0         
_________________________________________________________________
conv1d_30 (Conv1D)           (None, 9, 32)             5152      
_________________________________________________________________
activation_30 (Activation)   (None, 9, 32)             0         
_________________________________________________________________
flatten_3 (Flatten)          (None, 288)               0         
_________________________________________________________________
dense_3 (Dense)              (None, 4)                 1156      
=================================================================
Total params: 47,716
Trainable params: 47,716
Non-trainable params: 0
_________________________________________________________________

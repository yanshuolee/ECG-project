Loss: 0.492
Accuracy: 0.835
F1[A]: 0.747774480712166
F1[~]: 0.5882352941176471
F1[N]: 0.9000404694455686
F1[O]: 0.7426086956521739
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv1d_31 (Conv1D)           (None, 8996, 32)          192       
_________________________________________________________________
activation_31 (Activation)   (None, 8996, 32)          0         
_________________________________________________________________
batch_normalization_4 (Batch (None, 8996, 32)          128       
_________________________________________________________________
max_pooling1d_28 (MaxPooling (None, 4498, 32)          0         
_________________________________________________________________
conv1d_32 (Conv1D)           (None, 4494, 32)          5152      
_________________________________________________________________
activation_32 (Activation)   (None, 4494, 32)          0         
_________________________________________________________________
max_pooling1d_29 (MaxPooling (None, 2247, 32)          0         
_________________________________________________________________
conv1d_33 (Conv1D)           (None, 2243, 64)          10304     
_________________________________________________________________
activation_33 (Activation)   (None, 2243, 64)          0         
_________________________________________________________________
max_pooling1d_30 (MaxPooling (None, 1121, 64)          0         
_________________________________________________________________
conv1d_34 (Conv1D)           (None, 1117, 64)          20544     
_________________________________________________________________
activation_34 (Activation)   (None, 1117, 64)          0         
_________________________________________________________________
max_pooling1d_31 (MaxPooling (None, 558, 64)           0         
_________________________________________________________________
conv1d_35 (Conv1D)           (None, 554, 128)          41088     
_________________________________________________________________
activation_35 (Activation)   (None, 554, 128)          0         
_________________________________________________________________
max_pooling1d_32 (MaxPooling (None, 277, 128)          0         
_________________________________________________________________
conv1d_36 (Conv1D)           (None, 273, 128)          82048     
_________________________________________________________________
activation_36 (Activation)   (None, 273, 128)          0         
_________________________________________________________________
max_pooling1d_33 (MaxPooling (None, 136, 128)          0         
_________________________________________________________________
dropout_13 (Dropout)         (None, 136, 128)          0         
_________________________________________________________________
conv1d_37 (Conv1D)           (None, 132, 256)          164096    
_________________________________________________________________
activation_37 (Activation)   (None, 132, 256)          0         
_________________________________________________________________
max_pooling1d_34 (MaxPooling (None, 66, 256)           0         
_________________________________________________________________
conv1d_38 (Conv1D)           (None, 62, 256)           327936    
_________________________________________________________________
activation_38 (Activation)   (None, 62, 256)           0         
_________________________________________________________________
max_pooling1d_35 (MaxPooling (None, 31, 256)           0         
_________________________________________________________________
dropout_14 (Dropout)         (None, 31, 256)           0         
_________________________________________________________________
conv1d_39 (Conv1D)           (None, 27, 512)           655872    
_________________________________________________________________
activation_39 (Activation)   (None, 27, 512)           0         
_________________________________________________________________
max_pooling1d_36 (MaxPooling (None, 13, 512)           0         
_________________________________________________________________
dropout_15 (Dropout)         (None, 13, 512)           0         
_________________________________________________________________
conv1d_40 (Conv1D)           (None, 9, 512)            1311232   
_________________________________________________________________
activation_40 (Activation)   (None, 9, 512)            0         
_________________________________________________________________
average_pooling1d_4 (Average (None, 4, 512)            0         
_________________________________________________________________
flatten_4 (Flatten)          (None, 2048)              0         
_________________________________________________________________
dense_10 (Dense)             (None, 128)               262272    
_________________________________________________________________
dropout_16 (Dropout)         (None, 128)               0         
_________________________________________________________________
dense_11 (Dense)             (None, 32)                4128      
_________________________________________________________________
dense_12 (Dense)             (None, 4)                 132       
=================================================================
Total params: 2,885,124
Trainable params: 2,885,060
Non-trainable params: 64
_________________________________________________________________

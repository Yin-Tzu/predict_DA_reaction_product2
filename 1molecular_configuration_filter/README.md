### cutvideotoimage:

先使用cutvideotoimage把影片截成好幾張圖片(程式、輸入圖片、輸出圖片)

### 手動

把沒辦法表現出正確分子結構的圖片刪除，並且剩下的張數與其他結構的張數相同，避免訓練數量不平均的問題(手動)

### 1NN_resize_npy:

輸入編號與沒有resize的圖片，輸出resize過的圖片的npy檔案與label的npy檔案

### imglabeltotrainvalidtestdataset:

輸入各個image&label的npy檔案，腳在一起後，輸出X_train,X_valid,X_test,y_train_label,y_valid_label,y_test_label的npy檔案

### divided_to_ring_or_straight

使用CNN預測是否是環還是直鏈

![avatar](https://github.com/Yin-Tzu/predict_DA_reaction_product2/raw/main/1molecular_configuration_filter/CNN_molecular_configuration_filter.png =x100)




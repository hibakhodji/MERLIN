* To train, use: ./darknet detector train data/obj.data yolov4-custom.cfg ./backup/yolov4-custom_best.weights -map -dont_show
* To evaluate, use ./darknet detector map data/obj.data yolov4-custom.cfg ./backup/yolov4-custom_best.weights
* To predict, use: ./darknet detector test data/obj.data yolov4-custom.cfg ./backup/yolov4-custom_best.weights
* to predict on multiple images, use: ./darknet detector test data/obj.data yolov4-custom.cfg backup/yolov4-custom_best.weights -dont_show -ext_output < data/images.txt > multiple_predictions.txt
* PRIMATES Data can be retrieved from https://zenodo.org/records/6637475#.ZCV9ai0RppQ
* BALIBASE images can be found in darknet/data/obj/balibase/

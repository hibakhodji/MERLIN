Necessary codes and scripts for our MERLIN paper: https://link.springer.com/chapter/10.1007/978-3-031-08333-4_16
* To train, use: ./darknet detector train data/obj.data yolov4-custom.cfg yolov4.conv.137 -map -dont_show (for detailed instructions, https://github.com/AlexeyAB/darknet?tab=readme-ov-file#how-to-train-to-detect-your-custom-objects)
* To evaluate, use ./darknet detector map data/obj.data yolov4-custom.cfg merlin_weights/yolov4-custom_best.weights
* To predict, use: ./darknet detector test data/obj.data yolov4-custom.cfg merlin_weights/yolov4-custom_best.weights
* to predict on multiple images, use: ./darknet detector test data/obj.data yolov4-custom.cfg merlin_weights/yolov4-custom_best.weights -dont_show -ext_output < data/images.txt > multiple_predictions.txt
* PRIMATES images can be found in data/train.txt, data/valid.txt, and data/test.txt and retrieved from https://zenodo.org/records/6637475#.ZCV9ai0RppQ
* BALIBASE images can be found in darknet/data/obj/balibase/

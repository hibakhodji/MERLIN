Necessary codes and scripts for our MERLIN paper: https://link.springer.com/chapter/10.1007/978-3-031-08333-4_16
* PRIMATES images can be found in data/train.txt, data/valid.txt, and data/test.txt and retrieved from https://zenodo.org/records/6637475#.ZCV9ai0RppQ
* Download darknet from: https://github.com/AlexeyAB/darknet.git
* To train, use: ./darknet detector train obj.data config/yolov4-custom.cfg yolov4.conv.137 -map -dont_show (for detailed instructions, https://github.com/AlexeyAB/darknet?tab=readme-ov-file#how-to-train-to-detect-your-custom-objects)
* To evaluate, use ./darknet detector map obj.data config/yolov4-custom.cfg weights/yolov4-custom_best.weights
* To predict, use: ./darknet detector test obj.data config/yolov4-custom.cfg weights/yolov4-custom_best.weights
* to predict on multiple images, use: ./darknet detector test obj.data config/yolov4-custom.cfg weights/yolov4-custom_best.weights -dont_show -ext_output < data/images.txt > multiple_predictions.txt

For more trained weights, predictions results, and BALIBASE data: https://gitlab.unistra.fr/khodji/merlin

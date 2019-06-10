#!/usr/bin/env bash

## BEWARE OF HARD_CODED TENSOR SIZES FOR LABELS.
## IF YOU CHANGE A MODEL OR ADD A LABEL WE NEED TO UPDATE THAT MODELS TENSOR SHAPE

CinemaNetPath=`pwd`
echo $CinemaNetPath

cd ../../tensorflow/

# Summarize a model to ensure our paths are ok.
#bazel-bin/tensorflow/tools/graph_transforms/summarize_graph --print_structure=true --in_graph=$CinemaNetPath/Models/CinemaNetShotAngles.pb 

TransformFlags="remove_nodes(op=Identity, op=CheckNumerics) fold_constants(ignore_errors=true) fold_batch_norms fold_old_batch_norms remove_device sort_by_execution_order"
TransformFlagsQuantized="$TransformFlags quantize_weights"

# TransformFlags="remove_nodes(op=Identity, op=CheckNumerics) fold_constants(ignore_errors=true) fold_batch_norms fold_old_batch_norms remove_device"
# TransformFlagsQuantized="remove_nodes(op=Identity, op=CheckNumerics) fold_constants(ignore_errors=true) fold_batch_norms fold_old_batch_norms remove_device quantize_weights"

echo "Exporting Feature Extractor"
#Transform feature extractor & quantized feature extractor
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/CinemaNetShotAngles.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers/CinemaNetFeatureExtractor.pb --inputs='input' --outputs='input_1/BottleneckInputPlaceholder' --transforms="strip_unused_nodes(type=float, shape=\"1,224,224,3\") $TransformFlags"
echo "Exporting Feature ExtractorQuantized"
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/CinemaNetShotAngles.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers\ Quantized/CinemaNetFeatureExtractor.pb --inputs='input' --outputs='input_1/BottleneckInputPlaceholder' --transforms="strip_unused_nodes(type=float, shape=\"1,224,224,3\") $TransformFlagsQuantized"

echo ""

#Transform classifiers & quantized classifiers
echo "Exporting CinemaNetShotAngles Classifier"
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/CinemaNetShotAngles.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers/CinemaNetShotAnglesClassifier.pb --inputs='input_1/BottleneckInputPlaceholder' --outputs='final_result' --transforms="strip_unused_nodes(type=float, shape=\"4,1001\") $TransformFlags"
echo "Exporting CinemaNetShotAngles Classifier Quantized"
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/CinemaNetShotAngles.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers\ Quantized/CinemaNetShotAnglesClassifier.pb --inputs='input_1/BottleneckInputPlaceholder' --outputs='final_result' --transforms="strip_unused_nodes(type=float, shape=\"4,1001\") $TransformFlagsQuantized"

echo ""

echo "Exporting CinemaNetShotFraming Classifier"
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/CinemaNetShotFraming.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers/CinemaNetShotFramingClassifier.pb --inputs='input_1/BottleneckInputPlaceholder' --outputs='final_result' --transforms="strip_unused_nodes(type=float, shape=\"5,1001\") $TransformFlags"
echo "Exporting CinemaNetShotFraming Classifier Quantized"
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/CinemaNetShotFraming.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers\ Quantized/CinemaNetShotFramingClassifier.pb --inputs='input_1/BottleneckInputPlaceholder' --outputs='final_result' --transforms="strip_unused_nodes(type=float, shape=\"5,1001\") $TransformFlagsQuantized"

echo ""

echo "Exporting CinemaNetShotSubject Classifier"
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/CinemaNetShotSubject.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers/CinemaNetShotSubjectClassifier.pb --inputs='input_1/BottleneckInputPlaceholder' --outputs='final_result' --transforms="strip_unused_nodes(type=float, shape=\"6,1001\") $TransformFlags"
echo "Exporting CinemaNetShotSubject Classifier Quantized"
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/CinemaNetShotSubject.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers\ Quantized/CinemaNetShotSubjectClassifier.pb --inputs='input_1/BottleneckInputPlaceholder' --outputs='final_result' --transforms="strip_unused_nodes(type=float, shape=\"6,1001\") $TransformFlagsQuantized"

echo ""

echo "Exporting CinemaNetShotType Classifier"
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/CinemaNetShotType.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers/CinemaNetShotTypeClassifier.pb --inputs='input_1/BottleneckInputPlaceholder' --outputs='final_result' --transforms="strip_unused_nodes(type=float, shape=\"4,1001\") $TransformFlags"
echo "Exporting CinemaNetShotType Classifier Quantized"
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/CinemaNetShotType.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers\ Quantized/CinemaNetShotTypeClassifier.pb --inputs='input_1/BottleneckInputPlaceholder' --outputs='final_result' --transforms="strip_unused_nodes(type=float, shape=\"4,1001\") $TransformFlagsQuantized"

echo ""

echo "Exporting PlacesNet Classifier"
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/PlacesNet.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers/PlacesNetClassifier.pb --inputs='input_1/BottleneckInputPlaceholder' --outputs='final_result' --transforms="strip_unused_nodes(type=float, shape=\"365,1001\") $TransformFlags"
echo "Exporting PlacesNet Classifier Quantized"
bazel-bin/tensorflow/tools/graph_transforms/transform_graph --in_graph=$CinemaNetPath/Models/PlacesNet.pb  --out_graph=$CinemaNetPath/Feature\ Extractor\ and\ Classifiers\ Quantized/PlacesNetClassifier.pb --inputs='input_1/BottleneckInputPlaceholder' --outputs='final_result' --transforms="strip_unused_nodes(type=float, shape=\"365,1001\") $TransformFlagsQuantized"

echo ""

cd $CinemaNetPath
echo "Convert to CoreML"
python $CinemaNetPath/coreml_converter.py
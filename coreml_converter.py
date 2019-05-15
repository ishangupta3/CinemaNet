import tfcoreml as tf_converter

# BEWARE OR LABEL COUNTS AND TENSOR SHAPES

# Feature Extractor
tf_converter.convert(tf_model_path = 'Feature Extractor and Classifiers/CinemaNetFeatureExtractor.pb',
                    mlmodel_path = 'CoreML/CinemaNetFeatureExtractor.mlmodel',
                    output_feature_names = ['input_1/BottleneckInputPlaceholder:0'],
                    input_name_shape_dict = {'input:0' : [1,224,224,3]},
                    image_input_names ='input:0',
                    red_bias=-1,
                    green_bias=-1,
                    blue_bias=-1,
                    image_scale=2.0/255.0,
                    is_bgr = True,
                    )


# Shot Angle
tf_converter.convert(tf_model_path = 'Feature Extractor and Classifiers/CinemaNetShotAnglesClassifier.pb',
                     mlmodel_path = 'CoreML/CinemaNetShotAnglesClassifier.mlmodel',
                     output_feature_names = ['final_result:0'],
                     input_name_shape_dict = {'input_1/BottleneckInputPlaceholder:0' : [4,1001]},
                     class_labels = 'Models/CinemaNetShotAnglesLabels.txt',
                     predicted_feature_name = 'classLabel',
                     # predicted_probabilities_output = 'final_result__0',
                     )


# Shot Framing
tf_converter.convert(tf_model_path = 'Feature Extractor and Classifiers/CinemaNetShotFramingClassifier.pb',
                     mlmodel_path = 'CoreML/CinemaNetShotFramingClassifier.mlmodel',
                     output_feature_names = ['final_result:0'],
                     input_name_shape_dict = {'input_1/BottleneckInputPlaceholder:0' : [5,1001]},
                     class_labels = 'Models/CinemaNetShotFramingLabels.txt',
                     predicted_feature_name = 'classLabel',
                     # predicted_probabilities_output = 'final_result__0',
        )


# Shot Subject
tf_converter.convert(tf_model_path = 'Feature Extractor and Classifiers/CinemaNetShotSubjectClassifier.pb',
                     mlmodel_path = 'CoreML/CinemaNetShotSubjectClassifier.mlmodel',
                     output_feature_names = ['final_result:0'],
                     input_name_shape_dict = {'input_1/BottleneckInputPlaceholder:0' : [6,1001]},
                     class_labels = 'Models/CinemaNetShotSubjectLabels.txt',
                     predicted_feature_name = 'classLabel',
                     # predicted_probabilities_output = 'final_result__0',
        )

# Shot Type
tf_converter.convert(tf_model_path = 'Feature Extractor and Classifiers/CinemaNetShotTypeClassifier.pb',
                     mlmodel_path = 'CoreML/CinemaNetShotTypeClassifier.mlmodel',
                     output_feature_names = ['final_result:0'],
                     input_name_shape_dict = {'input_1/BottleneckInputPlaceholder:0' : [4,1001]},
                     class_labels = 'Models/CinemaNetShotTypeLabels.txt',
                     predicted_feature_name = 'classLabel',
                     # predicted_probabilities_output = 'final_result__0',
        )

# Places Type
tf_converter.convert(tf_model_path = 'Feature Extractor and Classifiers/PlacesNetClassifier.pb',
                     mlmodel_path = 'CoreML/PlacesNetClassifier.mlmodel',
                     output_feature_names = ['final_result:0'],
                     input_name_shape_dict = {'input_1/BottleneckInputPlaceholder:0' : [365,1001]},
                     class_labels = 'Models/PlacesNetLabels.txt',
                     predicted_feature_name = 'classLabel',
                     # predicted_probabilities_output = 'final_result__0',
        )

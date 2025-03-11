from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.ml import PipelineModel
from pyspark.ml.classification import NaiveBayesModel

from pyspark.sql.functions import regexp_replace, col, udf, split, lower


# Initialize Spark session
spark = SparkSession.builder \
    .appName("NewsCategoryPrediction") \
    .getOrCreate()

prediction_to_category = {
    
    0: "Entertainment",
    1: "Business",
    2: "Technology",
    3: "Health"
}

pipeline_path_model = 'models/pipeline_model2'
nb_path_model = 'models/naive_bayesian_final'

loaded_pipeline_model = PipelineModel.load(pipeline_path_model)
nb_loaded_model = NaiveBayesModel.load(nb_path_model)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the text data from the POST request
        data = request.get_json()
        titles = data['titles']  # The column name is now 'TITLE'

        # Convert the input text in a format of list into a DataFrame (for Spark processing)
        input_data = spark.createDataFrame([Row(TITLE=title) for title in titles])

        def preprocess_title_column(df, input_col="TITLE", output_col="title_only_str"):
            return df.withColumn(output_col, lower(regexp_replace(col(input_col), r'[^\w\s]|[0-9]+', '')))
        
        processed_data  = preprocess_title_column(input_data)
        # Apply the loaded model to new data
        loaded_transformed_df = loaded_pipeline_model.transform(processed_data)
        predictions = nb_loaded_model.transform(loaded_transformed_df)

        # create an output response
        result = []
        for row in predictions.select("TITLE", "prediction").collect():
            predicted_category_index = row['prediction']
            predicted_category = prediction_to_category.get(predicted_category_index, "Unknown")
            result.append({
                'TITLE': row['TITLE'],
                'category': predicted_category
            })

        # Return the predictions as a JSON response
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8777)
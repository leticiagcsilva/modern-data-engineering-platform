import sys
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount_spark.py <input_gcs_path> <output_gcs_path>", file=sys.stderr)
        sys.exit(-1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    sc = SparkContext(appName="PySpark Word Count - Dataproc")

    words = sc.textFile(input_path).flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    sortedCounts = wordCounts.sortBy(lambda a: a[1], ascending=False)

    sortedCounts.saveAsTextFile(output_path)

    sc.stop()

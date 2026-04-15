# Hadoop Ecosystem: Word Count with PySpark on Google Cloud Dataproc

This subproject demonstrates a distributed word count pipeline using **PySpark** executed on **Google Cloud Dataproc**, with input and output files stored on **Google Cloud Storage (GCS)**.

---

## Project Overview

This job:
- Reads a text file (`.txt`) stored on a GCS bucket
- Splits the text into words
- Counts the frequency of each word
- Sorts words by frequency
- Saves the result back to GCS as a text file

It uses PySpark’s `textFile`, `flatMap`, `map`, `reduceByKey`, and `saveAsTextFile` transformations. This approach is scalable and can handle large datasets in a distributed environment.

---

## Project Structure

```
Ecossistema_Hadoop/
├── wordcount_spark.py       # Main PySpark job script
├── README.md                # This documentation file
```

---

## Technologies Used

- PySpark
- Google Cloud Platform (GCP)
- Google Cloud Dataproc
- Google Cloud Storage (GCS)
- Hadoop-compatible Input/Output with Spark

---

## How to Run This on GCP Dataproc

Make sure you have a Dataproc cluster running and a GCS bucket with your input file uploaded.

### Submit the job:

```bash
gcloud dataproc jobs submit pyspark wordcount_spark.py \
  --cluster=your-cluster-name \
  --region=your-region \
  -- gs://your-bucket/livro.txt gs://your-bucket/output_folder
```

- Replace `your-cluster-name` and `your-region` accordingly.
- Replace `your-bucket` with the name of your GCS bucket.
- The output will be saved as part-files inside `output_folder`.

---

## Example with Dummy Data

You can upload any `.txt` file to a GCS bucket and run the command:

```bash
gcloud dataproc jobs submit pyspark wordcount_spark.py \
  --cluster=cluster-spark \
  --region=southamerica-east1 \
  -- gs://meu-bucket/livro.txt gs://meu-bucket/resultado
```

---

## Output

Output files will be created under the specified GCS path in text format. Each line will follow the format:

```
(word, count)
```

---
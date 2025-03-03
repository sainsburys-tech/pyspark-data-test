import argparse

from pyspark.sql import SparkSession, DataFrame


def read_input_data(
    spark: SparkSession,
    customers_location: str,
    products_location: str,
    transactions_location: str,
) -> tuple[DataFrame, DataFrame, DataFrame]:

    customers_df = spark.read.csv(customers_location, header=True)
    products_df = spark.read.csv(products_location, header=True)
    transactions_df = spark.read.json(transactions_location, multiLine=True)

    return customers_df, products_df, transactions_df


def run_transformations(
    spark: SparkSession,
    customers_location: str,
    products_location: str,
    transactions_location: str,
    output_location: str
):

    customers_df, products_df, transactions_df = read_input_data(
        spark,
        customers_location,
        products_location,
        transactions_location
    )

def get_latest_transaction_date(spark: SparkSession):
    result = spark.sql("""SELECT MAX(date_of_purchase) AS date_of_purchase FROM raw_transactions""").collect()[0]
    max_date = result.date_of_purchase
    return max_date


def to_canonical_date_str(date_to_transform):
    return date_to_transform.strftime('%Y-%m-%d')


if __name__ == "__main__":
    spark_session = (
            SparkSession.builder
                        .master("local[2]")
                        .appName("DataTest")
                        .config("spark.executorEnv.PYTHONHASHSEED", "0")
                        .getOrCreate()
    )

    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--customers_location', required=False, default="./input_data/starter/customers.csv")
    parser.add_argument('--products_location', required=False, default="./input_data/starter/products.csv")
    parser.add_argument('--transactions_location', required=False, default="./input_data/starter/transactions/")
    parser.add_argument('--output_location', required=False, default="./output_data/outputs/")
    args = vars(parser.parse_args())

    run_transformations(
        spark_session,
        args['customers_location'],
        args['products_location'],
        args['transactions_location'],
        args['output_location']
    )

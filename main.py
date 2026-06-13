from extract import extract_gasprices
from transform import transform_gasprices
from load import load_gasprices


def main():
    data = extract_gasprices()
    df = transform_gasprices(data)
    load_gasprices(df)

    print("ETL process completed successfuly")

if __name__== "__main__":
    main()


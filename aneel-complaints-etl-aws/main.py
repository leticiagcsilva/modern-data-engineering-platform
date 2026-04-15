"""Entrypoint for running the ANEEL complaints ETL pipeline locally."""

from src.pipeline import run_pipeline


if __name__ == "__main__":
    run_pipeline()

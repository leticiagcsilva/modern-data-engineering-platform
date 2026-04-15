"""Backward-compatible entrypoint for the renamed seed generation script."""

from scripts.generate_climate_seed import main


if __name__ == "__main__":
    main()

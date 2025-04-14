# ML Data Verifier
This project was completed within a 24-hour timeframe as an experiment to assess the impact of strict deadlines on productivity. The objective was to evaluate whether a constrained timeline would enhance focus and efficiency. The results demonstrated that the time limitation significantly boosted productivity and concentration, leading to the successful completion of the project within the allotted period.

## Overview the Project

ML Data Verifier is a tool designed to validate and preprocess datasets for machine learning projects. It ensures data quality, consistency, and readiness for training models.

## Features

- **Data Validation**: Detect missing values, duplicates, and outliers.
- **Data Preprocessing**: Perform normalization, encoding, and dataset splitting.
- **Custom Rules**: Allow the definition of custom validation rules tailored to specific needs.
- **Reports**: Generate comprehensive reports on dataset quality.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Abhishek-M-29/ml-data-verifier.git
cd ml-data-verifier
pip install -r requirements.txt
```

## Usage

Run the verifier on your dataset using the following command:

```bash
python verifier.py --input your_dataset.csv --output report.json
```

### Options

- `--input`: Specifies the path to the input dataset.
- `--output`: Specifies the path to save the validation report.
- `--config`: (Optional) Path to a configuration file for custom rules.

## Contributing

We welcome contributions! Feel free to fork the repository and submit a pull request with your improvements or features.

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

## Contact

For any questions or feedback, please reach out to [abhishekmurali2006@gmail.com], [abhishekr.23.becs@acharya.ac.in].
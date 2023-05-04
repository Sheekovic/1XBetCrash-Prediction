# 1XBetCrash Prediction Bot

This is a Telegram bot that predicts the next 10 values of the 'Multiplier' column in the '1XBetCrash.csv' dataset using multiple regression models.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use this bot, you'll need to have the following libraries installed:

- pandas
- scikit-learn
- telebot

You can install them using pip:

```python
pip install pandas scikit-learn telebot
```

## Usage

To use this bot, you'll need to create a Telegram bot and obtain its API token. Once you have the API token, you can run the following command to start the bot:


Once the bot is running, you can send it the `/predict` command to get the predictions.

## Contributing

Contributions are always welcome! If you would like to contribute to this project, you can modify the `1XBetCrashUpdater.py` file to automatically update the `1XBetCrash.csv` file. This will help to strengthen the models that rely on the `Multiplier` column.

To make a contribution, follow these steps:

- Fork the repository
- Clone the repository to your local machine
- Modify the `1XBetCrashUpdater.py` file to update the `1XBetCrash.csv` file
- Test your modifications to ensure they work as expected
- Commit your changes and push them to your forked repository
- Submit a pull request to have your changes reviewed and merged into the main repository.
- Thank you for your contribution!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

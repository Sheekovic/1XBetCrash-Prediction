# 1XBetCrash-PredictionDescription
This project predicts the next 10 values of the "Multiplier" column of the "1XBetCrash.csv" file using multiple machine learning models. The models trained in this project include:

Linear Regression
Decision Tree Regression
Random Forest Regression
Multi-Layer Perceptron Regression
The data is first loaded into a Pandas DataFrame, and the "Multiplier" column is extracted from it. The "Time" and "Multiplier" columns are dropped from the DataFrame, and the remaining data is normalized using StandardScaler. The data is then split into training and test sets using a 70-30 split ratio.

Afterwards, the multiple models are trained using the training data. Each model is used to predict the next 10 values of the "Multiplier" column, and the results are sent to the user via Telegram using the "/predict" command.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/1XBetCrash-Prediction.git
Install the required Python packages:

Copy code
pip install -r requirements.txt
Add your Telegram bot API key in the bot = telebot.TeleBot('<YOUR API KEY HERE>') line of the code.

Usage
Start the Telegram bot by running the following command:

css
Copy code
python main.py
Open Telegram and search for your bot.

Send the "/predict" command to the bot.

Credits
This project was created by Your Name.

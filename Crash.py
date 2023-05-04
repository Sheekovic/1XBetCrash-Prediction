import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import telebot
from telebot.types import Message

# Load the data into a Pandas DataFrame
df = pd.read_csv('1XBetCrash.csv')

# Extract the 'Multiplier' column from the DataFrame
y = df['Multiplier']

# Drop the 'Time' and 'Multiplier' columns from the DataFrame
X = df.drop(columns=['Time', 'Multiplier'])

# Normalize the data using StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and test sets
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=123)

# Train multiple models
linear_reg = LinearRegression()
linear_reg.fit(train_X, train_y)

tree_reg = DecisionTreeRegressor(random_state=123)
tree_reg.fit(train_X, train_y)

forest_reg = RandomForestRegressor(n_estimators=100, random_state=123)
forest_reg.fit(train_X, train_y)

nn_reg = MLPRegressor(hidden_layer_sizes=(100,), max_iter=1000, random_state=123)
nn_reg.fit(train_X, train_y)

# Create a Telegram bot object
bot = telebot.TeleBot('5917307553:AAFD7RgRMF3supp-RdRhFkR9t-E9G-4NRLU')

# Define the handler function for the '/predict' command
@bot.message_handler(commands=['predict'])
def handle_predict(message: Message):
    # Get the chat ID of the user who sent the message
    chat_id = message.chat.id
    
    # Use the trained models to predict the next 10 values of the multiplier
    for model in [linear_reg, tree_reg, forest_reg, nn_reg]:
        predictions = []
        for i in range(1, 11):
            next_X = X[-i].reshape(1, -1)
            next_y = model.predict(next_X)[0]
            predictions.append("Prediction {}: {}".format(i, next_y))

        # Send a separate message for each model's predictions
        bot.send_message(chat_id=chat_id, text="Based on Model: {}".format(model.__class__.__name__))
        bot.send_message(chat_id=chat_id, text='\n'.join(predictions))

# Start the bot
bot.polling()
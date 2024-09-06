# 🚀🚀 1XBetCrash Prediction Bot

This is a Telegram bot that predicts the next 10 values of the 'Multiplier' column in the `1XBetCrash.csv` dataset using multiple regression models.

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#run)
- [Contributing](#contributing)
- [License](#license)

## Installation

### ✅Step 1: Set Up Docker and Remote WSL

To run this project, you will use Docker and Remote WSL. Follow these steps to set up your environment:

1. ✅ **Install Docker**:
   - Download and install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).
   - Ensure Docker is running.

2.✅ **Enable WSL 2**:

- Follow the instructions on [Microsoft's official documentation](https://docs.microsoft.com/en-us/windows/wsl/install) to enable WSL 2.
  - Install a WSL 2 Linux distribution (e.g., Ubuntu) from the Microsoft Store.

3.✅ **Configure Docker to Use WSL 2**:

- Open Docker Desktop and go to Settings.
  - Under the General tab, enable "Use the WSL 2 based engine".
  - Go to the Resources tab, then WSL Integration, and enable integration with your installed Linux distribution.

4.✅ **Install VS Code and Remote WSL Extension**:

- Download and install Visual Studio Code from [Microsoft's official website](https://code.visualstudio.com/).
- Install the "Remote - WSL" extension from the VS Code marketplace.

### ✅ Step 2: Install Python in WSL

Open your WSL terminal and run the following commands to install Python and the necessary libraries:

1.✅ **Update package list**:

    
    sudo apt-get update
    

2.✅ **Install Python 3.6 and pip**:

    
   
    sudo apt-get install python3-pip
    pip3 install --upgrade pip
    

  

3.✅ **Install required libraries**:

    
    pip install pandas scikit-learn telebot
    

### ✅ Step 3: Clone the Repository

If you haven't already, clone your project repository:

    
    git clone https://github.com/aa-sikkkk/FortuneTeller.git
    

### ✅  Step 4: Create and Configure the Telegram Bot

1.Open Telegram and search for @BotFather.
2.Start a chat with @BotFather and use the /start command.
3.Use the /newbot command to create a new bot.
4.Follow the prompts to set the bot's name and username.
5.Once created, @BotFather will provide you with an API token. Save this token.

Update the ```1XBetCrashUpdater.py``` to extract the multiplier values from the Crash Game ```

## RUN

### ✅ Step 5: Run the ```Crash.py``` file

Once ```the Crash.py``` script is running, you can send it the /predict command to your bot to get the predictions for the next 10 values of the 'Multiplier' column.

![Screenshot (23)](https://github.com/aa-sikkkk/FortuneTeller/assets/152005759/e62b1650-6379-4814-80c0-b35b875fe824)


## Contributing

Contributions are always welcome! If you would like to contribute to this project, you can enhance the 1XBetCrashUpdater.py file to automatically update the ```1XBetCrash.csv file.``` This will help improve the accuracy of the models that rely on the 'Multiplier' column.

### ℹ️ℹ️  Steps to Contribute

- Fork the repository.
- Clone the forked repository to your local machine.
- Modify the ```1XBetCrashUpdater.py``` file to update the ```1XBetCrash.csv``` file.
- Test your modifications to ensure they work as expected.
- Commit your changes and push them to your forked repository.
- Submit a pull request to have your changes reviewed and merged into the main repository.

Thank you for your contributions!

## License

This project is licensed under the MIT License - see the [License](https://github.com/aa-sikkkk/FortuneTeller/blob/master/LICENSE) file for details.

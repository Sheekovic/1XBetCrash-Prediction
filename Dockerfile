FROM python:3.12.1

WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Install necessary packages and dependencies for Chrome, ChromeDriver, and Xvfb
RUN apt-get update && \
    apt-get install -y wget unzip xvfb libxi6 libgconf-2-4 libnss3 libxss1 libasound2 libgbm-dev && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean && \
    wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE -O /tmp/chromedriver_latest && \
    CHROMEDRIVER_VERSION=$(cat /tmp/chromedriver_latest) && \
    wget https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip -P /tmp && \
    unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin && \
    rm /tmp/chromedriver_linux64.zip /tmp/chromedriver_latest

# Start Xvfb and run the script
CMD ["bash", "-c", "Xvfb :99 -screen 0 1024x768x16 & export DISPLAY=:99 && python 1XBetCrashUpdater.py"]

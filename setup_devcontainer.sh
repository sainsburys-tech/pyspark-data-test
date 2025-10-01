#!/bin/bash

# Install SDKMAN and Java 17
curl https://get.sdkman.io | bash 
source "/home/vscode/.sdkman/bin/sdkman-init.sh"
sdk install java 17.0.2-open
sdk default java 17.0.2-open
java -version

# Set up Python environment
pip3 install --upgrade pip 
python3 -m venv .venv 
pip3 install --user -r requirements.txt

# Generate initial data
python ./input_data_generator/main_data_generator.py

echo "Development container setup complete."
echo "Java version:"
java -version
echo "Python version:"
python --version
echo "Pip version:"
pip --version
echo "Virtual environment created at .venv"
echo "Initial data generated in the input_data directory."
echo "Test the setup by running \`pytest ./tests\`"
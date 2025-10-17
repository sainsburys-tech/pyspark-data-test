# Data Test - Starter Project

## For Interviewers

### Quick Start with DevContainer (Recommended)

This project includes a devcontainer configuration for easy setup. This is the recommended approach for conducting interviews.

#### Prerequisites for Interviewer
- **Visual Studio Code** with the following extensions:
  - [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
  - [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)
- **Docker Desktop** running on your machine

#### Setup Instructions for Interview

After cloning the repository, open it in VS Code and when prompted choose to open the project in a devcontainer. If not prompted, use the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and select "Dev Containers: Reopen in Container".

**Verify Setup**:
   Once the container is ready, run:
   ```bash
   pytest ./tests
   ```
   This should pass, confirming Java 17, Python, and PySpark are working correctly.

**Start Live Share Session**:
   - Click the "Live Share" button in the status bar (bottom of VS Code)
   - Choose "Start Collaboration Session"
   - Share the generated link with the candidate
   - Grant appropriate permissions (edit access recommended)

#### What the DevContainer Provides
- ✅ **Python 3.12** with all dependencies
- ✅ **Java 17** (installed via SDKMAN)
- ✅ **Generated sample data** (customers, products, transactions)
- ✅ **Working PySpark environment** with proper JVM configuration

#### Troubleshooting
- If container build fails, ensure Docker Desktop is running
- If tests fail, try rebuilding the container: Command Palette → "Dev Containers: Rebuild Container"

---

## For Manual Setup (Candidates or Alternative Setup)

### Prerequisites
#### Java JDK 17

Go to https://www.oracle.com/java/technologies/javase/jdk17-0-13-later-archive-downloads.html
and select the installer appropriate to your operating system.
Click the `Accept License Agreement` radio button and download and run the installer.

#### Python 3.11.* or later.

See installation instructions at: https://www.python.org/downloads/

Check you have python3 installed:

```bash
python3 --version
```

#### Preferably an IDE such as Pycharm Community Edition

https://www.jetbrains.com/pycharm/download/


### Dependencies and data

#### Creating a virtual environment

Ensure your pip (package manager) is up to date:

```bash
pip3 install --upgrade pip
```

To check your pip version run:

```bash
pip3 --version
```

Create the virtual environment in the root of the cloned project:

```bash
python3 -m venv .venv
```

#### Activating the newly created virtual environment

You always want your virtual environment to be active when working on this project.

```bash
source ./.venv/bin/activate
```

#### Installing Python requirements

This will install some of the packages you might find useful:

```bash
pip3 install -r ./requirements.txt
```

#### Running tests to ensure everything is working correctly

```bash
pytest ./tests
```

#### Generating the data

A data generator is included as part of the project in `./input_data_generator/main_data_generator.py`
This allows you to generate a configurable number of months of data.
Although the technical test specification mentions 6 months of data, it's best to generate
less than that initially to help improve the debugging process.

To run the data generator use:

```bash
python ./input_data_generator/main_data_generator.py
```

This should produce customers, products and transaction data under `./input_data/starter`



#### Getting started

The skeleton of a possible solution is provided in `./solution/solution_start.py`
You do not have to use this code if you want to approach the problem in a different way.

### For Interviewers Using Live Share

**Recommended Live Share Settings**:
- **Read/Write Access**: Allow candidate to edit files
- **Terminal Access**: Grant terminal access for running commands

**Candidate Onboarding**:
1. Ask candidate to share their whole screen (not just the VS Code window) for transparency
2. Send the Live Share link
3. Candidate clicks link → opens VS Code → joins session
4. No local setup required for candidate
5. All tools (Python, Java, PySpark) are pre-configured

**During the Interview**:
- Use the integrated terminal for running tests: `pytest ./tests`
- Generated data is available in `./input_data/starter/`

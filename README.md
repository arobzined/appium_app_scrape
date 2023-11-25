# Appium App Scraping

A basic example of how to scrape data from Mobile Apps. I used Android device for that purpose

## Main Idea

Getting information about automobiles from sahibinden mobile app. Basically specify your input
and get information about the cars you are looking for.

## Installation

First of all , you need to download the required platforms and tools to use this application.

### Installing Python
I used Python 3.12.0 in this project so I recommend you to use this version of Python. You can install the version of Python you want by clicking [this link](https://www.python.org/downloads/). You can also follow this [instructors](https://www.javatpoint.com/how-to-set-python-path) to add your Python version to your PATH.
   
### Insalling npm (Node Package Manager) and appium

1.  **Download Node.js:**
    
    -   Visit the official Node.js website: [https://nodejs.org/](https://nodejs.org/).
    -   You will see two versions: LTS (Long Term Support) and Current. For most users, the LTS version is recommended as it is stable and widely used.
    -   Click on the LTS version to download the installer appropriate for your operating system (Windows, macOS, or Linux).
2.  **Install Node.js:**
    
    -   Run the downloaded installer and follow the installation instructions.
    -   During installation on Windows, make sure to check the box that says "Automatically install the necessary tools..." This will install tools like npm as part of the Node.js installation.
3.  **Verify Installation:**
    
    -   Open a command prompt or terminal window.
    -   Type the following commands to check if Node.js and npm are installed:
		>node -v
		>npm -v
    -   If installed correctly, these commands will print the versions of Node.js and npm.


4. **Install Appium:**
	- Run the following command to install Appium globally on your machine:
		>npm install -g appium

	- The `-g` flag installs the Appium package globally, making it available as a command-line tool.

### Installing Android SDK

You need to download Android SDK to use appium so you can test different codes. I suggest you to download [Android Studio](https://developer.android.com/studio) and download SDK from there because it is easier to use. You can follow the instructions inside the application . In my code I used Android 9 (API level 28) so I suggest you to download SDK version 28. 

### Installing UiAutomator2

Since the UiAutomator2 driver is maintained by the core Appium team, it has an 'official' driver name that you can use to install it easily via the [Appium Extension CLI](https://appium.io/docs/en/2.1/cli/extensions/):

>appium  driver  install  uiautomator2

### Installing Genymotion

1.  **Create a Genymotion Account:**
    
    -   Visit the Genymotion website ([https://www.genymotion.com/](https://www.genymotion.com/)).
    -   Sign up for a Genymotion account. You may need to verify your email address.
2.  **Download Genymotion Desktop:**
    
    -   After creating an account, log in to the Genymotion website.
    -   Go to the Genymotion Desktop download page ([https://www.genymotion.com/download/](https://www.genymotion.com/download/)).
    -   Download the appropriate version for your operating system (Windows, macOS, or Linux).
3.  **Install Genymotion Desktop:**
    
    -   Run the installer that you downloaded in the previous step.
    -   Follow the on-screen instructions to install Genymotion on your computer.
4.  **Download and Install VirtualBox (Required for Genymotion):**
    
    -   Genymotion requires a virtualization engine to run virtual Android devices. VirtualBox is a free and widely used virtualization tool that works with Genymotion.
    -   If you don't have VirtualBox installed, download and install it from the VirtualBox website ([https://www.virtualbox.org/](https://www.virtualbox.org/)).
5.  **Configure Genymotion with VirtualBox:**
    
    -   Open Genymotion Desktop after installation.
    -   Log in with your Genymotion account credentials.
    -   In Genymotion, go to "Settings" and navigate to the "ADB" tab.
    -   Set the path to the Android SDK if it's not automatically detected.
6.  **Add and Start a Virtual Device:**
    
    -   In Genymotion, click the "Add" button to add a virtual device.
    -   Choose a virtual device from the list and click "Next."
    -   Follow the on-screen instructions to download and set up the virtual device.
    -   Once the virtual device is added, select it from the list and click "Start" to launch the virtual device.

### Installing APK file

For this project , go to [this link](https://sahibinden-com.tr.uptodown.com/android) and download the apk file , then install the apk file to your android device.

### Install this code

You can clone this code to any directory you want in your local device. Just go to directory you want to install this code and run:
>git clone https://github.com/arobzined/appium_app_scrape.git

You can install required packages using
>pip install requirements.txt

## Usage 

1. Start your Virtual Device
2. Open your terminal and run:
>appium
3. Open another terminal , run:
>python code/main.py

The Input of the code is placed default in the "main.py" file. You can change the variables in the input or , you can change the input with:
>inputs.get_input()

method. Make sure you give the model and brand names correctly because it is required to search given inputs without getting any error. After data extraction is completed , you can found the output in the code file with ".json" extention. The default inputs output file also placed in the code.

## Conclusion

Appium is a powerful package that can directly interact with the applications we use, just like the Selenium package. This application is a comprehensive example that shows automation operations that can be done in mobile applications using the Appium library. I hope this project can help you and add something to the projects you are/will be dealing with. 

## THANKS FOR READING!
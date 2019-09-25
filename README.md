# Monitoring IOT Asset Data for Anomalies Using Python Functions and Dashboards

This sample function uses a regression model to predict the value of one or more output  variables. It compares the actual value to the prediction and generates an alert when the difference between the actual and predicted value is outside of a threshold.

When the reader has completed this Code Pattern, they will understand how to:

* Understand how deploy this Python anomaly function  into  [Watson IOT Platform Analytics](https://www.ibm.com/support/knowledgecenter/en/SSQP8H/iot/analytics/as_overview.html)
* Build a dashboard using [Watson IOT Platform Monitoring Dashboard](https://www.ibm.com/support/knowledgecenter/en/SSQP8H/iot/analytics/as_overview.html) to monitor, visualize, and analyze IOT asset data from [IBM TRIRIGA Building Insights](https://www.ibm.com/support/knowledgecenter/en/SSQP8H/iot/analytics/as_overview.html)
* Deploy, schedule and run this anomaly Python Functions in [Watson IOT Platform Analytics](https://www.ibm.com/support/knowledgecenter/en/SSQP8H/iot/analytics/as_overview.html) to score metrics every 5 minutes to see if there has been an anomaly.

The intended audience for this Code Pattern is application developers and other stakeholders who wish to utilize the power of Watson IOT Platform Monitoring Dashboard to quickly and effectively monitor any asset to ensure availability, utilization and efficiency.

![architecture](./images/architecture.png)

#  Components

* [Watson IOT Platform Analytics](https://www.ibm.com/support/knowledgecenter/en/SSQP8H/iot/analytics/as_overview.html).   Sign up for an account [here](https://www.ibm.com/us-en/marketplace/internet-of-things-cloud/purchase)  An IBM Software as A Service that allows you to register devices, collect IOT Data and build IOT applications.

* [Monitoring Dashboard](https://jupyter.org/) Code free dashboards that allow you to monitor a variety of types of assets.  Use out of the box cards to visualize timeseries data and other asset properties.

* [BI_HTTPPreload](https://ibm.biz/BdzvyX) Python functions that allow you to collect IOT asset and sensor data from other IOT Platforms or data sources that can then be used to quickly monitor your assets in Watson IOT Platform Analytics.


# Flow

1. Setup your Python development environment
2. Create an Entity Type in Watson IOT Platform
3. Deploy Anomaly function
4. Schedule the function to collect asset data
5. Create a Monitoring Dashboard to manage the asset
6. View the Monitoring Dashboard with Building Energy Consumption

# Prerequisites

* An account on IBM Marketplace that has access Watson IOT Platform Analytics [here](https://www.ibm.com/us-en/marketplace/internet-of-things-cloud/purchase)

# Steps

Follow these steps to setup and run this Code Pattern.

1. [Setup your Python development environment](#1-setup-your-python-development-environment)
2. [Create an entity type](#2-create-an-entity-type)
3. [Deploy Function](#3-deploy-function)
4. [Update Function](#3-update-function)
5. [Create a Dashboard](#4-create-dashboard)
6. [View Dashboard](#5-view-dashboard)

## 1. Setup your Python development environment

### Install Python
* Mac comes with Python v2.7.9  recommend using Python v3.6.5 for using DB2. Launch Terminal
```
Launchpad – Other – Terminal
```
* Install Brew which is a package manager for Mac OS
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”
```
* Change directory to your virtual environment
```
brew install python3
```
* Verify version of Python
```
python --version
```

### Install and Create a Virtual Environment
* Launch Terminal
```
Launchpad – Other – Terminal
```
* Install Pip. (Python Package Installer):
```
sudo easy_install pip
```
* Install virtual environment to keep dependencies separate from other projects
```
sudo pip install virtualenv
```
* Create a virtual environment
```
python3 -m venv /path_to_new/virtual_env
```

### Activate Virtual Environment, Install Python Dependencies and Verify Environment
* Change directory to where you made a Virtual Environment
```
cd /path_to_new/virtual_env
```
* Activate your virtual environment
```
source bin/activate
```
* The result in Terminal should be something like:
```
(virtual_env) My-Mac: myuserid$
```
* Install dependencies in from requirements.txt file on next:
```
git clone
cd fun-anomaly
pip install -r requirements.txt
```
* Install Watson IOT Functions dependencies:
```
pip install git+https://@github.com/ibm-watson-iot/functions.git@ --upgrade
```
* Set PYTHONPATH to your project directory:
```
export PYTHONPATH="/Users/carlosferreira/Documents/workspace/fun-weather"
```
* Verify that you can invoke local_test_of_function.py PYTHONPATH to your project directory:
```
python ./scripts/local_test_of_function.py
```

## 2. Create an entity type

* Copy your Watson IOT Platform Service credentials into a credentials.json file
```
browse to your Watson IOT Platform Analytics service
https://dashboard-us.connectedproducts.internetofthings.ibmcloud.com/preauth?tenantid=Think-2019
Explore > Usage > Watson IOT Platform Analytics > Copy to clipboard
```
![credentials](./images/watson_iot_credentials.png)

* Modify your .custom/function.py to reflect your PACKAGE_URL to reflect your forked function Github repository name.  Repace fun-anomaly with your own repo name.
```
PACKAGE_URL = 'git+https://github.com/fe01134/fun-anomaly@'

# Change the class name "SimpleAnomaly" if someone else has already published a function with the same name in your tenant function catalog.

class SimpleAnomaly(BaseRegressor):
```

* Invoke local_test_of_function.py PYTHONPATH to create your Buildings Entity Type and execute your class SimpleAnomaly function to get data from Building Insights:
```
python ./scripts/local_test_of_function.py
```

## 3. Deploy Function

* Push function code changes to Github.
```
git add ./custom/functions.py
git commit -m "my function changes"
git push origin master
```
* Add function to the Entity Type that you created earlier that has your metrics data to run anomaly function on.
```
Explore > Entity Types > Buildings > Add Data > Search on WeatherHTTPPreload
```
![Select function ](./images/create_new_data.png)

* Set values for your anomaly function.
```
URL = enter
a
b
C
```
![credentials](./images/function-tenant.png)

## 4. Update Function
* Push function code changes to Github.
```
git add ./custom/functions.py
git commit -m "my function changes"
git push origin master
```
* Update function input arguments in your created Entity Type to reflect your metrics to evaluate.
```
Explore > Entity Types > Buildings > output_item > configure > next > update
```

## 5. Create Dashboard
* Import the dashboard layout file
```
Explore > Entity Types > Buildings > click gear top right > manage dashboards > import
Choose file  ./json/Staging-Dashboard.json
```
* Save changes
```
save
```

## 6. View Dashboard
* A new Dashboard tab should appear on each entity
```
Explore > Entity Types > Buildings > select an entity which is one of your buildings > Dashboard
```
![dashboard](./images/dashboard.png)


# Learn more

* **Watson IOT Platform Code Patterns**: Enjoyed this Code Pattern? Check out our other [Watson IOT Platform Code Patterns](https://developer.ibm.com/?s=Watson+IOT+Platform).

* **Knowledge Center**:Understand how this Python function can load data into  [Watson IOT Platform Analytics](https://www.ibm.com/support/knowledgecenter/en/SSQP8H/iot/analytics/as_overview.html)

# License

This code pattern is licensed under the Apache Software License, Version 2.  Separate third party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1 (DCO)](https://developercertificate.org/) and the [Apache Software License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache Software License (ASL) FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)

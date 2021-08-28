# capstone-group1
Automatic Social Distancing and Mask detection using Machine Learning
# Packages needed to be installed (Expand this if you use non-default new packages)
### 1. Paho MQTT
```
pip install paho-mqtt
```

### 2. Mosquitto MQTT broker for windows
https://mosquitto.org/

# Project Structure (Tentative)
### 1. Class Mqtt
Contents: APIs for sending and receiving messages in the IoT network 
### 2. Class Encoder
Contents: APIs to encode and decode message used in the IoT network, e.g JSON, XML, HTTP. 
### 3. Class ML
Contents: Machine Learning Algorithms 
### 4. Main Folder
Main Algorithm 

# Writing Rules
Refer into PEP8(https://www.python.org/dev/peps/pep-0008/) Python writing guide, some simple rules that must be implemented:
## 1. Use lowercase letters for function and variables, delimited with underscore (snake_case).
### Dos
```
some_ordinary_function() 
number_of_retries = 10 
connect_into_drive()
```
### Don'ts
```
someOrdinaryFunction() # camelCase is not valid
NumberOfRetries() # PascalCase is not valid
connect-into-drive() # kebab-case is a sin
```
## 2. Use UPPERCASE letters for constants 
```
CONST = 4
```
## 3. Comments, functions , variables, etc are written in english.
### Dos 
```
"""
This function is used for connecting into drive with the provided credentials
"""
def connect_into_drive():
    retries = 3
    return None
```
### Don'ts 
```
"""
此功能用于使用提供的凭据连接到驱动器
"""
def conectar_para_dirigir():
    perulangan = 3
    return None
```
## 4. Use type annotations for functions
### Dos 
```
def is_it_one(x: int) -> string:
    if x == 1:  
        return "Yes"
    return "No"
    
def increment_all_elements(array : np.array) -> None: 
    for count, num in np.ndenumerate(array):
        array[count] = num + 1
    
```
### Don'ts 
```
def is_it_one(x):
     if x == 1:  
        return "Yes"
    return "No"
    
def increment_all_elements(array): 
    for count, num in np.ndenumerate(array):
        array[count] = num + 1
```

## 5. Do Not use long inline statements 
For the love of God this is not a challenge in hackerrank or leetcode. You dont have to crank your code in one line. 
### Dos
```
p = []
for v in range(10000):
    if v%2 == 0:
        p.append("True")
        continue
    p.append("False")
        
```

### Don'ts
```
p = ["True" if v %2 ==0 else "False" for v in range(10000)]
```
All of those rules are enforced so we can put this project into our portofolio.


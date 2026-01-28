#                            **Wi-Fi Network Scanner**



#### **Project Overview**

##### 

##### The Wi-Fi Network Scanner is a desktop-based application developed using Python and Tkinter that allows users to scan, analyze, and monitor nearby wireless networks in real time. The application provides detailed information about available Wi-Fi networks such as SSID, signal strength, quality, encryption type, authentication method, bandwidth, channel number, connected stations, and supported data rates. This tool is especially useful for network administrators, students, and home users to evaluate network performance and troubleshoot connectivity issues.

##### 

#### **Objectives**

##### 

##### The main objective of this project is to design a user-friendly Wi-Fi scanning tool that:

##### 

##### Detects all nearby wireless networks

##### 

##### Displays network details in a structured table format

##### 

##### Evaluates signal quality visually using color indicators

##### 

##### Automatically refreshes network data at regular intervals

##### 

##### Helps users choose the best available Wi-Fi network

##### 

#### **Technology Stack**

##### 

##### Programming Language: Python

##### 

##### GUI Framework: Tkinter

##### 

##### System Command: netsh wlan show networks (Windows)

##### 

##### Libraries Used: subprocess, re, tkinter, ttk

##### 

#### **System Functionality**

##### 

##### The application executes Windows network commands to retrieve real-time Wi-Fi data. It processes the command output using regular expressions and displays the extracted information in a table (Treeview). Signal strength is categorized into Excellent, Good, or Poor, with corresponding color codes (green, orange, red) for better visualization. The tool also identifies whether a network operates on 2.4 GHz or 5 GHz based on the channel number.

##### 

#### **Features**

##### 

##### One-click Wi-Fi network scanning

##### 

##### Auto-refresh every 10 seconds

##### 

##### Signal strength and quality classification

##### 

##### Display of security details (WPA2, CCMP, etc.)

##### 

##### Clean and responsive graphical user interface

##### 

##### Color-coded signal quality indicators

##### 

#### **Applications**

##### 

##### Network performance analysis

##### 

##### Wi-Fi troubleshooting

##### 

##### Educational use for networking concepts

##### 

##### Optimal channel and network selection

##### 

#### **Conclusion**

##### 

##### The Wi-Fi Network Scanner is an efficient and lightweight tool that simplifies wireless network analysis through an intuitive interface. By combining system-level commands with a graphical display, the project demonstrates practical use of Python in networking and GUI development. This application can be further enhanced by adding features such as network connection management, signal graphs, and cross-platform support.


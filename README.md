# eternalblue_scanner

This script creates a GUI application that allows users to check if a specific IP address is vulnerable to the EternalBlue exploit. It uses the Python modules tkinter, nmap, socket, and threading. The GUI consists of an IP address entry box, a "Check" button, a progress bar, and a label that displays the result of the scan. When the user clicks the "Check" button, the script checks if the entered IP address is valid, and if so, it uses Nmap to scan for the EternalBlue exploit status of that IP address. While the scan is running, a progress bar shows the progress of the scan. Once the scan is complete, the label displays whether the EternalBlue exploit is possible or not.



![et1](https://user-images.githubusercontent.com/128103079/226227582-2b698e27-7c04-48d3-b897-cfbf76880ece.jpg)

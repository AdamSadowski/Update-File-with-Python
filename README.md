<h1>Updating file using Python algorithm</h1>


<h2>Description</h2>
The project showcases Python 3 skills used to update a file in order to remove certain IP addresses from the set allowed on an imaginary network. A simple project that showcases the ability to automate responsibilities that require diligent, but repetitive work. Within the scenario the starting file containing allowed ip addresses will be called allow_list.txt. This file will be updated with the contents of a file called remove_list.txt. The whole code is posted into subdirectory
<br />


<h2>Languages Used</h2>

- <b>Python 3</b> 

<h2>Environments Used </h2>

- <b>Windows 11</b>
- <b>SublimeText code editor</b>

<h2>Program walk-through:</h2>

<p align="center">
Starting point - allow_list.txt <br/>
<br />
<br />
<img src="https://i.imgur.com/7UVSCWD.png" title="source: imgur.com" height="80%" width="80%"/>
<br />
<br />
List of IP addresses to be removed from the allow_list.txt file: <br/>
<img src="https://i.imgur.com/d8RFDgq.png" title="source: imgur.com" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
First part of code - define destination of files and open them for reading. With key word is used to better manage resources as it will close the files after exiting the with statement:  <br/>
<br />
<img src="https://i.imgur.com/77SYaFB.png" title="source: imgur.com" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Converting the files to lists in order to be able to read each of them:  <br/>
<img src="https://i.imgur.com/5RHTGbt.png" title="source: imgur.com" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Creating a copy of list to be modified to avoid modification of the original file:  <br/>
<img src="https://i.imgur.com/iVvjb3d.png" title="source: imgur.com" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Script removes IP addresses listed in remove_list and joins filtered IP addresses into a string adding spaces for readability:  <br/>
<img src="https://i.imgur.com/PIbL1mE.png" title="source: imgur.com" height="80%" width="80%"/>
<br />
<br />
Finally script opens allow_list.txt and writes modified string of IP address to it:  <br/>
<img src="https://i.imgur.com/WETdGsd.png" title="source: imgur.com" height="80%" width="80%"/>
<br />
<br />
To execute code on sample I navigate to a folder where script and files are stored:  <br/>
<img src="https://i.imgur.com/8QnNADd.png" title="source: imgur.com" height="80%" width="80%""/>
<br />
<br />
And observe the outcome 😸:  <br/>
<img src="https://i.imgur.com/U1snyAX.png" title="source: imgur.com" height="80%" width="80%""/>
<br />
<br />
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>

<h2>Password pwn cheking GUI</h2>

This program is graphical user interface for checking pwned passwords, it's writen with python and pyQT4.
Program calculates password hash and then finds all prefix matches from <b>https://api.pwnedpasswords.com</b>,
then full hash match is found <b>localy</b> on users machine.
<br>
<b>NOTE:</b> there are no support for proxies.
<br>
<br>
![pwnCheck](https://raw.githubusercontent.com/f5AFfMhv/pwnCheck_GUI/master/pwnCheck_v1.png)

 <h3>Prebuild packages</h3>
You can download prebuild packages from sourceforge. Executables were made with <b>pyinstaller</b>.
 <table style="width:100%">
  <tr>
    <th>Link</th>
    <th>Tested</th>
  </tr>
  <tr>
    <td><a href="https://sourceforge.net/projects/pwncheck/files/pwnCheck_v1.0_amd64.exe/download">pwnCheck_v1.0_amd64.exe</a></td>
    <td>Windows 10 <br> Windows 7</td>
  </tr>
  <tr>
    <td><a href="https://sourceforge.net/projects/pwncheck/files/pwnCheck_1.0_amd64.deb/download">pwnCheck_1.0_amd64.deb</a></td>
    <td>LinuxMint 19 <br> Ubuntu 18</td>
  </tr>
</table> 

<h3>Dependencies</h3>
<ul>
  <li>Python 2.7</li>
  <li>QT4</li>
</ul>

<h3>Instalation</h3>

Install dependencies and run main.py.

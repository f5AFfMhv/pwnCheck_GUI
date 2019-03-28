#!/usr/bin/env python

"""
This program is a graphical user interface for checking pwned passwords, it's writen with python and pyQT4.
Program calculates password hash and then searches for matches with first 5 symbols (prefix) in https://api.pwnedpasswords.com,
then full hash match is found localy on users PC.

Copyright (C) 2019 Martynas J. 
f5AFfMhv@protonmail.com  
https://github.com/f5AFfMhv

This file is part of pwnCheck.

    pwnCheck is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    pwnCheck is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with pwnCheck.  If not, see <https://www.gnu.org/licenses/>.
"""

# TODO:


# FIXME:



from PyQt4 import QtGui, QtCore # Import the PyQt4 modules we'll need
import sys  # We need sys so that we can pass argv to QApplication
import hashlib # Library for hash calculation
import urllib2 # Library for 
import re # library for searching regular expressions
import qtGUI # file converted from QT design 


class App(QtGui.QMainWindow, qtGUI.Ui_MainWindow):
    def __init__(self):
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in qtGUI.py file automatically
        # It sets up layout and widgets that are defined
        # Input object signal connetion to function
        self.checkButton.clicked.connect(self.pwncheck) 
        self.passwordLineEdit.returnPressed.connect(self.pwncheck)

    def pwncheck(self): # Function for checking pwned passwords
        self.output_text = "SHA1: "
        # Calculate SHA1 of entered password
        self.password_hash = hashlib.sha1(str(self.passwordLineEdit.text())).hexdigest()
        self.output_text += "<b>" + self.password_hash + "</b>" + "<br>"
        # Separate prefix and postfix
        self.prefix = self.password_hash[0:5]
        self.postfix = self.password_hash[5:].upper()
        # Download SHA1 hashes with matching prefixes
        self.url = "https://api.pwnedpasswords.com/range/" + self.prefix
        self.prefix_matches = urllib2.urlopen(self.url).read()
        self.prefix_matches_count = len(self.prefix_matches.split('\n'))
        self.password_match = ""
        # Search for postfix match
        for self.word in self.prefix_matches.split():
            if re.search(self.postfix, self.word):
                self.password_match = self.word
        if self.password_match:
            # Postfix match found
            self.output_text += "<h3>" + "PASSWORD PWNED " + self.password_match.split(":")[1] + " TIMES!" + "</h3>"
            self.resultLabel.setStyleSheet(QtCore.QString.fromUtf8("background-color: rgb(255, 0, 0);"))
        else:
            # Postfix match wasn't found
            self.output_text += "<h3>" + "PASSWORD WAS NOT FOUND IN THE DB" + "</h3>"
            self.resultLabel.setStyleSheet(QtCore.QString.fromUtf8("background-color: rgb(0, 255, 0);"))
        # Output message
        self.resultLabel.setText(self.output_text)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = App()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
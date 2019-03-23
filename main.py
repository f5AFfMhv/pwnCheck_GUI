#!/usr/bin/env python

"""
This program is graphical user interface for checking pwned passwords, it's writen with python and pyQT4.
Program calculates password hash and then searches all matches with first 5 symbols in https://api.pwnedpasswords.com,
then full hash match is found localy on users machine.

Copyright (C) 2018 Martynas J. f5AFfMhv@protonmail.com  

This file is part of OpenVPN_GUI.

    OpenVPN_GUI is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenVPN_GUI is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with OpenVPN_GUI.  If not, see <https://www.gnu.org/licenses/>.
"""

# TODO:


# FIXME:



from PyQt4 import QtGui # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
import hashlib
import urllib2
import re
import qtGUI  # This file holds our MainWindow and all design related things


class App(QtGui.QMainWindow, qtGUI.Ui_MainWindow):
    def __init__(self):
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        self.checkButton.clicked.connect(self.pwncheck)
        self.passwordLineEdit.returnPressed.connect(self.pwncheck)
        self.fill_info()

    def fill_info(self):
        try:
            with open("README.md","r") as self.readme_file: 
                self.readme = self.readme_file.read()
        except:
            self.readme = "No README file found"

        self.descriptionLabel.setText(self.readme)

        try:
            with open("COPYING","r") as self.license_file: 
                self.license = self.license_file.read()
        except:
            self.license = "No README file found"

        self.licenseLabel.setText(self.license)

    def pwncheck(self):
        self.output_text = "SHA1: "
        self.password_hash = hashlib.sha1(str(self.passwordLineEdit.text())).hexdigest()
        self.output_text += "<b>" + self.password_hash + "</b>" + "<br>"
        self.prefix = self.password_hash[0:5]
        self.postfix = self.password_hash[5:].upper()
        self.output_text += "prefix: " + "<b>" + self.prefix + "</b>" + "<br>"
        self.url = "https://api.pwnedpasswords.com/range/" + self.prefix
        self.prefix_matches = urllib2.urlopen(self.url).read()
        self.prefix_matches_count = len(self.prefix_matches.split('\n'))
        self.output_text += "found " + "<b>" + str(self.prefix_matches_count) + "</b>" + " prefix matches" + "<br>"
        self.password_match = re.search(self.postfix, self.prefix_matches)
        if self.password_match:
            self.output_text += "password pwned"
        else:
            self.output_text += "password was not found in the DB"

        self.resultLabel.setText(self.output_text)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = App()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
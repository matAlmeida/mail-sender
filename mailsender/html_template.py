import codecs
from bs4 import BeautifulSoup
import re
import os


class HTMLTemplate:
    def __init__(self, htmlFilePath):
        """
        Create a Template
            :param htmlFilePath: Path to a html file that will be used as template. The variables names in the HTML file be defined inside a double-{ structure
        """
        dirname = os.path.dirname(__file__)
        self.htmlFilePath = os.path.join(dirname, htmlFilePath)
        try:
            file = codecs.open(self.htmlFilePath, 'r', 'utf-8')
            self.htmlFile = BeautifulSoup(file.read(), "html.parser")
            self.variables = re.findall(
                r'\{\{([\w]+)\}\}', self.htmlFile.prettify())

            file.close()
        except FileNotFoundError:
            print(f'File not found at: {self.htmlFilePath}')

        self.__dictionary = None  # Will be used to create new emails using this template
        pass

    def get_variables(self):
        """
        Return all variables defined for this template
        """
        return self.variables

    def __sub_template__(self, matchObj):
        """
        Callback function for the Regex Substitution
            :param matchObj: The matched object
        """
        if matchObj.group(1) in self.__dictionary.keys():
            return self.__dictionary[matchObj.group(1)]
        else:
            return matchObj.group(0)

    def new_mail(self, values):
        """
        Return a HTML based in this template with the variables changed
            :param values: A dictionary with the pre-defined variables as key and their value for this template
        """
        self.__dictionary = values
        template = self.htmlFile.prettify().replace('\n', '').replace('\r', '')
        newMail = re.sub(r'\{\{([\w]+)\}\}', self.__sub_template__, template)
        self.__dictionary = None

        return newMail

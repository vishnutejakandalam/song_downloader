"""This code contains the major song class."""


class Song:
    url:str = ""
    img_url:str = ""
    def __init__(self, token, name, year, album):
        """Constructor to initialise all the values of he song."""
        self.token = token
        self.name = name
        self.year = year
        self.album = album
    
    def print_all(self):
        """This method prints all the details of the song"""
        print(self.token, self.name, self.year, self.album, self.url, self.img_url)

    
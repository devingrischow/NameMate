"""
This Is the main class of the program, run this to start the program. 
This program uses databases to easily rapidly research different names and companies rapidly.
"""

import DataBaseManager
import webbrowser
dbm = DataBaseManager.DATABASE_MANAGER()
class NameMate:
    


    def __init__(self):

        self.userSearch = ''

    def run(self):
        request = input("What would you like to Search for?\nA.App Name\nB.Company Name\nC.Both\nD.Add A New Add Search Query\nE.Add A new Companny Search Query\n\n\n")
        request = request.lower()

        if request == 'a':
            self.appSearch()
        elif request == 'b':
            self.companySearch()
        elif request == 'c':
            self.both()
        elif request == 'd':
            self.addNewAppQuery()
        elif request == 'e':
            self.addCompanyQuery()
        else:
            print("error, please try again\n\n")
            self.run()
        
    #gathers all the possible search queries from the apps table and sends them to the google search function
    def appSearch(self):
        searches = dbm.search_for_AppNames()
        self.openSearches(searches)
        # for entry in searches:
        #     entry = entry[0]
        #     print(entry, 'entry')


    def companySearch(self):
        searches = dbm.search_for_CompanyNames()
        self.openSearches(searches)

    def both(self):

        self.appSearch()
        self.companySearch()    

    def openSearches(self, searchList):
        taburl = "https://www.google.com/search?q="
        searchTerm = input("Enter A Name To Search For:     ")
        searchTerm = searchTerm.replace(' ', '+')
        #remove first search and open a new browser
        
        c = webbrowser.get('safari')
        c.open_new(f'{taburl}{searchTerm}')


        for search in searchList:
            search = search[0]
            newSearch = f"{taburl}{searchTerm} {search}"
            #newSearch = f"{taburl}{searchTerm}+{search}&start=0"
            c.open_new_tab(f'{newSearch}')
        self.run()

    def addNewAppQuery(self):
        newAppQuery = input("Enter a new search query to: \nFollow this formula: ___ *Query*\n")

        dbm.newappQuery(newAppQuery)
        self.run()

    def addCompanyQuery(self):
        newAppQuery = input("Enter a new search query to: \nFollow this formula: ___ *Query*\n")

        dbm.newcompanyQuery(newAppQuery)
        self.run()
        



        




n = NameMate()
n.run()
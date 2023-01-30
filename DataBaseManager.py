import sqlite3

class DATABASE_MANAGER:
    def __init__(self):
        
        self.database = sqlite3.connect('NameMateSearches.db')
        self.cursor = self.database.cursor()

    def newappQuery(self, QUERY):
        newQuery = f"""INSERT INTO AppSearches (searchQuery) VALUES ('{QUERY}');"""
        self.cursor.execute(newQuery)
        self.database.commit()

    def newcompanyQuery(self, QUERY):
        newQuery = f"""INSERT INTO CompanySearches (searchQuery) VALUES ('{QUERY}');"""
        self.cursor.execute(newQuery)
        self.database.commit()

    

    def search_for_AppNames(self):
        searches = f"""SELECT searchQuery FROM AppSearches"""
        self.cursor.execute(searches)
        list_of_searches = self.cursor.fetchall()
        return list_of_searches

    def search_for_CompanyNames(self):
        searches = f"""SELECT searchQuery FROM CompanySearches"""
        self.cursor.execute(searches)
        list_of_searches = self.cursor.fetchall()
        return list_of_searches
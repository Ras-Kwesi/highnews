class Articles:
    '''
    definition of the news class properties
    '''

    def __init__(self,title,author,description,url,urlToImage,publishedAt):
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage # The link to the URL will be object.image, which points to urlToImage
        self.publishedAt = publishedAt






class Source:
    '''
    definition for the news sources class
    '''

    

    def __init__(self, id, name, url, category, language, country,description):
        self.id = id
        self.name = name
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        self.description = description



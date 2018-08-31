class Articles:
    '''
    definition of the news class properties
    '''

    def __init__(self,title,author,description,url,urlToImage,publishedAt):
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.image = urlToImage # The link to the URL will be object.image, which points to urlToImage
        self.time = publishedAt






class Source:
    '''
    definition for the news sources class
    '''

    sourceNewsList = []

    def __init__(self, id, name, url, category, language, country):
        self.id = id
        self.name = name
        self.url = url
        self.category = category
        self.language = language
        self.country = country



        
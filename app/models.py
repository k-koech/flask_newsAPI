class Source:
    '''
    Source class to define source Objects
    '''

    def __init__(self,id,name,description,url,language,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.language = language
        self.country = country

class Article:
    '''
    Article class to define article Objects
    '''
    def __init__(self,author,title,description,image,url,date_published,content):
        self.author =author
        self.title = title
        self.description = description
        self.url =  url
        self.image = image
        self.date_published = date_published
        self.content = content
class Article:
    all = []

    def __init__(self, author, magazine, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise TypeError("Title must be a string")
        self._author = author
        self._magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @title.setter
    def title(self, value):
        raise AttributeError("can't set attribute")

    @author.setter
    def author(self, value):
        raise AttributeError("can't set attribute")

    @magazine.setter
    def magazine(self, value):
        raise AttributeError("can't set attribute")


class Author:
    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("Name must be a string")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("can't set attribute")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list(set(article.magazine.category for article in self.articles()))
        return categories if categories else None


class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("Name must be a string")
        if isinstance(category, str):
            self._category = category
        else:
            raise TypeError("Category must be a string")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("Name must be a string")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str):
            self._category = value
        else:
            raise TypeError("Category must be a string")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [author for author in self.contributors() if len([article for article in author.articles() if article.magazine == self]) > 2]
        return authors if authors else None

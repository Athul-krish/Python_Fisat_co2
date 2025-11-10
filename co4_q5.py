class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Publisher Name: {self.name}")


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")	
		
class Python(Book):
    def __init__(self, name, title, author, price, pageno):
        super().__init__(name, title, author)
        self.price = price
        self.pageno = pageno

    def display(self):
        super().display()
        print(f"Price: ${self.price}")
        print(f"Number of Pages: {self.pageno}")
        
book = Python("java","HELLO","Athul",2000,160)
book1 = Python("C","hii","Athul",300,100)
book.display()
book1.display()
	


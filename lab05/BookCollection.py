from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def getNumberOfBooks(self): # length
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def insertBook(self, book):
        current = self.head
        previous = None
        done = False
        while current != None and not done:
            if current.getData() > book:
                done = True
            else:
                previous = current
                current = current.getNext()
        temp = BookCollectionNode(book)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
    
    def getBooksByAuthor(self,author):
        current = self.head
        book_str = ""
        while current != None:       
            if current.getData().getAuthor().lower() == author.lower():
                book_str += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return book_str
 
    def getAllBooksInCollection(self):
        current = self.head
        all_books = ""
        while current != None:
            all_books += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return all_books

    def removeAuthor(self, author):
        current = self.head
        prev = None
        while current != None:
            if current.getData().getAuthor().lower() == author.lower():
                if prev == None:
                    self.head = current.getNext()
                else:
                    prev.setNext(current.getNext())
                current = current.getNext()
            else:
                prev = current
                current = current.getNext()

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        if bookNode.getData().getTitle().lower() == title.lower():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.next)

# b0 = Book("Cujo", "King, Stephen", 1981)
# b1 = Book("The Shining", "King, Stephen", 1977)
# b2 = Book("Ready Player One", "Cline, Ernest", 2011)
# b3 = Book("Rage", "King, Stephen", 1977)
# b4 = Book("Divergent", "Roth, Veronica", 2011)
# b5 = Book("Insurgent", "Roth, Veronica", 2012)

# bc = BookCollection()
# bc.insertBook(b0)
# bc.insertBook(b1)
# bc.insertBook(b2)
# bc.insertBook(b3)
# bc.insertBook(b4)
# bc.insertBook(b5)
# print(bc.getAllBooksInCollection())


# b0 = Book("Cujo", "King, Stephen", 1981)
# b1 = Book("The Shining", "King, Stephen", 1977)
# bc = BookCollection()
# bc.insertBook(b0)
# bc.insertBook(b1)
# assert bc.recursiveSearchTitle("CUJO", bc.head) == True
# assert bc.recursiveSearchTitle("Twilight", bc.head) == False
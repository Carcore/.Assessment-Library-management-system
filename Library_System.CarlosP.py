books = {}  # We create a dictionary to store book records.
taken_books = {} #We create a list for taken books , to be removed from books list

def add_book(): #We define first function.
    book_title = input("Enter Book Title: ").strip() #User to enter the book tittle and we remove the whitespace.
    if book_title in books: #Check the book is on the list.
        print("Error: This Book Title already exists!")
        return

    author = input("Enter Author: ").strip() #User to enter the author
    genre = input("Enter Genre: ").strip()  #User to enter the genre

    if not book_title or not author or not genre: #condition to check user enterer all the fields required.
        print("All fields must be filled.") #Message to be printed in case a field is empty.
        return

    books[book_title] = {  #Add a new book details to books dicntionary list.
        'author': author,
        'genre': genre
    }

    print("Book added successfully!") #Information message.
    
def display_books(): #We defined a function.
    if not books:      #Condition to check if there are books to display.
        print("No books found!")
        return

    print("\nBooks List:")   #We print the book details from books list.
    print("Title\t\tAuthor\t\tGenre")
    print("-" * 40)

    for book_title, details in books.items():
        author = details.get('author', 'N/A')
        genre = details.get('genre', 'N/A')
        print(f"{book_title}\t{author}\t{genre}")

def search_book():  #We define function.
    book_title = input("Enter Book Title to search: ").strip() #Users enter tittle for a search.
    if book_title in books:  #Condition to check is the tittle is on the library.
        details = books[book_title]
        print(f"\nBook Found:\nTitle: {book_title}\nAuthor: {details.get('author', 'N/A')}\nGenre: {details.get('genre', 'N/A')}")
    else:
        print("Error: Book not found!")


def take_book(): #We define a fucntion.
    book_title = input("Enter Book Title: ").strip() #We as user to enter a book title.

    if book_title.isdigit(): #Condition to validate the right data type is entered.
        print("Error: Book title should be a string, not a number!")
        return

    if book_title in books:    #If the book is on the list, removes it from books list and add it to taken_books list.
        taken_books[book_title] = books.pop(book_title)
        print("Enjoy this book!")
    else:
        print("Error: Book not available!")
        
def return_book():  #We definde a function.
    book_title = input("Enter Book Title to Return: ").strip()

    if book_title in taken_books:  #Condition to check if the book is on taken_books list, remove it from that list and add it to books list
        books[book_title] = taken_books.pop(book_title)
        print("Thank you for returning the book!")
    elif book_title in books:
        print("This book is already in the books list.")
        
while True:   #LOOP to display the menu and get user choice.
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books List")
    print("3. Search Book")
    print("4. Take a Book")
    print("5. Return a Book")
    print("6. Exit")
    
    try:  #Error handling.
        choice = input("Enter your choice (1-6): ").strip()
         # Call the appropriate function based on user choice.
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            take_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
    
    except Exception:
        print(f"An unexpected error occurred: ")

     
     
     
     
    
  


        

        






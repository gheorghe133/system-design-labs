import spacy, re
nlp = spacy.load("en_core_web_sm")

vague_terms = ["appropriate","user-friendly","fast","as required","etc","TBD","may","should"]
requirements = [
("SRS-001","The system shall display the user account information including user ID, last and first name, and user position, privilege."),
("SRS-002","The system shall use a graphic user interface which allows librarians to choose actions including removing, changing and adding user accounts and information."),
("SRS-003","When checking out books, the system shall show all borrowing information about a particular user including first and last name, library card number, expiry date, unpaid penalties and number of unreturned books."),
("SRS-004","When checking out books, the system shall show information about books borrowed before and not returned yet including ISBN, title, borrowing and due date, and branch checked out."),
("SRS-005","When checking out books, the system shall display the information of the book being checked out including ISBN, title and due date."),
("SRS-006","When checking in books, the system shall show the title and ISBN of the book being checked in and display a check-in stamp when finished."),
("SRS-007","When recalling a book, the system shall display a list of all copies borrowed out ordered by lend-out time."),
("SRS-008","When the recalled book arrives, the system shall display user name, recall date and arrival date; if more than one user waits, users shall be displayed ordered by recalling time, and a check-in recall stamp shall appear when done."),
("SRS-009","The system shall display a list of books matching the search criteria sorted by title including category, ISBN, title and author."),
("SRS-010","The system shall allow a user to enter data via keyboard or choose an item via mouse."),
("SRS-011","Whenever date data is needed, it shall be entered only by choosing a date from an online calendar."),
("SRS-012","The system shall allow the user to enter the library card number and ISBN either by typing or scanning."),
("SRS-013","The system shall allow the user to enter book borrowing or recalling data as frequently as required."),
("SRS-014","The system shall allow the user to attach notes to each account."),
("SRS-015","The system shall allow the user to add or change account information including last name, first name, user ID, position and privilege."),
("SRS-016","The system shall allow the user to delete an entire account."),
("SRS-017","The system shall allow the user to specify a checking-out book using its ISBN."),
("SRS-018","The system shall allow the user to specify a patron by the library card number."),
("SRS-019","The system shall allow the user to specify a checking-in book using its ISBN."),
("SRS-020","The system shall allow the user to specify that a penalty is paid."),
("SRS-021","The system shall check and show the number of books checked out and whether this exceeds the limit for patrons except librarian card holders."),
("SRS-022","The system shall check and show if the book can only be used in the library."),
("SRS-023","The system shall let librarian card holders check out books that can only be used in the library."),
("SRS-024","The system shall commit the check-in and check-out data to the database as soon as the data is entered."),
("SRS-025","The system shall allow the user to specify a recalled book by its ISBN."),
("SRS-026","The system shall allow the user to choose one copy of a book to recall from a list of copies borrowed out."),
("SRS-027","The system shall allow the user to record the recall notification send-out date, arrival date and pick-up notification send-out date."),
("SRS-028","The system shall allow the user to type in search criteria including book title, keyword in title, ISBN, subject or category."),
("SRS-029","The system shall allow the user to choose a language option (English, Spanish, French) for the searched book."),
("SRS-030","If the search results in a list of books, the system shall allow the user to choose any one to see its details."),
("SRS-031","The system shall allow the user to add or change record information including category, title, ISBN, publisher, description, library location, purchase date and price."),
("SRS-032","The system shall allow the user to mark an existing book as deleted and specify the deletion reason."),
("SRS-034","The system shall allow the user to generate a report showing information on all signed-out books in a period grouped by book categories."),
("SRS-035","The system shall allow the user to generate a report showing information about users with overdue books and penalties."),
("SRS-036","The system shall allow the user to generate a report showing information about a particular patron."),
("SRS-037","The system shall allow the user to generate a report showing purchase information in a period including titles, category, author, publisher and price, plus total statistics per category."),
("SRS-038","The system shall generate those reports to display, file or printer linked to the system."),
("SRS-039","The check-in and check-out system shall respond to the user in no more than 5 seconds; the search function shall respond in no more than 9 seconds."),
("SRS-040","The system shall be installed in a Windows NT network."),
("SRS-041","The account management system shall only be used by managers or users with defined privileges."),
("SRS-042","The check-in, check-out and recall system shall only be used by users who have librarian ID."),
("SRS-043","The patron information report shall only be generated by users who have librarian ID."),
("SRS-044","The book sign-out or purchase report shall only be generated by managers or users with defined privileges."),
("SRS-045","Database update data shall be committed only after approval by managers."),
("SRS-046","The system shall show appropriate messages at terminal when the system is down.")
]

for req_id,text in requirements:
    doc = nlp(text)
    vag = [v for v in vague_terms if v in text.lower()]
    print(req_id, "Ambiguă" if vag else "Clară", vag)
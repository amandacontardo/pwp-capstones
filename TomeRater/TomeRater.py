class User(object):
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}

	def get_email(self):
		return self.email

	def change_email(self, address):
		self.email = address
		print(self.name + "'s email has been updated")

	def __repr__(self):
		return "User {}, email: {}, books read: {}".format(self.name, self.email, len(self.books))

	def __eq__(self, other_user):
		return (self.name == other_user.name and self.email == other_user.email)
		
	def read_book(self, book, rating = None):
		self.books[book] = rating
		
	def get_average_rating(self):
		total_ratings = 0
		count = 0
		for book in self.books.keys():
			if self.books[book] != None:
				total_ratings += self.books[book]
				count += 1
		return total_ratings/count
	
		
class Book(object):
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []

	def get_title(self):
		return self.title
		
	def get_isbn(self):
		return self.isbn
		
	def set_isbn(self, new_isbn):
		self.isbn = new_isbn
		print(self.title + "'s ISBN has been updated")
		
	def add_rating(self, rating):
		if (rating != None and rating >= 0 and rating <= 4):
			self.ratings.append(rating)
		else:
			print("Invalid Rating")
			
	def __eq__ (self, other_book):
		return (self.title == other_book.title and self.isbn == other_book.isbn)
		
	def get_average_rating(self):
		total_rating = 0
		for rating in self.ratings:
			total_rating += rating
		return total_rating/len(self.ratings)
		
	def __hash__(self):
		return hash((self.title, self.isbn))
		
	def __repr__(self):
		return self.title
			
		
class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author
		
	def get_author(self):
		return self.author
		
	def __repr__(self):
		return "{} by {}".format(self.title, self.author)
		
		
class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level		
		
	def get_subject(self):
		return self.subject
		
	def get_level(self):
		return self.level
		
	def __repr__(self):
		return "{}, a {} manual on {}".format(self.title, self.level, self.subject)
		

class TomeRater():
	def __init__(self):
		self.users = {}
		self.books = {}
	
	def create_book(self, title, isbn):
		exists = False
		for book in self.books.keys():
			if isbn == book.get_isbn():
				exists = True
		if exists == False:	
			return Book(title,isbn)
		else:
			print("ISBN already in use")
	
	def create_novel(self, title, author, isbn ):
		exists = False
		for book in self.books.keys():
			if isbn == book.get_isbn():
				exists = True
		if exists == False:	
			return Fiction(title, author, isbn)
		else:
			print("ISBN already in use")
			
	def create_non_fiction(self, title, subject, level, isbn):
		exists = False
		for book in self.books.keys():
			if isbn == book.get_isbn():
				exists = True
		if exists == False:
			return Non_Fiction(title, subject, level, isbn)
		else:
			print("ISBN already in use")
			
	def add_book_to_user(self, book, email, rating = None):
		if email in self.users:
			self.users[email].read_book(book, rating)
			book.add_rating(rating)
			if book in self.books:
				self.books[book] = self.books[book] + 1
			else:
				self.books[book] = 1
		else:
			print("No user with email {}!".format(email))
			
	def add_user(self, name, email, user_books = None):
		if email in self.users:
			print("This user already exists")
		elif email.find("@") < 0 or (email.find(".com") < 0 and email.find(".edu") < 0 and email.find(".org") < 0) :
			print("Email is not in appropriate format")
		else:
			new_user = User(name, email)
			self.users[email] = new_user
			if user_books != None:
				for book in user_books:
					self.add_book_to_user(book, email)
					
	def print_catalog(self):
		for book in self.books.keys():
			print(book)
	
	def print_users(self):
		for user in self.users.values():
			print(user)
	
	def get_most_read_book(self):
		max = 0
		for book, count in self.books.items():
			if count > max:
				max = count
				max_book = book
		return max_book
		
	def highest_rated_book(self):
		high = 0
		for book in self.books.keys():
			avg_rating = book.get_average_rating() 
			if avg_rating > high:
				high = avg_rating
				high_book = book
		return high_book
	
	def most_positive_user(self):
		high_avg_rate = 0
		for user in self.users.values():
			user_avg_rate = user.get_average_rating()
			if user_avg_rate > high_avg_rate:
				high_avg_rate = user_avg_rate
				high_avg_user = user
		return high_avg_user
			
			
			
			

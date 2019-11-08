from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, MenuItem ,User

#engine = create_engine('sqlite:///categorymenu.db')
engine = create_engine('postgresql://catalog:password@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Nada", email="nadaaskora@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for first year
category1 = Category(user_id=1,name="first year")

session.add(category1)
session.commit()


menuItem1 = MenuItem(user_id=1 ,name="c++", description="Beginner",
                      course="Programming", category=category1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1 ,name="Photoshop", description="Beginner",
                    course="Design", category=category1)

session.add(menuItem2)
session.commit()


# Menu for second year
category2 = Category(user_id=1 ,name="Second year")

session.add(category2)
session.commit()


menuItem1 = MenuItem(user_id=1 ,name="photoshop", description="intermediate",
                      course="Design", category=category2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    user_id=1 ,name="digital marketing ", description="Beginner", course="Marketing", category=category2)

session.add(menuItem2)
session.commit()


# Menu for third year
category1 = Category(user_id=1 ,name="Third year")

session.add(category1)
session.commit()


menuItem1 = MenuItem(user_id=1 ,name="digital marketing", description="intermediate",
                      course="Marketing", category=category1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1 ,name="Project Management", description="Beginner",
                     course="Business", category=category1)

session.add(menuItem2)
session.commit()



# Menu for fourth year
category1 = Category(user_id=1 ,name="Fourth year")

session.add(category1)
session.commit()


menuItem1 = MenuItem(user_id=1 ,name="illustrator", description="Beginner",
                      course="Design", category=category1)

session.add(menuItem1)
session.commit()



print "added menu items!"

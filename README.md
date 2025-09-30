Booking System Project
Introduction
The project is Python based Booking System, which was developed because of my education on Software Development Fundamentals. This project will not focus on the development of a commercial application; rather it will be a straightforward application of software design principles in a simple and real-world inspired program.
The system allows users to:
- Type in personal information (ID, name)
- Select services (such as ferry bookings)
- Calculate the total cost
- Approve or reject bookings
The project made me realize that Object-Oriented Programming (OOP) can be applied to create clean, modular and structured code. It also gave me practical experience in the implementation of design principles like Encapsulation, Single Responsibility Principle (SRP), Don’t Repeat Yourself (DRY) and Keep It Simple (KISS).
This experience taught me how to relate theory and practice by working on a Python program and applying principles to it.

What I Practiced
 Classes and Objects
I have made a class called Booking System and it contains not only the data (such as passenger name, ID number, ticket ID etc) but also the methods (such as customerinfo() and ferryservicedetails()). This made me realize how objects and classes are able to combine related functionality into a single logical unit.

 Encapsulation
The entire booking attributes (e.g. ID, ticket, total, status) are saved within the class. This makes sure that data is maintained and it is not altered by outside forces. It is also more maintainable and transparent since the only method that can update the data is the methods of the class.

 Single Responsibility Principle (SRP)
There are two methods in the class that are specialized to do one thing.
- customerinfo() - gathers the information of the user.
- ferryservicedetails() - calculates total cost
- respondrequsition() - deals with approval logic
- displaybooking_info( ) - shows final details.
The code can be read, updated and debugged more easily by assigning each method a purpose.

 DRY (Don't Repeat Yourself)
I did not repeat logic by repeating common variables, which was in this case, the global counter to generate ticket IDs. This lessens redundancy and makes the system more efficient.
KISS (Keep It Simple, Stupid)
The software is maintained to be basic and user friendly. The code has a simple flow that is easily understood and expanded. All the parts are understandable in their role without any needless complexity.
A program is an organized structure of data that a computer can execute to accomplish a task. Principles and Concepts Programming A program is a systematized arrangement of data that a computer is able to execute so as to finish a task .
This project showed the use of software design principles to be useful in the writing of structured and reusable code. Encapsulation, SRP and DRY do not duplicate data, respectively, again in the class, on single responsibility, respectively.
Even though the system is effective, I realized that it still combines business logic and input/output which I will separate in subsequent projects. It also taught me the importance of understanding principles such as Open/ Closed Principle can be used to perform extensions with ease without altering the existing code something that I would like to study more.
Difficulties and Improvement areas.
- I am at times confused as to the distinction between class variables and instance variables.
- I should have more practice on how to cope with errors in user input (e.g. typing text rather than numbers).
- I would like to know how to keep the logic and user interaction separate to make the design cleaner.

Reflection
Development of this Booking System made me understand that code merely needs to run, but it needs to be written in a clean, maintainable and extendable form. All the design choices, including the choice of using a class or organizing the methods, were informed by theory so this project will be a solid demonstration of the research-practice combination.
This may have been a small project, but it taught me valuable lessons about how to think about software design, as well as gave me the confidence to implement these principles to larger, real-world projects in the future.

#Booking system
class BookingSystem:
    #setting counter
    counter = 1 

    def __init__(self):
        # booking for instance attrributes for each
        self.form_of_id = ""
        self.id_number = ""
        self.passenger_name = ""
        self.ticket_id = 0
        self.total = 0
        self.status = "Pending" 
        self.approval_reference = ""

#customer details
    def customer_info(self):
        BookingSystem.counter += 1
        self.form_of_id = input("Form of ID (Passport, driver's license): ")
        self.id_number = input("Enter ID Number: ")
        self.passenger_name = input("Enter Passenger Name: ")
        self.ticket_id = BookingSystem.counter + 20000

#Gather ferry service details and calculate total cost
    def ferry_service_details(self):
        self.total = 0
        number_items = int(input("Enter number of services: "))
        for i in range(number_items):
            item = input("Enter service name: ")
            price = float(input(f"Enter price of {item}: "))
            # calculate the service prices to total
            self.total += price

#A booking request based on user input for approves or rejects
    def respond_requsition(self):
        # It process only  if the booking is still pending
        if self.status == "Pending": 
            choice = input(f"Approve requisition {self.id_number}? (yes or no): ").lower()
            if choice == "yes":
                self.status = "Approved"
                # It combines ID with last 3 digits
                self.approval_reference = str(self.id_number) + str(self.id_number)[-3:]
            elif choice == "no":
                self.status = "Not approved"
                self.approval_reference = "Not available"

    # This line is  for display the full booking information
    def display_booking_info(self):
        print(f"Form of ID (Passport, driver's license): {self.form_of_id}")
        print(f"ID Number: {self.id_number}")
        print(f"Passenger Name: {self.passenger_name}")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference}")

#calling all the functions
booking = BookingSystem()
booking.customer_info()
booking.ferry_service_details()
booking.respond_requsition() 
booking.display_booking_info()

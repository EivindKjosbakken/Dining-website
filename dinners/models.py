from django.db import models
from django.urls import reverse


# Create your models here.
class Dinner(models.Model):
    # Dinner model for middagsarrangement \
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False, default="")
    #time = models.TimeField(_(""), auto_now=False, auto_now_add=False)
    place = models.CharField(max_length=50, blank=False, default="")
    first_name = models.CharField(max_length=50, blank=False, default="")
    date = models.CharField(max_length=10, blank=False, default="10.02.2021")
    time = models.CharField(max_length=10, blank=False, default="16.00")
    max_guests = models.IntegerField(blank=False, default=4)
    number_of_guests = models.IntegerField(blank=False, default=0)
    available = models.IntegerField(blank=False, default=4)
    guests = models.CharField(max_length=1000, blank= True, default= "")
    allergies = models.CharField(max_length=1000, blank= True, default= "")
    category = models.CharField(max_length=50, blank=False, default="other")
    host_username = models.CharField(max_length=50, blank=False, default="")
    chat = models.CharField(max_length=10000, blank=True, default="")
    city = models.CharField(max_length=50, blank=False, default="")
    cost = models.IntegerField(blank=False, default=1)
    cost_per = models.IntegerField(default=0, blank=False)
    
    def get_absolute_url(self):
        # URL til detaljert oversikt over et arrangement, bestemt av my_id.
        return reverse("dinners:dinner-detail", kwargs={"my_id": self.id})

    def update_available(self):
        self.available = self.max_guests-self.number_of_guests

    def increment_number_of_guests(self):
        # Øker påmeldte gjester med en.
        self.number_of_guests += 1
        self.update_available()
    
    def decrement_number_of_guests(self):
        # Senker påmeldte gjester med en dersom det er noen påmeldt.
        if self.number_of_guests >= 1:
            self.number_of_guests -= 1
        self.update_available()
    
    def guests_string_to_list(self):
        # Konverterer self.guests til en liste
        return self.guests.replace(" ","").split(",")

    def guests_list_to_string(self, liste):
        # Konverterer gjestelisten til en streng. legges til i self.guest, lagres ikke.
        guest_list = ", ".join(liste)
        self.guests = guest_list
        if guest_list[:2] == ", ":
            self.guests = guest_list[2:]
        
    def user_in_guests(self, username):
        # Returnerer True dersom username er i gjest/ er påmeldt. False ellers
        guest_list = self.guests_string_to_list()
        if username in guest_list:
            return True
        else:
            return False

    def add_or_remove_guest_to_guests(self, username):
        # Dersom brukernavnet er i guests/ er påmeldt, kjører funksjonen:
        # remove_guest_from_guest_list
        # Dersom brukernavnet ikke er i guest, kjører funksjonen:
        # add_guest_to_guests
        guest_list = self.guests_string_to_list()
        if self.user_in_guests(username):
            self.remove_guest_from_guest_list(username)
        else:
            self.add_guest_to_guests(username)
        
    def add_guest_to_guests(self, username):
        # Sjekker om bruker allerede er påmeldt, er Host, eller om det er fullt. 
        # Hvis ikke blir brukeren påmeldt / lagt til i guest og number_of_guests inkrementeres.
        guest_list = self.guests_string_to_list()
        if len(guest_list) == 1 and guest_list[0] == "":
            if username in guest_list or username == self.host_username: 
                #print("brukeren er allerede påmeldt")
                pass
            else:
                guest_list.append(username)
                self.increment_number_of_guests()
        elif len(guest_list) >= self.max_guests:
            #print("Arrangementet er fullt")
            pass
        else:
            if username in guest_list or username == self.host_username:
                #print("brukeren er allerede påmeldt")
                pass
            else:
                guest_list.append(username)
                self.increment_number_of_guests()
        self.guests_list_to_string(guest_list)

    def remove_guest_from_guest_list(self, username):
        #Dersom brukeren er påmeldt, melder bruker av, decrementerer number_of_guests.
        guest_list = self.guests_string_to_list()
        if len(guest_list) >= 1:
            if username in guest_list:
                guest_list.remove(username)
                self.guests_list_to_string(guest_list)
                self.decrement_number_of_guests()

    def add_message(self, username, message):
        self.chat = self.chat + '\n' + username + ": " + message

    def get_chat(self):
        return self.chat

    def get_message_list(self):
        return self.chat.split('\n')








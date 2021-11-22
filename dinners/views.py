from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import RedirectView

from .models import Dinner
from .forms import DinnerForm
from users.models import User
import datetime
from django.contrib import messages


# Create your views here.
def dinner_create_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        first_name = request.POST['first_name']
        date = request.POST['date']
        time = request.POST['time']
        max_guests = request.POST['max_guests']
        allergies = request.POST['allergies']
        description = request.POST['description']
        category = request.POST['category']
        place = request.POST['place']
        city = request.POST['city']
        cost = request.POST['cost']
        cost_per = int(cost)/(int(max_guests)+1)


        # Sjekker om dato er frem i tid
        # Henter dato fra input, kombinerer med tid. Konverterer til datetime-objekt
        dateAndTimeStr = date + ' ' + time
        dateAndTimeToDateObj = datetime.datetime.strptime(dateAndTimeStr, "%Y-%m-%d %H:%M")

        # Henter dagens dato, kombinerer med tid. Konverterer så til dattime-objekt
        currentDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        currentDateToDateObj = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M")

        # Boolean -> True, dersom valgt dato er før dagens dato
        isDateBeforeCurrentDate = currentDateToDateObj > dateAndTimeToDateObj

        if (isDateBeforeCurrentDate):
            messages.info(request, 'Dato må være frem i tid')
        else:
            dinner = Dinner.objects.create(title=title,
                                           description=description,
                                           place=place,
                                           first_name=first_name,
                                           date=date,
                                           time=time,
                                           max_guests=max_guests,
                                           category=category,
                                           number_of_guests=0,
                                           guests="",
                                           allergies=allergies,
                                           host_username=request.user.username,
                                           available=max_guests,
                                           city = city,
                                           cost=cost,
                                           cost_per=cost_per
                                           )
            dinner.save()
            return redirect('feed')

    return render(request, 'dinners/dinner_create.html')


def dinner_edit_view(request, my_id=id):
    dinner = get_object_or_404(Dinner, id=my_id)
    context = {
        "dinner": dinner
    }

    if request.method == 'POST':
        dinner.title = request.POST['title']
        dinner.place = request.POST['place']
        dinner.first_name = request.POST['first_name']
        dinner.date = request.POST['date']
        dinner.time = request.POST['time']
        dinner.max_guests = request.POST['max_guests']
        dinner.allergies = request.POST['allergies']
        dinner.description = request.POST['description']
        dinner.category = request.POST['category']
        dinner.city = request.POST['city']
        dinner.cost = request.POST['cost']
        dinner.cost_per = int(dinner.cost)/(int(dinner.max_guests)+1)

        # Sjekker om dato er frem i tid
        # Henter dato fra input, kombinerer med tid. Konverterer til datetime-objekt
        dateAndTimeStr = dinner.date + ' ' + dinner.time
        dateAndTimeToDateObj = datetime.datetime.strptime(dateAndTimeStr, "%Y-%m-%d %H:%M")

        # Henter dagens dato, kombinerer med tid. Konverterer så til dattime-objekt
        currentDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        currentDateToDateObj = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M")

        # Boolean -> True, dersom valgt dato er før dagens dato
        isDateBeforeCurrentDate = currentDateToDateObj > dateAndTimeToDateObj

        if (isDateBeforeCurrentDate):
            messages.info(request, 'Dato må være frem i tid')
        else:
            dinner.save()
            return redirect('feed')

    return render(request, 'dinners/dinner_edit.html', context)


def dinner_delete_view(request, my_id=id):
    obj = get_object_or_404(Dinner, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('feed')
    context = {
        "dinner": obj
    }
    return render(request, "dinners/dinner_delete.html", context)


def feed_view(request):
    all_dinners = Dinner.objects.all()
    dinners = []
    users = User.objects.all()
    usernames = [user.username for user in users]
    filter = ""
    chosen_city = "Oslo"
    chosen_category = "other"
    search_word = None

    if request.method == 'POST':
        filter = request.POST['dropdown']
        try:
            chosen_city = request.POST['city']
        except:
            pass
        try:
            chosen_category = request.POST['category']
        except:
            pass
        try:
            search_word = request.POST['search']
        except:
            pass

    user = request.user

    for dinner in all_dinners:
        if filter == "available":
            if dinner.available > 0:
                dinners.append(dinner)
        elif filter == "myDinners":
            if dinner.host_username == user.username:
                dinners.append(dinner)
        elif filter == "joined":
            if dinner.user_in_guests(user.username):
                dinners.append(dinner)
        elif filter == "category":
            if dinner.category == chosen_category:
                dinners.append(dinner)
        elif filter == "city":
            if dinner.city == chosen_city:
                dinners.append(dinner)
        elif filter == "search" and search_word:
            if search_word.lower() in dinner.description.lower() or search_word.lower() in dinner.title.lower():
                dinners.append(dinner)
        else:
            dinners.append(dinner)

        host = False
        guest = False
        guests = dinner.guests_string_to_list()
        for user1 in users:
            if dinner.host_username == user1.username:
                host = True
        for guest in guests:
            if not guest in usernames:
                dinner.remove_guest_from_guest_list(guest)
                dinner.save()
        if host == False:
            dinner.delete()

    context = {
        "dinners": dinners,
        "user": user,
        "filter": filter,
        "selected_id": filter,
        "selected_city": chosen_city,
        "selected_category": chosen_category,
        "search": search_word
    }

    return render(request, "dinners/feed.html", context)


def dinner_detail_view(request, my_id):
    obj = get_object_or_404(Dinner, id=my_id)
    user = request.user
    signed_up = obj.user_in_guests(user.username)  # is the user signed_up to the event.
    owner = obj.host_username == user.username  # is the user the owner of the event.
    event_full = obj.max_guests <= obj.number_of_guests  # is the event full.
    allergies_active = True
    chat_list = obj.get_message_list()

    if obj.allergies == "":
        allergies_active = False

    context = {
        "dinner": obj,
        "user": user,
        "signed_up": signed_up,
        "owner": owner,
        "allergies_active": allergies_active,
        "event_full": event_full,
        "chat_list": chat_list
    }

    if request.method == "POST":
        message = request.POST['message']
        obj.add_message(user.username, message)
        obj.save()
        return_page = "../../dinners/" + str(my_id)
        return redirect(return_page, context)

    return render(request, "dinners/dinner_detail.html", context)


def add_guest_to_dinner_view(request, my_id):
    # hjelpemetode for å melde bruker på/av. 
    # lagrer endringer i databasen.
    # Sender brukeren tilbake til detail_view
    obj = get_object_or_404(Dinner, id=my_id)
    user = request.user
    context = {
        "dinner": obj,
        "user": user
    }
    obj.add_or_remove_guest_to_guests(user.username)
    obj.save()  # lagrer endring i databasen
    # dinner_detail_view(request, my_id)
    returnToPage = "../../dinners/" + str(my_id)
    return redirect(returnToPage, context)

from ..models import Booking
def check_availablity(room,check_in,check_out):
	avail_list = []
	list =Booking.objects.filter(room=room)
	for booking in list :

		if booking.check_in>check_out or booking.check_out<check_in:
			avail_list.append(True)
		else:
			avail_list.append(False)
	return all(avail_list)

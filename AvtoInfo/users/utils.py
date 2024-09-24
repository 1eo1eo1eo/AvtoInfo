from cars.models import Car


def select_user_cars(request):

    user = request.user
    result = Car.objects.filter(owner=user)

    return result

from petstagram.pets.models import Pet


def get_pet_by_name_and_username(pet_name, username):
    # TODO: fix when user auth
    return Pet.objects.get(name=pet_name)
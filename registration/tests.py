from django.test import TestCase
from django.core.urlresolvers import reverse

from registration.models import Player
from registration.forms import PlayerForm


def create_player(first_name, last_name, email="j@gmail.com", phone_number="1112223333",
    gender="m", skill="3", want_shirt=True, want_frisbee=True, shirt_size="s", position="oc"):

    p = Player(first_name=first_name, last_name=last_name, email=email,
        phone_number=phone_number, gender=gender, skill=skill, want_shirt=want_shirt,
        want_frisbee=want_frisbee, shirt_size=shirt_size, position=positon)
    p.save()


class FormSubmissionTests(TestCase):

    def test_unsuccesful_form_submission(self):
        response = self.client.post(reverse('registration:register'), {'first_name':''})
        self.assertFormError(response, 'form', 'first_name', 'This field is required.')

    def test_successful_form_submission(self):
        forum_data = {'first_name': 'Jon', 'last_name': 'Smith',
        'email': 'j@gmail.com', 'phone_number': 1112223333,
        'gender': 'm', 'skill': '3', 'want_shirt': True,
        'want_frisbee': True, 'shirt_size': 's', 'position': 'oc'}

        form = PlayerForm(forum_data)
        self.assertEqual(form.is_valid(), True)

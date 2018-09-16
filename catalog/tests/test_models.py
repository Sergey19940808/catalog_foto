from django.utils.timezone import now

from django.test import TestCase
from catalog.models import Foto


class FotoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Foto.objects.create(
            name='img',
            text='Text it is about',
            image='images/Снимок_экрана_от_2018-06-16_09-24-50.png',
            date_added=now()
        )

    def test_name_label(self):
        foto = Foto.objects.get(id=1)
        field_label = foto._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Имя:')

    def test_text_label(self):
        foto = Foto.objects.get(id=1)
        field_label = foto._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Описание:')

    def test_image_label(self):
        foto = Foto.objects.get(id=1)
        field_label = foto._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Фотография:')

    def test_date_added_label(self):
        foto = Foto.objects.get(id=1)
        field_label = foto._meta.get_field('date_added').verbose_name
        self.assertEquals(field_label, 'Дата публикации:')

    def test_name_max_length(self):
        foto = Foto.objects.get(id=1)
        max_length = Foto._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_name_blank(self):
        foto = Foto.objects.get(id=1)
        field_label = foto._meta.get_field('name').blank
        self.assertEquals(field_label, False)

    def test_image(self):
        foto = Foto.objects.get(id=1)
        field_label = foto._meta.get_field('image').blank
        self.assertEquals(field_label, True)

    def test_object_name_is_name(self):
        foto = Foto.objects.get(id=1)
        expected_object_name = '%s' % foto.name
        self.assertEquals(expected_object_name, str(foto))

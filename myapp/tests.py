import time

from django.contrib.auth.models import Group, User
from django.test import Client, TestCase
from django.urls import reverse


class QualityAndSupportTests(TestCase):
    """Pruebas funcionales y de rendimiento para la experiencia del usuario."""

    def setUp(self):
        self.client = Client()

        self.admin_user = User.objects.create_user(
            username='adminqa',
            email='adminqa@demo.com',
            password='Segura123!',
            is_staff=True,
            is_superuser=True,
        )

        self.medico_user = User.objects.create_user(
            username='medicoqa',
            email='medicoqa@demo.com',
            password='Segura123!',
            is_staff=True,
        )
        self.medico_group, _ = Group.objects.get_or_create(name='Medico')
        self.medico_user.groups.add(self.medico_group)

        self.enfermera_user = User.objects.create_user(
            username='enfermeraqa',
            email='enfermeraqa@demo.com',
            password='Segura123!',
            is_staff=True,
        )
        self.enfermera_group, _ = Group.objects.get_or_create(name='Enfermeria')
        self.enfermera_user.groups.add(self.enfermera_group)

        # Additional role users
        self.psicologo_user = User.objects.create_user(
            username='psicologoqa',
            email='psicologoqa@demo.com',
            password='Segura123!',
            is_staff=True,
        )
        self.psicologo_group, _ = Group.objects.get_or_create(name='Psicologo')
        self.psicologo_user.groups.add(self.psicologo_group)

        self.fisio_user = User.objects.create_user(
            username='fisioaqa',
            email='fisioaqa@demo.com',
            password='Segura123!',
            is_staff=True,
        )
        self.fisio_group, _ = Group.objects.get_or_create(name='Fisioterapia')
        self.fisio_user.groups.add(self.fisio_group)

        self.fono_user = User.objects.create_user(
            username='fonoqa',
            email='fonoqa@demo.com',
            password='Segura123!',
            is_staff=True,
        )
        self.fono_group, _ = Group.objects.get_or_create(name='Fonoaudiologia')
        self.fono_user.groups.add(self.fono_group)

    def test_home_and_login_pages_load(self):
        start = time.perf_counter()
        response_home = self.client.get(reverse('home'))
        response_login = self.client.get(reverse('login'))
        elapsed = time.perf_counter() - start

        self.assertEqual(response_home.status_code, 200)
        self.assertEqual(response_login.status_code, 200)
        self.assertLess(elapsed, 2.0)

    def test_invalid_login_returns_error_message(self):
        response = self.client.post(
            reverse('login'),
            {'usuario': 'adminqa', 'contrasena': 'incorrecta'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'El usuario o contraseña son incorrectos')

    def test_admin_login_redirects_to_administrador(self):
        start = time.perf_counter()
        response = self.client.post(
            reverse('login'),
            {'usuario': 'adminqa', 'contrasena': 'Segura123!'},
            follow=True,
        )
        elapsed = time.perf_counter() - start

        self.assertRedirects(response, reverse('administrador'), fetch_redirect_response=False)
        self.assertLess(elapsed, 2.0)

    def test_medico_and_enfermeria_roles_redirect_correctly(self):
        response_medico = self.client.post(
            reverse('login'),
            {'usuario': 'medicoqa', 'contrasena': 'Segura123!'},
            follow=True,
        )
        self.assertRedirects(response_medico, reverse('medico'), fetch_redirect_response=False)

        self.client.logout()

        response_enfermeria = self.client.post(
            reverse('login'),
            {'usuario': 'enfermeraqa', 'contrasena': 'Segura123!'},
            follow=True,
        )
        self.assertRedirects(response_enfermeria, reverse('enfermeria'), fetch_redirect_response=False)

        # Psicólogo
        self.client.logout()
        response_psico = self.client.post(
            reverse('login'),
            {'usuario': 'psicologoqa', 'contrasena': 'Segura123!'},
            follow=True,
        )
        self.assertRedirects(response_psico, reverse('psicologo'), fetch_redirect_response=False)

        # Fisioterapia
        self.client.logout()
        response_fisio = self.client.post(
            reverse('login'),
            {'usuario': 'fisioaqa', 'contrasena': 'Segura123!'},
            follow=True,
        )
        self.assertRedirects(response_fisio, reverse('fisioterapia'), fetch_redirect_response=False)

        # Fonoaudiologia
        self.client.logout()
        response_fono = self.client.post(
            reverse('login'),
            {'usuario': 'fonoqa', 'contrasena': 'Segura123!'},
            follow=True,
        )
        self.assertRedirects(response_fono, reverse('fonoaudiologia'), fetch_redirect_response=False)

    def test_protected_routes_require_session(self):
        protected_urls = [
            reverse('administrador'),
            reverse('medico'),
            reverse('enfermeria'),
            reverse('psicologo'),
            reverse('fisioterapia'),
            reverse('fonoaudiologia'),
        ]

        login_url = reverse('login')
        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertTrue(response.url.startswith(login_url))
            self.assertIn('next=', response.url)

    def test_performance_of_login_flow_is_under_threshold(self):
        timings = []

        for _ in range(3):
            start = time.perf_counter()
            self.client.post(
                reverse('login'),
                {'usuario': 'adminqa', 'contrasena': 'Segura123!'},
                follow=True,
            )
            timings.append(time.perf_counter() - start)

        self.assertLess(max(timings), 2.0)
        self.assertLess(sum(timings) / len(timings), 1.5)

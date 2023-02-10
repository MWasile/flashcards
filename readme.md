# Azeno

## Algorytm postępowania:

1. Czy potrzebujemy django app?
   1. `python manage.py startapp <app_name>`
   2. Dodaj do install apps -> settings.py
2. Analiza czy potrzebujemy dane?
   1. Narysuj ERD diagram na kartce
   2. Implementacja w models.py
   3. `python manage.py makemigrations <app_name>`
   4. `python manage.py migrate <app_name>`
   5. Unit tests -> pytest
3. Czy potrzebujemy zarządzać tym zasobem z CMS(django admin)?
   1. Rejestrujemy modele w admin.py
4. Czy wystawiamy dane w widoku?
   1. Tworzymy plik serializers.py (format danych)
   2. Unit tests
5. Tworzymy widoki (logike)
   1. Dobieramy odpowiednią klase do obsługi widoku [wyszukiwarka widoków](https://www.cdrf.co)
   2. Widok musi zwracać response lub redirect
   3. Logika uprawnień permission.py
   4. Unit tests
6. Tworzymy lokalny router
   1. W pliku urls.py tworzymy urlpatterns lub router
   2. Podpinamy lokalne urls do globalnych urls -> config/urls.py
   3. Unit tests
7. Postman i stworzenie kolekcji
   1. Wyeksportowanie kolekcji do repozytorium
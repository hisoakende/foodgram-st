import json

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Load ingredients data from JSON file into database'

    def handle(self, *args, **options):
        try:
            with open('data/ingredients.json', 'r', encoding='utf-8') as f:
                ingredients = json.load(f)
                created_count = 0
                
                for item in ingredients:
                    _, created = Ingredient.objects.get_or_create(
                        name=item['name'],
                        measurement_unit=item['measurement_unit']
                    )
                    if created:
                        created_count += 1
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully loaded {created_count} ingredients'
                    )
                )
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR('File data/ingredients.json not found')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error loading ingredients: {str(e)}')
            )

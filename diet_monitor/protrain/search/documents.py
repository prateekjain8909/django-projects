from django_elasticsearch_dsl import Document, Index
from home.models import Nutrition

nutrition = Index('nutrition')

@nutrition.doc_type
class NutritionDocument(Document):
      class Django:
            model = Nutrition

            fields = ['food'
,'servings'
,'ingredients'
,'procedure'
,'calories'
,'total_fat'
,'saturated_fat'
,'polyunsaturated_fat'
,'monounsaturated_fat'
,'cholesterol'
,'sodium'
,'potassium'
,'total_carbohydrate'
,'dietary_fiber'
,'sugars'
,'protein'
,'vitamin_a'
,'vitamin_b12'
,'vitamin_b6'
,'vitamin_c'
,'vitamin_d'
,'vitamin_e'
,'calcium'
,'copper'
,'folate'
,'iron'
,'magnesium'
,'manganese'
,'niacin'
,'pantothenic_acid'
,'phosphorus'
,'riboflavin'
,'selenium'
,'thiamin'
,'zinc']
class ChaiUtils:
   @staticmethod
   def clean_ingrideints(text):
        return [item for item in text.split(",")]



raw = " water ,  milk  ginger ,  honey"    

cleaned = ChaiUtils.clean_ingrideints(raw)
print(cleaned)
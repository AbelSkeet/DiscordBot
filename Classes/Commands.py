from datetime import datetime
import random

timeNow = datetime.now()

class Commands:

   def reflection(self):
      reflections = ['''It's already another day and you're still having the same problem? Are you discouraged, tired thinking about dropping everything and selling coconuts on the beach?
Remember the path you took to get here and how many problems you've overcome..
The problem you're experiencing is just one more step, and it's up to you to overcome it or avoid it.
Force!! :muscle::wink: ''',
'''The thinker Guimarães Rosa has a maxim about the difficulties of life that it is interesting to share: "Living is very dangerous... Because learning to live is what living really is... A dangerous crossing, but it is the life. Sertão that raises and lowers... The most difficult thing is not a good being and honest behavior, even difficult, it is a defined knowledge of what you want, and having the power to go to the tail of the word."
We have several meanings to draw from this maxim, but the end is what matters. For you who feel lost at a given moment while programming, understand that sometimes we need to take a few steps back, and see the field or block as a whole. Remember thinking hurts, but what hurts the most is knowing we are afraid of not thinking. So release this command and let's code''']
        return random.choice(reflections)
      
      def morning(self):
        return '''Good morning'''
    
    def afternoon(self):
        return '''Good afternoon'''
    
    def night(self):
        return '''Good night'''

    def salutation(self):
        if timeNow.hour < 12 and timeNow.hour >= 6:
            return self.morning()
        elif timeNow.hour >= 12 and timeNow.hour < 19:
            return self.afternoon()
        else:
            return self.night()
          
          def commands(self):
        return {
            '<3rafa': 'oh disus',
            '<3matan': 'Ask me what you want, and I'll give you the answer',
            '<3arthur': 'I'm going to eat glass and cry in the shower after this one... :smiling_face_with_tear:',
            '<3ander': 'Good cxr, ce deserves it',
          '<3kyle': f'And let's go to the off topic , this chat was totally distorted',
            '<3water': '--> Drink Water <--',
            '<3joelzin': 'https://tenor.com/view/tohru-dragonmaid-anime-gif-9656401',
            '<3kaway': 'Life is a blank sheet of paper, and I don't have a pen',
            '<3gentil': 'Kindness begets kindness',
        }
         
            

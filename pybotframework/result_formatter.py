HH_IMG = "https://www.whatsuplife.in/kolkata/blog/wp-content/uploads/2016/05/happy-hour-offers-in-kolkata.jpg"
class ResultFormatter:
    def process_results(self,result):
        print ("Calling process_results")
        if result['best_intent'] == 'FindPub':
            intent_str = "Pubs"
            if result['best_entity'] and result['best_entity'] != 'None':
                return 'You are looking for {} in {} area. Am I correct?'.format(intent_str, result['best_entity'])
            else:
                return 'You are looking for {}. Which city or area?'.format(intent_str)
        elif result['best_intent'] == 'HappyHours':
            if result['best_entity'] and result['best_entity'] != 'None':
                return 'You are looking for {}, {}'.format(result['best_intent'], result['best_entity'])
            else:
                return 'You are looking for {}. Let me know the date.'.format(result['best_intent'])
        elif result['best_intent'] == 'WishBot':
            if result['best_entity'] and result['best_entity'] != 'None':
                return '![image]({})'.format(HH_IMG)+\
                       '<br>Hello {}, Welcome!<br>Alcohol consumption is injurious to health.'.format(result['best_entity'])
            else:
                return '![image]({})'.format(HH_IMG) +\
                        '<br>Hello, Welcome!<br>Alcohol consumption is injurious to health.'
        else:
            #return self.getAdaptiveCard()
            return "I am still a novice. Ask me more questions."

    def getAdaptiveCard(self):
        return '{"type":"AdaptiveCard","version":"1.0","body": ['+ \
               '{' + \
               '"type": "Image",' + \
               '"url": "{}"' + \
               '},' + \
               '{' + \
               '"type": "TextBlock",'+\
               '"text": "I am still a novice. Ask me more questions."'+\
            '}'+\
        ']'+\
        '}}'.format(HH_IMG)
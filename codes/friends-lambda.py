# -*- coding: utf-8 -*-
""" Trivia quiz.. """
from __future__ import print_function
import math
import string
import random

GAME_STATE_TRIVIA = "TRIVIA"
GAME_STATE_START = "START"
GAME_STATE_HELP = "HELP"

GAME_QUESTIONS_KEY = "gameQuestions"
ANSWERTEXT_KEY = "correctAnswerText"
SCORE = "score"
CORRECTANSWERINDEX = "correctAnswerIndex"
SPEECHOUTPUT_KEY = "speechOutput"
REPROMPT_KEY = "repromptText"
CURRENTQUESTION_KEY = "currentQuestionIndex"
STATE_KEY = "state"
LOCALE = "locale"

COUNTER = 0
QUIZSCORE = 0
GAME_LENGTH = 10
ANSWER_COUNT = 3

game_state = GAME_STATE_START


languageSupport = {  
    "en-IN": {
        "translation": {
            "QUESTIONS": [
        {
          "What’s Joey’s penguin’s name?": 
          [ "Huggsy","Snowflake","Waddle","scorpo" ]
        },
        
        {
            "Where do they all travel to when Ross is a key note speaker?": 
            [ "barbados","miami","sydney","singapore" ]
        },
        
        {
            "What is Joey’s agent’s name?": 
            [ "estelle","janine","angela","mary" ]
        },
		
		{
            "Into how many categories does monica classifies her towels?": 
            [ "eleven","seven","nine","thirteen" ]
        },
		
        {
            "What game did Chandler make up to give Joey money?": 
            [ "cups","bowls","bamboozled","fuzzie" ]
        },
        
        {
            "What does Rachel say is Chandler’s job?": 
            [ "transposter","transporter","transplanter","trader" ]
        },
        
        {
            "Who did Rachel almost marry?": 
            ["barry","paolo","richard","joey" ]
        },
        
        {
            "What is Joey's catchphrase?": 
            [   "how you doing","hey whats up","hey man","hello brother" ]
        },
        
        {
            "Where do they all live?": 
            [   "New york",	"chicago","westchester","paris"]
        },
        
        {
            "Where do they hang out all the time?": 
            [   "central perk","nyc perks","star bucks","ny central"]
        },
        
        {
            "Whose mom committed suicide?":
            [ "phoebe", "joey", "chandler", "monica"]
        },
        
        {
            "what is monica's occupation?":
            [ "chef", "eye doctor", "fashion designer", "data scientist"]
        },
        
        {
            "What show do Joey and Chandler love to watch?":
            [ "Baywatch", "wheel of fortune", "days of our lives", "star wars"]
        },
        
		{
            "Where are Ross, Rachel, and Monica from?": 
            [ "long island","connecticut","westchester","rio di janero" ]
        },
        
        {
            "What is the building superintendant's name?": 
            [ "treeger","jack","james","gunther" ]
        },
        
		{
            "What is the neighbor's name that lives below Rachel and Monica?": 
            [ "Mr heckles","Mr tribbiani","Mr trevor","Mr salvatore" ]
        },
        
        {
            "What does Ross buy for Rachel's birthday?": 
            [ "a brooch","a necklace","a dress","a sweater" ]
        },
        
        {
            "Who does Phoebe end up with?": 
            [   "mike","mark","david","duncan" ]
        },
        
        {
            "Whose father has a show in Las Vegas?": 
            [ "chandler's","joey's","gunther's","janice's" ]
        },
        
        {
            "Which FRIENDS are siblings?": 
            [ "ross and monica","rachel and monica","joey and phoebe","monica and joey" ]
        },

        {
            "Where is Rachel's first job after moving to the city?": 
            [ "central perk","raplh lauren","starbucks","h&m" ]
        },
        
        {
            "Whose laughter is most weird?": 
            [ "janice","angela","rachel","bob" ]
        },
        
        {
            "Who wasn't joey's girfriend?": 
            [ "monica","rachel","charlie","kathy" ]
        },
        
        {
            "What is the name of Chandler's crazy roommate?": 
            [ "eddie","marcus","matthew","damon" ]
        },
        
        {
            "What did Rachel and Chandler eat off of the floor?": 
            [   "cheese cake","chocolate cake","pizza","noodles" ]
        },
        
        {
            "What does Phoebe get a tattoo of?": 
            [   "the whole world","a cat","m for mike","a freckle" ]
        },
        
        {
            "What does Mike change his name to?": 
            [   "crap bag","shit head","crappy head","freak head" ]
        },
        
        {
            "Who gave birth to Chandler and Monica's twins?": 
            [   "erika","janine","ursula","monica" ]
        }
            
    		],
            "GAME_NAME" : "My Friends Quiz", 
            "HELP_MESSAGE": "I will ask you {0} multiple choice questions. Respond with the number of the answer. " +
            "For example, say one, two or  three. To start a new game at any time, say, start game. ",
            "REPEAT_QUESTION_MESSAGE": "To repeat the last question, say, repeat. ",
            "ASK_MESSAGE_START": " What would you like to do? ",
            "HELP_REPROMPT": "To give an answer to a question, respond with the number of the answer. ",
            "STOP_MESSAGE": "Ok, we'll play another time. Goodbye!",
            "CANCEL_MESSAGE": "Ok, let's play again soon.",
            "NO_MESSAGE": "Ok, we'll play another time. Goodbye!",
            "TRIVIA_UNHANDLED": "Try saying a number between 1 and %s",
            "HELP_UNHANDLED": "Say yes to continue, or no to end the game.",
            "START_UNHANDLED": "Say start to start a new game.",
            "NEW_GAME_MESSAGE": "Welcome to {0}. ",
            "WELCOME_MESSAGE": "I will ask you {0} questions, try to get as many right as you can. Just say the number of the answer. Let's begin. ",
            "ANSWER_CORRECT_MESSAGE": "correct. ",
            "ANSWER_WRONG_MESSAGE": "wrong. ",
            "CORRECT_ANSWER_MESSAGE": "The correct answer is {0}: {1}. ",
            "ANSWER_IS_MESSAGE": "That answer is ",
            "TELL_QUESTION_MESSAGE": "Question {0}. {1} ",
            "GAME_OVER_MESSAGE":"You got {0} out of {1} questions correct.",
            "SCORE_IS_MESSAGE": "Your score is {0}. ",
            "GAME_MSG_GOOD":" Great. You're Indeed a True Friends Fan! ",
            "GAME_MSG_BAD":" Never Mind Buddy! We will play some other time. ",
            "FINAL_MSG":"Thank you for playing!"
     }, 
    },
	}

# --------------- entry point -----------------

def lambda_handler(event, context):
    """ App entry point  """
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended()

# --------------- response handlers -----------------

def on_intent(request, session):
    """ called on Intent """
    intent = request['intent']
    intent_name = request['intent']['name']
    #print("on_intent " +intent_name)
    #print(request)

    getstate(session)
    locale = getlocale(request, session)

    if get_game_state() == GAME_STATE_TRIVIA:        
        return rungame(request, session, locale, intent, session)
        
    return help_handler(False, request, locale, session)

def rungame(request, newgame, locale, intent, session):
    """ process the game questions and user response """
    intent_name = request['intent']['name']
    resource = getresource(locale)

    if 'dialogState' in request:
        if request['dialogState'] == "STARTED" or request['dialogState'] == "IN_PROGRESS":
            attributes = {"locale":locale}
            return dialog_response(attributes, False)
    
    if intent_name == "AMAZON.StartOverIntent":
        return start_game(request, True, locale)
    elif intent_name == "AMAZON.RepeatIntent":
        reprompt = session['attributes'][REPROMPT_KEY]
        return rebuild_response(request, locale, session, reprompt )
    elif intent_name == "AMAZON.CancelIntent":
        return cancel_response(locale)
    elif intent_name == "AMAZON.StopIntent":
        return cancel_response(locale)
    elif intent_name == "AMAZON.HelpIntent":
        return dohelp(request, False, locale)
    elif intent_name == "AnswerIntent":
        return processuserguess(False, request, session, intent, locale)
    elif intent_name == "DontKnowIntent":
        return processuserguess(True, request, session, intent, locale) 
    return dohelp(request, False, locale)

def processuserguess(usergaveup, request, session, intent, locale):
    resource = getresource(locale)
    speech_output = ""

    game_questions = session['attributes'][GAME_QUESTIONS_KEY]
    correct_answer_index_previous_question = int(session['attributes'][CORRECTANSWERINDEX])
    current_score = int(session['attributes'][SCORE])
    current_question_index_previous_question = int(session['attributes'][CURRENTQUESTION_KEY])
    correct_answer = session['attributes'][ANSWERTEXT_KEY]

    if match_guess_with_answer(intent, correct_answer_index_previous_question):    
        current_score += 1
        speech_output = resource["ANSWER_CORRECT_MESSAGE"]
      
    else:
        if usergaveup == False:            
            speech_output = resource["ANSWER_WRONG_MESSAGE"]
                          
        speech_output +=" "+ resource["CORRECT_ANSWER_MESSAGE"].format(correct_answer_index_previous_question, correct_answer)

    if current_question_index_previous_question >= (GAME_LENGTH - 1):
        speech_message = ""
        if usergaveup == False:
            speech_message = resource["ANSWER_IS_MESSAGE"]
        
        speech_message +=" "+ speech_output +" "+ resource["GAME_OVER_MESSAGE"].format(str(current_score), str(GAME_LENGTH))
        #return response("", response_plain_text(speech_message, True))
        if current_score > (GAME_LENGTH / 2):
            game_msg= resource["GAME_MSG_GOOD"]
            return response("", GAME_OVER_GOOD(speech_message, game_msg, resource["FINAL_MSG"], True))
        else:
            game_msg=  resource["GAME_MSG_BAD"]
            return response("", GAME_OVER_BAD(speech_message, game_msg, resource["FINAL_MSG"], True))
        
    current_question_index_next_question = current_question_index_previous_question + 1    
    correct_answer_index_next_question = random.randrange(0, ANSWER_COUNT -1 , 1)    
        
    new_questions = game_questions[current_question_index_next_question]
            
    round_answers = populate_round_answers(new_questions, 
                    current_question_index_next_question, correct_answer_index_next_question)
         
    correct_answer_text_next_question = round_answers[correct_answer_index_next_question]    
          
    reprompt = get_answers_text(game_questions[current_question_index_next_question], round_answers,
               current_question_index_next_question, locale)
            
    if usergaveup == False:
        speech_message  = resource["ANSWER_IS_MESSAGE"]
    else:
        speech_message = ""   
    speech_message +=" "+ speech_output + " " + resource["SCORE_IS_MESSAGE"].format(str(current_score)) + " " + reprompt

    correct_answer_index_next_question += 1    
    set_game_state(GAME_STATE_TRIVIA)

    attributes = { SPEECHOUTPUT_KEY: reprompt,
                      REPROMPT_KEY: reprompt,
                      CURRENTQUESTION_KEY: str(current_question_index_next_question),
                      CORRECTANSWERINDEX: str(correct_answer_index_next_question),
                      GAME_QUESTIONS_KEY: game_questions,
                      SCORE: str(current_score),
                      ANSWERTEXT_KEY: correct_answer_text_next_question,
                      STATE_KEY: get_game_state(),
                      LOCALE: locale
                 }
    
    return response(attributes, speech_response_prompt_card(resource["GAME_NAME"],speech_message, reprompt, False))


def match_guess_with_answer(intent, correctAnswerIndex):
    """ check if answer matches """  
    if 'slots' in intent:
        slots = intent['slots']
        for key, val in slots.items():            
            if val.get('value'):
                if (val.get('value')).isdigit():
                    lval = int(val['value'].lower())
                    if lval == correctAnswerIndex and lval <= ANSWER_COUNT and lval > 0:
                        #print("user answered " + str(lval) + " correct answer number is: " + str(correctAnswerIndex))
                        return True
    return False

def cancel_response(locale):
    resource = getresource(locale)
    speechmessage = resource["CANCEL_MESSAGE"] 
    return response("", response_plain_text(speechmessage, True))

def rebuild_response(request, locale, session, speech_message):
    speech_output = session['attributes'][SPEECHOUTPUT_KEY]
    reprompt = session['attributes'][REPROMPT_KEY]
    game_questions = session['attributes'][GAME_QUESTIONS_KEY]
    correct_answer_index = session['attributes'][CORRECTANSWERINDEX]
    current_score = session['attributes'][SCORE]
    current_question_index = session['attributes'][CURRENTQUESTION_KEY]
    correct_answer_text = session['attributes'][ANSWERTEXT_KEY]
    set_game_state(GAME_STATE_TRIVIA)
    attributes = { SPEECHOUTPUT_KEY: reprompt,
                  REPROMPT_KEY: reprompt,
                  CURRENTQUESTION_KEY: current_question_index,
                  CORRECTANSWERINDEX: correct_answer_index,
                  GAME_QUESTIONS_KEY: game_questions,
                  SCORE: current_score,
                  ANSWERTEXT_KEY: correct_answer_text,
                  STATE_KEY: get_game_state(),
                  LOCALE: locale
                 }

    return response(attributes, response_plain_text_promt(speech_message, speech_message, False))

def dohelp(request, newgame, locale):
    """ display help for selected locale """
    
    resource = getresource(locale)
    askmessage =  resource["REPEAT_QUESTION_MESSAGE"] +" " +resource["ASK_MESSAGE_START"] 
    speech_message = resource["HELP_MESSAGE"].format(resource["GAME_NAME"]) +" " + askmessage

    set_game_state(GAME_STATE_HELP)
    attributes = {
                 STATE_KEY: get_game_state()                  
                 }
    return response(attributes, response_plain_text_promt(speech_message, speech_message, False))

def help_handler(newgame, request, locale, session):
    """ help handler """
    intent_name = request['intent']['name']
    resource = getresource(locale)
    if newgame == True:
        askmessage = resource["ASK_MESSAGE_START"] 
    else:
        askmessage = resource["REPEAT_QUESTION_MESSAGE"] + resource["ASK_MESSAGE_START"]
     
    if intent_name == "AMAZON.StartOverIntent":
        print("help state: startover intent")
        set_game_state(GAME_STATE_START)
        return start_game(request, False, locale)

    elif intent_name == "AMAZON.RepeatIntent":
        print("help state: repeat intent")
        if SPEECHOUTPUT_KEY in session['attributes']:
            if not( session['attributes'][SPEECHOUTPUT_KEY] is None) and not(session['attributes'][REPROMPT_KEY] is None):
                return dohelp(False, request, session, locale)
        return dohelp(request, True, locale)

    elif intent_name == "AMAZON.CancelIntent":
        return cancel_response(locale)

    elif intent_name == "AMAZON.StopIntent":
        return cancel_response(locale)

    elif intent_name == "AMAZON.HelpIntent":
        if SPEECHOUTPUT_KEY in session['attributes']:
            if not( session['attributes'][SPEECHOUTPUT_KEY] is None) and not(session['attributes'][REPROMPT_KEY] is None):
                return dohelp(request, False, locale)
        return dohelp(request, True, locale)    
     
    speechmessage = resource["HELP_MESSAGE"].format(GAME_LENGTH) +" "+ askmessage
    set_game_state(GAME_STATE_HELP)    
    attributes = {
                  STATE_KEY: get_game_state()                  
                 }
    return response(attributes, response_plain_text(speechmessage, False))    

def on_launch(request, session):
    """ start """
    #print("launch")
    set_game_state(GAME_STATE_TRIVIA)
    return start_game(request, True, getlocale(request, session))

def start_game(request, newgame, locale):
    """ start a new game """
    
    resource = getresource(locale)

    speechOutput = "" 
    if newgame == True:
        speechOutput = resource["NEW_GAME_MESSAGE"].format(resource["GAME_NAME"]) +" "+ resource["WELCOME_MESSAGE"].format(str(GAME_LENGTH)) 
        
    current_question_index = 0
    
    questions = get_question_list(locale)
    correct_answer_index= random.randrange(0, ANSWER_COUNT , 1)
     
    round_answers = populate_round_answers(questions[current_question_index], 
        current_question_index, correct_answer_index)
    correct_answer_text = round_answers[correct_answer_index]
    
    reprompt = get_answers_text(questions[current_question_index], round_answers, current_question_index, locale)
    speech_message = speechOutput +" "+ reprompt
    
    correct_answer_index += 1    
    set_game_state(GAME_STATE_TRIVIA)
    
    attributes = { SPEECHOUTPUT_KEY: speech_message,
                  REPROMPT_KEY: reprompt,
                  CURRENTQUESTION_KEY: str(current_question_index),
                  CORRECTANSWERINDEX: str(correct_answer_index),
                  GAME_QUESTIONS_KEY: questions,
                  SCORE: "0",
                  ANSWERTEXT_KEY: correct_answer_text,
                  STATE_KEY: get_game_state(),
                  LOCALE: locale
                 }

    return response(attributes, welcome_msg(resource["GAME_NAME"],speech_message, reprompt, False))  

def populate_round_answers(question, correct_question_index, correct_answer_index):
    """ get answers for a given question, place correct answer at the spot marked by the/
        correctAnswerIndex. 
    """
    for theanswers in question.values():        
        tmp_answer = theanswers[0]        
        theanswers.remove(tmp_answer)
        theanswers_randomised = random.sample(theanswers, len(theanswers) )
        theanswers_randomised.insert(correct_answer_index, tmp_answer)
        theanswers.insert(correct_question_index, tmp_answer)
        return theanswers_randomised

def getstate(session):
    if STATE_KEY in session['attributes']:
        set_game_state(session['attributes'][STATE_KEY])
    else:
        set_game_state(GAME_STATE_START)

def get_answers_text(question, reorderedquestion, current_question_index, locale):
    """ get text for the answer """
    number = current_question_index + 1
    resource = getresource(locale)
    k = list(question.keys())
    questiontext = k[0]
    outtext = resource["TELL_QUESTION_MESSAGE"].format(str(number), questiontext) + " "
    
    index = 0
    for qtext in reorderedquestion:
        outtext += str(index + 1) + ". " + qtext +". "
        index += 1        
        if index == ANSWER_COUNT:
            break

    return outtext[:-1]

def get_game_state():
    """ """
    global game_state
    return game_state

def set_game_state(state):
    """ """
    global game_state
    game_state = state

def getresource(locale):
    """ """
    return languageSupport[locale]["translation"]

def getlocale(request,session):
    locale = request['locale']
    if locale == "":
        attributes = session['attributes']
        attributes['locale']

    if locale == "":
        locale = "en-US" 
    
    return locale

def on_session_ended():
    """ called on session end  """
    #print(on_session_ended)


def get_question_list(locale):
    """ """
    global GAME_LENGTH
    questions  = []
    res = getresource(locale)
    ilen = len(res["QUESTIONS"])
    questionsample = random.sample(range(0, ilen), GAME_LENGTH)
    for index in questionsample:
        questions.append(res["QUESTIONS"][index])
    return questions
 
 # --------------- speech response handlers -----------------

def response_plain_text(output, endsession):
    """ create a simple json plain text response  """
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output+"</speak>"
        },     
        'shouldEndSession': endsession
    }

def response_plain_text_promt(output, reprompt_text, endsession):
    """ create a simple json plain text response  """
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
            'type': 'PlainText',
            'text': reprompt_text
            }
        },
        'shouldEndSession': endsession
    }

def response_ssml_text(output, endsession):
    """ create a simple json plain text response  """
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
        },
        'shouldEndSession': endsession
    }

def response_ssml_text_card_image(title, output, endsession, cardtext, smallimage, largeimage):
    """ create a simple json plain text response  """
    return {
        'card': {
            'type': 'Standard',
            'title': title,
            'text': cardtext,
            'image':{
                'smallimageurl':smallimage,
                'largeimageurl':largeimage
            },
        },
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
        },
        'shouldEndSession': endsession
    }
def GAME_OVER_GOOD(output,game_msg1,final_msg, endsession):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>"+output+"<amazon:emotion name='excited' intensity='high'>" +" "+ game_msg1 +" "+"</amazon:emotion>"+final_msg+"<audio src='soundbank://soundlibrary/alarms/chimes_and_bells/chimes_bells_04'/></speak>"
        },
        'shouldEndSession': endsession
    }

def GAME_OVER_BAD(output,game_msg1,final_msg, endsession):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>"+output+"<amazon:emotion name='disappointed' intensity='medium'>" +" "+ game_msg1 +" "+"</amazon:emotion>"+final_msg+"<audio src='soundbank://soundlibrary/alarms/chimes_and_bells/chimes_bells_04'/></speak>"
        },
        'shouldEndSession': endsession
    }

def response_ssml_text_card(title, output, endsession):
    """ create a simple json plain text response  """
    return {
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
        },
        'shouldEndSession': endsession
    }

def speech_response_prompt_card(title, output, reprompt_text, endsession):
    """  create a simple json response with a card  """
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>"+output+"</speak>"
        },
         'card': {
            'type': 'Simple',
            'title': title,
            'content': reprompt_text
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': endsession
    }



def welcome_msg(title, output, reprompt_text, endsession):
    """  create a simple json response with a card  """
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak><audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_bridge_01'/><amazon:emotion name='excited' intensity='low'>"+output+"</amazon:emotion></speak>"
            #'ssml': "<speak><amazon:emotion name='excited' intensity='low'>"+output+"</amazon:emotion></speak>"
            
        },
         'card': {
            'type': 'Simple',
            'title': title,
            'content': reprompt_text
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': endsession
    }



def response_ssml_text_reprompt(title, output, endsession, repromt_text):
    """  create a simple json response with a card  """
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': "<speak>" +repromt_text +"</speak>"
            }
        },
        'shouldEndSession': endsession
    }

def dialog_response(attributes, endsession):
    """  create a simple json response with card """
    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response':{
            'directives': [
                {
                    'type': 'Dialog.Delegate'
                }
            ],
            'shouldEndSession': endsession
        }
    }

def response(attributes, speech_response):
    """ create a simple json response """
    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': speech_response
    }

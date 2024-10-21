class SurveyLanguage:
    surveyls_survey_id = -1
    surveyls_language = ""
    surveyls_title = ""
    surveyls_description = ""
    surveyls_welcometext = ""
    surveyls_endtext = ""
    surveyls_url = ""
    surveyls_urldescription = ""
    surveyls_email_invite_subj = ""
    surveyls_email_invite = ""
    surveyls_email_remind_subj = ""
    surveyls_email_remind = ""
    surveyls_email_register_subj = ""
    surveyls_email_register = ""
    surveyls_email_confirm_subj = ""
    surveyls_email_confirm = ""
    surveyls_dateformat = 1
    surveyls_alias = ""
    email_admin_notification_subj = ""
    email_admin_notification = ""
    email_admin_responses_subj = ""
    email_admin_responses = ""
    surveyls_numberformat = 0

    def __init__( self, surveyls_survey_id, surveyls_language, surveyls_title, surveyls_description, 
        surveyls_welcometext=None, surveyls_endtext=None, surveyls_alias=None):

        self.surveyls_survey_id = surveyls_survey_id
        self.surveyls_language = surveyls_language
        self.surveyls_title = surveyls_title
        self.surveyls_description = surveyls_description
        self.surveyls_welcometext = surveyls_welcometext
        self.surveyls_endtext = surveyls_endtext
        self.surveyls_alias = surveyls_alias

    def __str__( self ):
        attributes = { **self.__class__.__dict__, **vars(self) }
        result = ""
        for attr, value in attributes.items():
            if not attr.startswith("__") and not callable(value):
                result += f"\t\tSL\t\t{attr}\t\t{value}\t\t{self.surveyls_language}\n"
            
        return result
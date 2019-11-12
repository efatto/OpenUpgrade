# coding: utf-8
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(cr, version):
    openupgrade.rename_tables(cr, [('survey', 'survey_survey')])
    openupgrade.rename_models(cr, [('survey', 'survey.survey')])
    openupgrade.rename_tables(cr, [('survey_request', 'survey_user_input')])
    openupgrade.rename_models(cr, [('survey.request', 'survey.user_input')])
    openupgrade.rename_tables(cr, [('survey_type', 'survey_type')])
    openupgrade.rename_models(cr, [('survey.type', 'survey.type')])
    openupgrade.rename_tables(cr, [('survey_response_line', 'survey_user_input_line')])
    openupgrade.rename_models(cr, [('survey.response.line', 'survey.user_input_line')])

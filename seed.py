import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

from project.models import Question, KnowledgeArea

ls = {
    11: {
        "name":["How good is your organization's portfolio process?",
                "What is the level of improvement in your organization's portfolio optimization process?",
                "What is the level of improvement in your organization's Authorize portfolio process??",
                "What does your organization's oversight process look like? ",
                "What is the level of improvement in your organization's portfolio management planning process?"
            ],
        "description":["Define Portfolio Process standards are established.",
                       "Optimize Portfolio Process standards are established.",
                       "Authorize Portfolio Process standards are established.",
                       "Provide Portfolio Oversight Process standards that are established.",
                       "Develop Portfolio Management Plan Process standards are established.",]
    },
    12: {
        "name":["How improved is your portfolio communication management plan development process?",
                "What is the level of improvement in your organization's portfolio information management process?"],
        "description":["Develop Portfolio Communication Management Plan Process standards are established.",
                       "Manage Portfolio Information Process standards are established."]
    },
    13: {
       "name":["How good is your organization's 'Strategic Change Management process?",
               "What is the level of improvement in your organization's 'Strategic Portfolio Planning process?",
               "How has your organization's portfolio charter development process improved?",
               "What is the level of improvement in the process of defining your portfolio roadmap?"],
       "description":["Manage Strategic Change Process standards are established",
                      "Develop Portfolio Strategic Plan Process standards are established",
                      "Develop Portfolio Charter Process standards are established",
                      "Define Portfolio Roadmap Process standards are established"]
    },
    14: {
        "name":["What does your organization's process for developing a portfolio risk management plan look like?",
                "What does your organization's Portfolio Risk Management process look like?"],
        "description":["Develop Portfolio Risk Management Plan Process standards are established.",
                       "Manage Portfolio Risks Process standards are established."]
    },
    15: {
        "name":["What is the level of improvement in your organization's portfolio performance management planning process?",
                "What is the level of improvement in your organization's supply and demand management process?",
                "At what level is the Portfolio Value Management process in your organization?"],
        "description":["Develop Portfolio Performance Management Plan Process standards are established.",
                       "Manage Supply and Demand Process standards are established.",
                       "Manage Portfolio Value Process standards are established."]
    }
}
ka = [11, 12, 13, 14, 15]

combined = []


for key, value in ls.items():
    dsl = ["standardize", "measure", "control", "improve"]
    # Iterate over each question and description in the current key-value pair
    for j in range(len(value["name"])):
        # For each question and description, create a dictionary with different stages and append it to the combined list
        for i in dsl:
                knowledge_area_instance= KnowledgeArea.objects.get(pk=key)
                Question.objects.create(
                    name = value["name"][j],
                    description = value["description"][j],
                    knowledge_area=knowledge_area_instance,
                    domain="portfolio",
                    stage=i,
                )

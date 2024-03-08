ls = {
    1: {
        "name": ["'Program Initiation' process in your program/ department?",
                 "'Program Management Plan Development' process in your program/ department?",
                 "'Program Infrastructure Development' process in your program/ department?",
                 "'Program Performance Monitoring and Control' process in your program/ department?",
                 "'Program Execution Management' in your program/ department?",
                 "'Program Transition and Benefits Sustainment' process in your program/ department?",
                 "'Program Closure' process in your program/ department?", ],
        "description": ["Program Initiation Process standards are established.",
                        "Program Management Plan Development Process standards are established.",
                        "Program Infrastructure Development Process standards are established.",
                        "Program Performance Monitoring and Control Process standards are established.",
                        "Program Execution Management Process standards are established.",
                        "The stability of the process. Program Transition and Benefits Sustainment Process standards are established.",
                        "Program Closure Process standards are established."]
    },
    2: {
        "name": ["'Program Scope Planning' process in your program/ department?",
                 "'Program Scope Control' process in your program/ department?", ],
        "description": ["Program Scope Planning Process standards are established.",
                        "Program Scope Control Process standards are established."]
    },
    3: {
        "name": ["'Program Schedule Planning' process in your program/ department?",
                 "'Program Schedule Control' process in your program/ department?", ],
        "description": ["Program Schedule Planning Process standards are established.",
                        "Program Schedule Control Process standards are established."]
    },
    4: {
        "name": ["'Program Cost Estimation' process in your program/ department?",
                 "'Program Cost Budgeting' process in your program/ department?",
                 " 'Program Financial Framework Establishment' process in your program/ department?",
                 " 'Program Financial Management Plan Development' process in your program/ department?",
                 " 'Program Financial Monitoring and Control' process in your program/ department?",
                 " 'Component Cost Estimation' process in your program/ department?",
                 " 'Program Financial Closure' process in your program/ department?", ],
        "description": ["Program Cost Estimation Process standards are established.",
                        "Program Cost Budgeting Process standards are established.",
                        "Analyzed. Program Financial Framework Establishment Process standards are established.",
                        "Program Financial Management Plan Development Process standards are established.",
                        "Program Financial Monitoring and Control Process standards are established.",
                        "Component Cost Estimation Process standards are established.",
                        "Program Financial Closure Process standards are established."]
    },
    5: {
        "name": [" 'Program Risk Management Planning' process in your program/ department?",
                 " 'Program Risk Identification' process in your program/ department?",
                 " 'Program Risk Response Planning' process in your program/ department?",
                 " 'Program Risk Monitoring and Control' process in your program/ department?",
                 " 'Program Risk Analysis' process in your program/ department?", ],
        "description": ["Program Risk Management Planning Process standards are established.",
                        "Program Risk Identification Process standards are established.",
                        "Program Risk Response Planning Process standards are established.",
                        "Program Risk Monitoring and Control Process standards are established.",
                        "Program Risk Analysis Process standards are established."]
    },
    6: {
        "name": [" 'Program Quality Planning' process in your program/ department?",
                 "'Program Quality Assurance' process in your program/ department?",
                 "'Program Quality Control' process in your program/ department?", ],
        "description": ["Program Quality Planning Process standards are established.",
                        "The overall program or management system is established to assign responsibilities and authorities, define policies and requirements, and provide for the performance and assessment of work.",
                        "The overall system developed and used by a producer ensures that a product will meet specified quality standards, including documentation supporting its effectiveness."]
    },
    7: {
        "name": ["'Communications Planning' process in your program/ department?",
                 " 'Information Distribution' process in your program/ department?", ],
        "description": ["Communications Planning Process standards are established.",
                        "Information Distribution Process standards are established."]
    },
    8: {
        "name": [" 'Program Procurement Planning' process in your program/ department?",
                 " 'Program Procurement Management' process in your program/ department?",
                 " 'Program Procurement Closure' process in your program/ department?",
                 " 'Program Procurement' process in your program/ department?", ],
        "description": ["Program Procurement Planning Process standards are established.",
                        "Program Procurement Administration Process standards are established.",
                        "Program Procurement Closure Process standards are established.",
                        "Program Procurement Process standards are established."]
    },
    9: {
        "name": ["'Planning Program Stakeholder Management' process in your program/ department?", ],
        "description": ["A written document that outlines how your team plans to manage the goals and expectations of key stakeholders during the project lifecycle."]
    },
    10: {
        "name": [" 'Resource Planning' process in your program/ department?",
                 " 'Resource Prioritization' process in your program/ department?",
                 " 'Resource Interdependency Management' process in your program/ department?", ],
        "description": ["Resource Planning Process standards are established.",
                        "Resource Prioritization Process standards are established.",
                        "Resource Interdependency Management Process standards are established."]
    }
}
ka = [1, 2, 3,
      4, 5, 6,
      7, 8, 9,
      10]

combined = []
for category in ka:
    dsl = ["standardize", "measure", "control", "improve"]
    for idx, name in enumerate(ls[category]["name"]):
        # Ensuring the lengths of names and descriptions are the same
        min_length = min(len(ls[category]["name"]), len(ls[category]["description"]))
        if idx < min_length:
            for stage in dsl:
                combined.append({
                    "name": ls[category]["name"][idx],
                    "description": ls[category]["description"][idx],
                    "domain": "program",
                    "stage": stage,
                    "knowledge_area": category
                })

print(combined)


# dd = ["Program Integration Management","Program Scope Management","Program Schedule Management","Program Financial Management","Program Risk Management","Program Quality Management", "Program Communications Management", "Program Procurement Management", "Program Stakeholder Management","Program Resource Management","Portfolio Government Management","Portfolio Communication Management","Portfolio Strategy Management", "Portfolio Risk Management", "Portfolio Performance Management","Cultural Organizational Project Management Policy and Vision", "Cultural Sponsorship","Cultural Strategic Alignment","Cultural Organizational Project Management Communities","Human Resources Competency Management", "Human Resources Resource Allocation", "Human Resources Project Management Training", "Structural Benchmarking", "Structural Knowledge Management and PMIS", "Structural Management Systems", "Structural Organizational Structures","Structural Project Management Metrics", "Structural Governance", "Technological Organizational Project Management Policy and Vision", "Technological Organizational Project Management Techniques", "Technological Organizational Project Management Methodology", "Integration Management", "Scope Management", "Quality Management", "Stakeholder Management", "Risk Management", "Procurement Management", "Communication Management", "Project Schedule Management", "Resource Management", "Cost Management"]
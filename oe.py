import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
django.setup()

from project.models import Question, KnowledgeArea
# from .models import Question, KnowledgeArea

ls = {
    "cultural": {
        16: {
            "questions": [
                "Establish standardized organizational project management policies for construction projects",
                "Educate executives on construction project principles and practices",
                "Establish internal project management communities within the construction organization",
                "Interact with external project management communities specific to the construction industry",
                "Define project management values that align with the requirements of the construction industry",
                "Implement an OPM leadership program tailored to the needs of the construction industry in Ethiopia",
                "Educate stakeholders on the importance and benefits of effective project management",
                "Promote cultural diversity awareness within the context of construction projects in Ethiopia",
                "Recognize the value of project management in achieving successful construction outcomes",
                "Create a risk-aware culture within your construction project"
            ],
            "description": [
                "The organization has policies describing the standardization, measurement, control, and continuous improvement of organizational project management processes.",
                "The organization educates its executives on the benefits of organizational project management.",
                "The organization establishes an internal community that supports project management.",
                "The organization encourages membership of external communities that support project management expertise. These can include professional associations or initiatives.",
                "The organization defines and applies project management vision and values within the organization.",
                "The organization has a leadership program for their OPM managers.",
                "The organization educates stakeholders in OPM.",
                "Educate employees on cultural diversity and empower them for working in a multi-cultural environment.",
                "The organization recognizes the value of project management.",
                "The organization has created a risk-aware culture, advocating that the portfolio, programs, and projects are less risky when more risks are being identified."
            ]
        },
        17: {
            "name": [
                "Establishing sponsorship mechanisms to support your construction project",
                "Ensure executive support for your construction project to facilitate its successful implementation"
            ],
            "description": [
                "Sponsors actively participate in supporting the project.",
                "The executives strongly support the project management process."
            ]
        },
        18: {
            "name": [
                "Achieve strategic goals and objectives in your construction project through the use of effective OPM practices organizational project management",
                "Evaluate the construction project’s value performance",
                "Assessing the realization of proposed benefits",
                "Developing an enterprise risk management methodology tailored to the construction industry",
                "Utilizing formal performance assessment methods specific to your construction project",
                "Creating a strategic alignment framework within the construction context",
                "Reporting your construction project management performance in alignment with organizational strategy"
            ],
            "description": [
                "Organizations adopt organizational project management as the means of achieving organization’s goals and objectives.",
                "The organization performs value performance analysis against the performance of its endeavors and refines the strategy appropriately.",
                "The organization establishes a formal process to assess and account for the realization of proposed benefits of their portfolio, programs, and projects.",
                "The organization captures enterprise risk (market, financial, business, and environment) and their impact on strategy and portfolio, programs, and projects.",
                "A strategic alignment framework is established.",
                "Project or phase(s) in relation to the business case used during initiation.",
                "Project or phase(s) in relation to the business case used during initiation."
            ]
        },
        19: {
            "name": [
                "Establish construction project delivery guidelines and techniques special interest group."
            ],
            "description": [
                "Organization establishes special interest groups for the project management community to share project delivery tips and techniques with respective colleagues."
            ]
        }
    },
    "humanresources": {
        20: {
            "name": [
                "Staff organizational project management with competent resources",
                "Establish career path for all organizational project management roles",
                "Manage the holistic view of the project",
                "Manage the environment",
                "The organization manages self-development"
            ],
            "description": [
                "The organization provides organizational project management with an adequate workforce with the right level of competence for each project-related role.",
                "The organization has progressive career paths for organizational project management-related roles.",
                "The project managers understand stakeholder needs, project impacts to the overall organization environment.",
                "Project managers effectively manage the project environment.",
                "The organization provides project managers the ability to effectively manage and develop their competencies."
            ]
        },
        21: {
            "name": [
                "Record project resource assignments",
                "Provide competent organizational project management resources",
                "Establish resource allocation and optimization processes",
                "Specialists are shared between projects"
            ],
            "description": [
                "The organization has a formal process for assigning resources to projects and recording assignments.",
                "The organization’s project management community provides sufficient competent resources to manage organizational project management.",
                "The organization utilizes resources in an optimized manner matching available resources with project and program needs.",
                "The organization provides adequate staffing with specialized resources, sharing them between the projects."
            ]
        },
        22: {
            "name": [
                "Provide continuous project management training"
            ],
            "description": [
                "The organization provides project management training appropriate for all roles within the project hierarchy."
            ]
        }
    },
    "structural": {
        23: {
            "name": [
                "Benchmark organizational project management performance against industry standards",
                "Benchmark OPM practices and results",
                "Incorporate performance benchmarks into a balanced scorecard system"
            ],
            "description": [
                "The organization identifies external standards against which they measure organizational project management performance.",
                "The PMO is using benchmark data to compare its achieving and current state to other PMOs.",
                "Augment traditional financial measures with benchmarks for performance in relationship with customers, key internal processes, and learning."
            ]
        },
        24: {
            "name": [
                "Capture and share lessons learned",
                "Construction project management information system",
                "Establish executive summary dashboards",
                "Establish organizational project management reporting standards"
            ],
            "description": [
                "The organization collects and shares lessons learned from projects, programs, and portfolios.",
                "The organization has a mechanism for the storage, retrieval, dissemination, and reporting of organizational project management information.",
                "Organization has dashboards for executives that summarize project progress with clear indicators of project status.",
                "Organization has dashboards for executives that summarize project progress with clear indicators of project status."
            ]
        },
        25: {
            "name": [
                "Establish common construction project management framework"
            ],
            "description": [
                "The organization uses a project management framework for all phases of a project."
            ]
        },
        26: {
            "name": [
                "Establish organizational project management structure",
                "Adopt organizational project management structure",
                "Institutionalize organizational project management structure"
            ],
            "description": [
                "The organization has determined the appropriate organizational structure to support organizational project management.",
                "Adopt organizational project management structure across the organization.",
                "Institutionalize the organizational Project management structure across the organization."
            ]
        },
        27: {
            "name": [
                "Collect OPM success metrics",
                "Use OPM success metrics",
                "Verify OPM success metric accuracy",
                "Analyze and improve OPM success metrics"
            ],
            "description": [
                "The organization uses and maintains a formal performance system to collect OPM success metrics.",
                "The organization uses the OPM success metrics to improve the performance of project management against plans, and improve realization of benefit to the organization.",
                "The organization ensures that OPM and benefit to the organization data is valid and accurate.",
                "The organization continuously improves its OPM data collection and use processes."
            ]
        },
        28: {
            "name": [
                "Establish governance policies across the organization",
                "Consistent project governance across the enterprise",
                "Plan and establish project governance structure",
                "Provide governance oversight"
            ],
            "description": [
                "The organization establishes governance policies across the organization.",
                "The organization establishes a governance board over all the project processes across the enterprise to optimize business value.",
                "The project team identifies governance goals and defines the governance structure, roles, and responsibilities.",
                "The program team provides governance and audit ability throughout the course of the program."
            ]
        }
    },
    "technological": {
        29: {
            "name": [
                "Tailor project management processes flexibly",
                "Integrate project management methodology with organizational processes"
            ],
            "description": [
                "The organization applies processes in a manner that is relevant to each project.",
                "The organization integrates the project management methodology with strategic, operational, and tactical processes."
            ]
        },
        30: {
            "name": [
                "Accommodate organization’s approved frameworks and governance structures",
                "Developing project management templates",
                "Building Information Modeling (BIM) Adoption"
            ],
            "description": [
                "Design and adopt flexible project management processes to accommodate and comply with frameworks and governance structures approved by the organization, such as CMMI, ITIL, and COBIT.",
                "Develop templates for organizations adopted project management knowledge areas to standardize project management practices.",
                "Actively promote the adoption of BIM technology in construction projects to enhance collaboration, coordination, and communication among project stakeholders. They can require BIM implementation in project contracts and provide necessary resources for training and support."
            ]
        },
        31: {
            "name": [
                "Estimating template/tools established for use across the organization",
                "Use mathematically sound methods for prioritization",
                "Manage project resources",
                "Manage project issues",
                "Manage component interfaces",
                "Plan project stakeholder management",
                "Identify project stakeholders",
                "Engage project stakeholders",
                "Manage project stakeholder expectations",
                "Plan for audits"
            ],
            "description": [
                "Standardize estimating so that there is consistency in the percentage applied to similar activities, consistent risk factors applied.",
                "The result of this prioritization along with the objectives prioritization produces ratio-scale relative benefit for each project candidate so they can be compared meaningfully.",
                "The project manager allows for the adjustment and reallocation of resources required to meet the needs of the project.",
                "The project team identifies, tracks, and closes issues effectively to ensure stakeholder expectations are aligned with project activities and deliverables.",
                "The project team maintains the adherence of project delivery and its constituent parts and manages relationships between the project components.",
                "The project manager covers planning how stakeholders will be identified, analyzed, engaged, and managed throughout the life of the project.",
                "The project team addresses the systematic identification and analysis of Project stakeholders and creates the stakeholder register.",
                "Engage project stakeholders in the project activities from initiation to closeout.",
                "The project team manages communications to satisfy the requirements of and resolves issues with project stakeholders.",
                "The Project team prepares for both external and internal audits of project finances, processes, and documents and demonstrates compliance with approved organizational project management processes."
            ]
        }
    }
}

# combined = []

# for key, value in ls.items():
#     for ka, quest in value.items():
#         if "questions" in quest:
#             names = quest["questions"]
#         else:
#             names = quest["name"]
        
#         descriptions = quest["description"]
        
#         # Check if the lengths of the lists match
#         if len(names) != len(descriptions):
#             print(f"Lengths of 'name' and 'description' lists do not match for {key}-{ka}")
#             continue  # Skip this iteration if lengths don't match
        
#         for i in range(len(names)):
#             combined.append({
#                 "name": names[i],
#                 "description": descriptions[i],
#                 "domain": "oe",
#                 "stage": key,
#                 "knowledge_area": ka,
#             })

# print(len(combined))

combined = []

for key, value in ls.items():
    for ka, quest in value.items():
        if "questions" in quest:
            names = quest["questions"]
        else:
            names = quest["name"]
        
        descriptions = quest["description"]
        
        if len(names) != len(descriptions):
            print(f"Lengths of 'name' and 'description' lists do not match for {key}-{ka}")
            continue
        
        for i in range(len(names)):
            combined.append({
                "name": names[i],
                "description": descriptions[i],
                "domain": "oe",
                "stage": key,
                "knowledge_area": ka,
            })

for item in combined:
    knowledge_area = KnowledgeArea.objects.get(id=item["knowledge_area"])
    Question.objects.create(
        name=item["name"],
        description=item["description"],
        domain=item["domain"],
        stage=item["stage"],
        knowledge_area=knowledge_area
    )

print(f'Inserted {len(combined)} records into the database.')
print("Done")

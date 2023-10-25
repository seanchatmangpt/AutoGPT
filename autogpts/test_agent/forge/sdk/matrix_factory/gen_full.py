import time

import yaml
from jinja2 import Environment, FileSystemLoader

from fgn.completion.complete import acreate
from matrix_factory.chat_helpers import best_models, instruct_models

# Define your jinja template
template_str = """
# {{ page_title }}
---
**{{ module_title }}**

## Overview
{{ overview_description }}

## Features
{% for feature in features %}
- {{ feature }}
{% endfor %}

## Further Documentation
Please refer to the detailed documentation for in-depth explanations and user guides related to {{ module_title }}.
"""

# Load your template using Jinja2
env = Environment(loader=FileSystemLoader("."))
template = env.from_string(template_str)

# Load your YAML data
yaml_data = """
# Page: Home
Home:
  page_title: "Home"
  module_title: "Home"
  overview_description: "Welcome to the Home Page of My Application."
  features:
    - "Welcome Message"
    - "Dashboard Overview of All Modules"
    - "Dynamic Navigation to Featured Modules"
    - "System Notifications and Alerts"
    - "Quick Access Tools (e.g., search, settings)"

# Page: Administration Module
AdministrationModule:
  page_title: "Administration Module"
  module_title: "Administration Module"
  overview_description: "Welcome to the Administration Module of My Application."
  features:
    - "Dashboard with Summary of System Health and Usage Metrics"
    - "Themes and UI Customization Options"
    - "User and Role Management"
    - "Federated Security Configuration"
    - "System-wide Audit Trail Logs"
    - "External System Integrations Management"
    - "System Preferences and Global Settings"

# Page: Online Contract Signing Facility
OnlineContractSigningFacility:
  page_title: "Online Contract Signing Facility"
  module_title: "Online Contract Signing Facility"
  overview_description: "Welcome to the Online Contract Signing Facility of My Application."
  features:
    - "Dashboard with Pending Actions (e.g., signatures required, review tasks)"
    - "Upload Contract with File Format Validation"
    - "Interactive Contract Markup and Annotation Tool"
    - "Signatory and Carbon Copy Management"
    - "Digital Signature Pad with User Identity Verification"
    - "Contract Review and Approval Workflow Visualization"
    - "Contract Metadata and Details Pane"
    - "Contract Version History and Change Tracking"

# Page: Contract Administration Capability
OnlineContractAdminCapability:
  page_title: "Contract Administration Capability"
  module_title: "Contract Administration Capability"
  overview_description: "Welcome to the Contract Administration Capability of My Application."
  features:
    - "Dashboard with Contract Metrics (e.g., approval rates, pending reviews)"
    - "Interactive Contract Query Tool with Natural Language Processing"
    - "Tolerance and Compliance Rule Management"
    - "Stack Management with Label Customization"
    - "Automatic and Manual Tolerance Adjustments"
    - "Contract Health Monitoring and Reporting"

# Page: Headless CRM Dashboard
HeadlessCRM:
  page_title: "Headless CRM Dashboard"
  module_title: "Headless CRM Dashboard"
  overview_description: "Welcome to the Headless CRM Dashboard of My Application."
  features:
    - "Dashboard with CRM Health Metrics and Data Synchronization Status"
    - "CRM Connection and Data Source Management"
    - "Advanced Data Query Builder"
    - "Data Visualization and Analytics Tools"
    - "Predictive Analytics Engine with User-Configurable Models"
    - "Data Export and Reporting Features"

# Page: Headless Email Facility Dashboard
HeadlessEmailFacility:
  page_title: "Headless Email Facility Dashboard"
  module_title: "Headless Email Facility Dashboard"
  overview_description: "Welcome to the Headless Email Facility Dashboard of My Application."
  features:
    - "Dashboard with Email Metrics and Communication Analysis"
    - "Email Server Connection Management"
    - "Email Browsing and Search Interface"
    - "Predictive Analytics for Email Trends and User Behavior"
    - "Email Templating and Automated Response Tools"

# Page: Content Creation Facility
ContentCreationFacility:
  page_title: "Content Creation Facility"
  module_title: "Content Creation Facility"
  overview_description: "Welcome to the Content Creation Facility of My Application."
  features:
    - "Dashboard with Content Metrics and Performance Insights"
    - "Rich Text Content Editor with Media Embedding Features"
    - "Multi-platform Post Scheduler and Publisher"
    - "Email Creation Tool with Responsive Design Templates"
    - "Landing Page Builder with Drag-and-Drop Features"
    - "Personalized Content Recommendations based on User Behavior and Competitive Analysis"

# Page: Event Planning Facility
EventPlanningFacility:
  page_title: "Event Planning Facility"
  module_title: "Event Planning Facility"
  overview_description: "Welcome to the Event Planning Facility of My Application."
  features:
    - "Dashboard with Upcoming Events and Performance Metrics"
    - "Event Creation Wizard with Budgeting and Resource Allocation Tools"
    - "Historical Event Performance Analysis"
    - "ROI Calculator with Customizable Metrics"
    - "Competitive Radar Integration for Event Strategy Insights"

# Page: Social Media Facility
SocialMediaFacility:
  page_title: "Social Media Facility"
  module_title: "Social Media Facility"
  overview_description: "Welcome to the Social Media Facility of My Application."
  features:
    - "Dashboard with Social Media Performance Metrics and Trends"
    - "Multi-platform Social Media Manager"
    - "Post Creation, Scheduling, and Analytics"
    - "Sentiment Analysis and Trending Topic Insights"
    - "Audience Behavior Predictive Analytics"

# Page: Financial Software Connection Dashboard
FinancialSoftwareConnectionFacility:
  page_title: "Financial Software Connection Dashboard"
  module_title: "Financial Software Connection Dashboard"
  overview_description: "Welcome to the Financial Software Connection Dashboard of My Application."
  features:
    - "Dashboard with Financial Data Summary and Health Metrics"
    - "ERP Data Integration and Management Tools"
    - "Financial Transaction Explorer"
    - "GL, AP, and AR Automated Entry Tools"
    - "Real-time Financial Reporting and Data Visualization"

# Page: Competitive Radar Facility
CompetitiveRadarFacility:
  page_title: "Competitive Radar Facility"
  module_title: "Competitive Radar Facility"
  overview_description: "Welcome to the Competitive Radar Facility of My Application."
  features:
    - "Dashboard with Competitive Landscape Overview"
    - "Company Search and Profile Viewer"
    - "SWOT and PESTEL Analysis Interactive Tools"
    - "Data Visualization with Drill-Down Capabilities"
    - "Competitive Insight Reporting and Data Export"

# Page: Web Module Dashboard
WebModule:
  page_title: "Web Module Dashboard"
  module_title: "Web Module Dashboard"
  overview_description: "Welcome to the Web Module Dashboard of My Application."
  features:
    - "Dashboard with Web Performance Metrics and SEO Health"
    - "Web Property Manager with Live Preview"
    - "Content Infusion Tools with Competitive Radar Insights"
    - "Module Integration Management for CRM, Email, and Financial Data"
    - "Website Analytics and User Behavior Tracking"

# Page: Decision Making Facility
DecisionMakingFacility:
  page_title: "Decision Making Facility"
  module_title: "Decision Making Facility"
  overview_description: "Welcome to the Decision Making Facility of My Application."
  features:
    - "Dashboard with Decision Metrics and System Recommendations"
    - "Decision Rule Builder and Manager"
    - "Tolerance Setting Tools with Predictive Adjustments"
    - "Decision Logs and Analysis Reports"

# Page: Settings and Configurations (Common for All Modules)
Settings:
  page_title: "Settings and Configurations (Common for All Modules)"
  module_title: "Settings and Configurations"
  overview_description: "Welcome to the Settings and Configurations section common to all modules in My Application."
  features:
    - "User and Role Management with Permissions Overview"
    - "System Preferences and Global Settings"
    - "Module-specific Configuration Options"
    - "Backup and Data Management Tools"

# Page: About and Documentation
Documentation:
  page_title: "About and Documentation"
  module_title: "About and Documentation"
  overview_description: "Welcome to the About and Documentation section of My Application."
  features:
    - "User Manuals and Interactive Guides"
    - "Technical Documentation Library"
    - "Frequently Asked Questions (FAQ)"
    - "System Version and Update Notes"

"""

data = yaml.safe_load(yaml_data)

# Generate docs for each module using the template
docs = []
for module, content in data.items():
    rendered_content = template.render(**content)
    docs.append(rendered_content)

# Save generated docs to individual files or any other desired format
# for idx, doc in enumerate(docs):
#     with open(f"module_{idx + 1}_documentation.md", "w") as file:
#         file.write(doc)

import asyncio

# MODELS = best_models  # and other models...
MODELS = instruct_models  # and other models...


async def generate_template_with_model(model_selector, prompt):
    """
    Asynchronously generates content using a round-robin model.
    """
    model = next(model_selector)
    result = await acreate(
        model=model, prompt=prompt, temperature=0.0, max_tokens=1000, stop=["```"]
    )
    return result


def round_robin_models():
    """A generator that yields models in a round-robin fashion."""
    idx = 0
    while True:
        yield MODELS[idx % len(MODELS)]
        idx += 1


def construct_prompt_for_model(module, content):
    """Constructs a prompt for a given module and content."""
    # Here you'd construct the prompt for the model (replace placeholder with the actual prompt)
    prompt = f"""You are a React Component Tree Architect tasked with designing a React component for "{module}". 
    The component should represent the following content:
    {content['features']}

    Given these details, please provide a basic React component structure for the "{module}".
    

    ```javascript
    import React from 'react';
    // Import the necessary components here
    """
    return prompt


async def main():
    """Asynchronous main function to run templates with models in round-robin and rate limiting."""
    start = time.time()
    tasks = []
    model_selector = round_robin_models()

    print("Generating React Components...")

    for module, content in data.items():
        prompt = construct_prompt_for_model(
            module, content
        )  # Assuming you'd build your prompt this way
        tasks.append(generate_template_with_model(model_selector, prompt))

    results = await asyncio.gather(*tasks)
    end = time.time()
    print(f"Total time taken: {end - start} seconds")
    for i, result in enumerate(results):
        with open(f"react/module_{i + 1}_react.md", "w") as file:
            file.write(result)


if __name__ == "__main__":
    # Execute
    asyncio.run(main())

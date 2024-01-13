import os

# Define the folder structure and content for each markdown file
folder_structure = [
    {
        "folder_name": "landing_page",
        "files": [
            {"file_name": "thankYou.md", "content": "# Content for the Landing/Thank You Page"}
        ],
    },
    {
        "folder_name": "role_description",
        "files": [
            {"file_name": "roleOverview.md", "content": "# Overview of your role for the Role Description Page"}
        ],
    },
    {
        "folder_name": "code_snippets",
        "files": [
            {"file_name": "frontendSnippets.md", "content": "# Frontend code snippets"},
            {"file_name": "backendSnippets.md", "content": "# Backend code snippets"},
            {"file_name": "testingSnippets.md", "content": "# Testing code snippets"},
            {"file_name": "principlesSnippets.md", "content": "# Code principles and best practices"},
            {"file_name": "dataStructuresAlgos.md", "content": "# Data Structures and Algorithms snippets"},
            {"file_name": "designPatterns.md", "content": "# Design Patterns snippets"},
            {"file_name": "databaseQueries.md", "content": "# Database and Query snippets"},
            {"file_name": "apiInteractions.md", "content": "# API Interaction snippets"},
            {"file_name": "securityAuth.md", "content": "# Security and Authentication snippets"},
            {"file_name": "performanceOptimization.md", "content": "# Performance Optimization snippets"},
            {"file_name": "responsiveUI.md", "content": "# Responsive and Interactive UI snippets"},
            {"file_name": "devOpsInfrastructure.md", "content": "# DevOps and Infrastructure snippets"},
            {"file_name": "debuggingProblemSolving.md", "content": "# Debugging and Problem-Solving snippets"},
            {"file_name": "accessibility.md", "content": "# Accessibility (a11y) snippets"},
            {"file_name": "internationalization.md", "content": "# Internationalization and Localization snippets"},
        ],
    },
    {
        "folder_name": "experience_stories",
        "files": [
            {"file_name": "story1.md", "content": "# Individual story of a particular project or experience"},
            {"file_name": "story2.md", "content": "# Another story/example"},
            {"file_name": "story3.md", "content": "# Additional stories as needed"},
        ],
    },
    {
        "folder_name": "about",
        "files": [
            {"file_name": "aboutMe.md", "content": "# Content for the About Page (if applicable)"}
        ],
    },
]

# Define the base folder path
base_folder_path = "./content"

# Create the folder structure and files
for folder_data in folder_structure:
    folder_name = folder_data["folder_name"]
    folder_path = os.path.join(base_folder_path, folder_name)
    
    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    # Create and write content to each file in the folder
    for file_data in folder_data["files"]:
        file_name = file_data["file_name"]
        file_content = file_data["content"]
        file_path = os.path.join(folder_path, file_name)
        
        # Write content to the file
        with open(file_path, "w") as file:
            file.write(file_content)

"Folder structure and files created successfully!"

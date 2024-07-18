# Content Creation Crew for Blog Posts

This project demonstrates a structured approach to generating high-quality blog content using a team of specialized agents powered by the GROQ_LLM model. The process involves three distinct roles: Content Planner, Content Writer, and Editor. Each role ensures that the final blog post is engaging, factually accurate, and aligned with the brand's voice.

## Overview

The system uses the GROQ_LLM model to facilitate a multi-step content creation process. Here's a brief description of each component:

### Agents

1. **Content Planner**:
   - **Role**: Plans engaging and factually accurate content on a given topic.
   - **Responsibilities**: 
     - Prioritize trends, key players, and noteworthy news.
     - Identify the target audience and their interests.
     - Develop a detailed content outline including an introduction, key points, and a call to action.
     - Include SEO keywords and relevant data sources.

2. **Content Writer**:
   - **Role**: Writes insightful and factually accurate opinion pieces based on the planner's outline.
   - **Responsibilities**:
     - Use the content plan to craft a compelling blog post.
     - Incorporate SEO keywords naturally.
     - Ensure the post is structured with an engaging introduction, insightful body, and a summarizing conclusion.
     - Proofread for grammatical errors and alignment with the brand's voice.

3. **Editor**:
   - **Role**: Edits the blog post to align with the writing style of the organization.
   - **Responsibilities**:
     - Review the blog post to ensure it follows journalistic best practices.
     - Provide balanced viewpoints when offering opinions or assertions.
     - Avoid major controversial topics or opinions when possible.

### Tasks

1. **Plan**:
   - **Description**: 
     - Prioritize the latest trends, key players, and noteworthy news on the topic.
     - Identify the target audience, considering their interests and pain points.
     - Develop a detailed content outline including an introduction, key points, and a call to action.
     - Include SEO keywords and relevant data or sources.
   - **Expected Output**: A comprehensive content plan document with an outline, audience analysis, SEO keywords, and resources.

2. **Write**:
   - **Description**: 
     - Use the content plan to craft a compelling blog post.
     - Incorporate SEO keywords naturally.
     - Ensure the post is structured with an engaging introduction, insightful body, and a summarizing conclusion.
     - Proofread for grammatical errors and alignment with the brand's voice.
   - **Expected Output**: A well-written blog post in markdown format, ready for publication, with each section containing 2 or 3 paragraphs.

3. **Edit**:
   - **Description**: Proofread the given blog post for grammatical errors and alignment with the brand's voice.
   - **Expected Output**: A well-written blog post in markdown format, ready for publication, with each section containing 2 or 3 paragraphs.

## Getting Started

### Prerequisites

- Python 3.7+
- Obtain a GROQ API key from [console.groq.com](https://console.groq.com) and set it as an environment variable `GROQ_API_KEY`.
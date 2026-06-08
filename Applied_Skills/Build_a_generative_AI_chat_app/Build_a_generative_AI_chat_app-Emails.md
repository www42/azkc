[Microsoft Applied Skills: Build a generative AI chat app - Applied Skills](https://learn.microsoft.com/en-us/credentials/applied-skills/build-a-generative-ai-chat-app/)

Date: 2026/04/29

---

Subject: General guidelines

From: cto@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Thank you for agreeing to help our team build a generative Al chat app.

We have some general guidelines that you must follow when you perform tasks in Azure. Please always use the following guidelines:

* When creating objects, use the default settings unless a different configuration is required to complete the task successfully.
* Only create, delete, or modify objects to achieve the stated requirements. Unnecessary changes to the environment can adversely affect your final score.
* If there are multiple approaches to achieving a goal, always choose the approach that requires the least amount of administrative effort.

Thanks,
<br>
Chief Technology Officer (CTO)

---

Subject: Existing environment

From: networkadmin@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Here are your credentials for accessing our resources in Azure:

User name: User1@cloudslice.onmicrosoft.com
<br>
Temporary Access Pass: ********

You can find these credentials by clicking the Instructions tab.

You have been given rights to the **RG1** resource group. Please create all Azure objects in this resource group.

Microsoft Visual Studio Code is installed on the local machine. All necessary extensions and libraries are already installed.

Thanks,
<br>
Network administrator

---

Subject: Deploy a Microsoft Foundry model

From: projman@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Hello,

We are currently building an Al app named App1 to help users answer questions in a chat interface. We need your help deploying an Al model for the app.

Due to compliance reasons, only **phi-4**, **gpt-4.1-nano** and **gpt-4.1-mini** models are allowed to be used within the app

This is your task:

You need to create a new Microsoft Foundry project in the **RG1** resource group and deploy either the **phi-4**, **gpt-4.1-nano** or **gpt-4.1-mini** model. The deployed model must meet the following requirements:

* Provides reasoning capabilities
* Has the highest quality metrics compared to the other two allowed models

Configure the model to use a content filter that blocks all severity levels for all harmful content. Also block jailbreak and indirect attacks. Configure these settings for both inputs and outputs.

Thanks,
<br>
Project Management Team

---

Subject: Build the initial Al chat app with Microsoft Foundry

From: projman@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Hello,

We are building a small generative Al chat app named App1 that connects to the Microsoft Foundry model you just deployed. We have both a C# version and Python version of the app. Use which ever language you are most comfortable with but only modify one version. The app versions are in **C:\Repos\App1**.

App1 will use the Microsoft Foundry SDK, send user messages to the model, and display the responses in the app.

This is your task:

You need to configure App1 as follows:

* Set up the app to connect to the deployed model.
* Add the Microsoft Foundry SDK dependency to the project.
* Update the app code to enable users to send a message in the app and ensure these messages are forwarded to the Al model to request answers.
* Update the app so that the model's responses are clearly shown in the chat interface. The responses must always be in the formatted as markdown.

By the end of this task, you will have a working chat app that sends messages to the Microsoft Foundry model and displays responses in the chat interface. Ensure that you have added code for the following comments:

* TODO: Configure to the deployed model
* TODO: Reference the Microsoft Foundry SDK
* TODO: Initialize the client
* TODO: Submit the message to Microsoft Foundry
* TODO: Output the message in the console

The TODO comments are located in the following files:

* For Python: **env**, **App1.py**
* For C#: **appsettings.json**, **App1.cs**

Note: When completing the TODO tasks, do not rename or change any existing variables or code structure. Use the variables that are already defined and only add the required code where indicated.

Thanks,
<br>
Project Management Team

---

Subject: Implement conversation history

From: projman@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Hello,

Thank you for helping us get a working Al chat app up and running.

We have received complaints from some of our users that the chatbot is "forgetting" things discussed during the conversation. For example, if I ask, "What is the capital of California?", I will receive a response such as, "Sacramento is the capital of California." If I then ask, "How many people live there?", I will receive a response such as, "Sorry, I cannot answer your question. Please provide a location when asking about population numbers."

We are building a new app named App2 to keep track of the conversations and to remember what was already discussed. You can use the same Microsoft Foundry environment settings as you used for App1. The App2 versions are in **C:\Repos\App2**.

This is your task:

You need to add chat history to the context of App2. You must complete the following configuration tasks:

* Store the user and agent messages in an in-memory object.
* Add the conversation history to completions that you send to the model by using the send message method.
* Limit the conversation history to 10 turns (20 historical messages).

When you complete these tasks, you must be able to ask follow-up questions that refer to a previous item in the chat history. Ensure that you have added code for the following comments:

* TODO: Limit the conversation history
* TODO: Add conversation history (part 1, 2)
* TODO: Trim the chat history

Thanks,
<br>
Project Management Team

---

Subject: Status - Complete

From: sto@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Thank you for helping our team build a generative Al chat app.

We look forward to working with you again.

Regards,
<br>
Chief Technology Officer (CTO)

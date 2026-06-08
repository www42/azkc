[Microsoft Applied Skills: Get started developing agents in Microsoft Foundry](https://learn.microsoft.com/en-us/credentials/applied-skills/get-started-developing-agents-in-microsoft-foundry/)

Date: 2026-06-06

---

Subject: General guidelines

From: cto@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Thank you for agreeing to help our team get started developing agents in Microsoft Foundry. We have some general guidelines that you must follow when you perform tasks in Azure.

Please always use the following guidelines:

- When creating objects, use the default settings unless a different configuration is required to complete the task successfully.
- Only create, delete, or modify objects to achieve the stated requirements. Unnecessary changes to the environment can adversely affect your final score.
- If there are multiple approaches to achieving a goal, always choose the approach that requires the least amount of administrative effort.
- Make sure every object you create in the project uses the exact name specified in each email.

Thanks,
<br>
Chief Technology Officer (CTO)

---

Subject: Existing environment

From: networkadmin@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Here are your credentials for accessing our resources in Microsoft Foundry.

User name: User1@cloudslice.onmicrosoft.com
<br>
Temporary Access Pass: *******

You can find these credentials by clicking the Instructions tab.

We have already provisioned a Microsoft Foundry project named **user1-62415637** for you to use. Be sure to work in this project.

Thanks,
<br>
Network administrator

---

Subject: Configure models in Microsoft Foundry

From: projman@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Hello,

We have recently started working with Microsoft Foundry and need your help to configure the models. We want you to deploy a new model and modify the configuration of an existing model.

This is your task:

You need to deploy a **gpt5-mini** model that uses the Data Zone Standard Deployment type. Your infrastructures token rate per minute is limited by policy. Ensure to select Custom settings to limit Tokens to less than 150,000.

Next, you must configure the preexisting model-router model to meet the following requirements:

- Ensure that the model data is processed within the data zone of the Foundry project.
- Consume a maximum of 50,000 input token per minute.
- Use the Contoso guardrail.

Thanks,
<br>
Project Management Team

---

Subject: Create an agent

From: projman@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Hello,

Now that the model has been configured, we want you to create a new agent that can analyze sales data. The agent will perform calculations by using the **Northwind.xlsx** Microsoft Excel file. You can find the file in **c:\files**.

This is your task:

You need to create an agent named **agent1** that meets the following requirements:

- Configure the agent to have a display name of **Sales Analyzer** and the following description: **This agent analyzes Northwind Traders historical sales data**.
- Use the gpt-5-mini model that you deployed previously and ensure that the reasoning effort is medium.
- Use the following instructions: **You reason over Excel sheets that contain sales data. Answer only questions that can be answered from the uploaded Excel sales data. Use the workbook as the sole source of truth for summaries, calculations, comparisons, trends, and anomalies. Do not use outside knowledge. If a question is out of scope, say: "I can only answer questions based on the uploaded Excel sales data."**
- Ensure that agent1 can reason over and analyze Northwind.xlsx by using the Code Interpreter.

Thanks,
<br>
Project Management Team

---

Subject: Test the agent

From: projman@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Hello,

Next, we want you to enhance agent1 by adding a few starter prompts and then test whether agent1 works as expected.

This is your task:

You need to create the following starter prompts:
- Calculate the total sales per year.
- Top 5 customers by revenue per year.

Once you have completed all the configurations and saved the agent, test agent1 by running both starter prompts.

Thanks,
<br>
Project Management Team

---

Subject: Status - Complete

From: cto@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Thank you for helping our team get starred developing agents in Microsoft Foundry.

We look forward to working with you again.

Regards,
<br>
Chief Technology Officer (CTO)
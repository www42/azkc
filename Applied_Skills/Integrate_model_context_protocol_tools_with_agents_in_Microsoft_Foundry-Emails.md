[Microsoft Applied Skills: Integrate model context protocol tools with agents in Microsoft Foundry](https://learn.microsoft.com/en-us/credentials/applied-skills/integrate-model-context-protocol-tools-with-agents-in-microsoft-foundry/)

Date: 2026-06-07

---

Subject: General guidelines

From: cto@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Thank you for agreeing to help our team integrate model context protocol tools with agents in Microsoft Foundry.

We have some general guidelines that you must follow when you perform tasks in Foundry. Please always use the following guidelines:
- When creating objects, use the default settings, unless a different configuration is required to complete the task successfully.
- Only create, delete, or modify objects to achieve the stated requirements. Unnecessary changes to the environment can adversely affect your final score.
- If there are multiple approaches to achieving a goal, always choose the approach that requires the least amount of administrative effort.

Thanks,
<br>
Chief Technology Officer (CTO)

---

Subject: Existing environment

From: networkadmin@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Here are your credentials for accessing our resources in Microsoft Foundry:

User name: User1
<br>
Temporary Access Pass: ********

You can find these credentials by clicking the Instructions tab.

We have provisioned the following resources already:
- A Microsoft Foundry project named **project-62441271** that has a gpt-5-mini model deployed.
- An Application Insights instance named **appInsights62441271**.
- A custom MCP server named **IncidentsMCP**

Thanks,
<br>
Network administrator

---

Subject: Deploy a new agent

From: projman@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Hello,

We are performing a proof of concept (POC) in Microsoft Foundry of a new agentic solution. We need your help with the initial agent deployment. We have already provisioned a Foundry project named **project-62441271**.

This is your task:
Create a new agent named **Agent1**. **Agent1** must be connected to a model that meets the following requirements:
- Can perform model routing
- Supports tool calling and streaming
- Ensures that data is processed within the Microsoft data zone associated to the Foundry project.
- Routes model requests based on cost
- Only routes to **gpt-5-mini**, **gpt-5-nano**, and **grok-4-1-fast-reasoning**
- Consumes a maximum of 50,000 input tokens per minute

**Agent1** must have the following instructions: "You are a helpful Al assistant."

You do **NOT** need to publish the agent.

Thanks,
<br>
Project Management Team

---

Subject: Connect MCP servers

From: projman@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Hello,

We want to connect the following two MCP servers to Agent1: the Microsoft Learn MCP Server and a custom MCP server named IncidentsMCP.

IncidentsMCP has the following configurations:
- URL: https://function62441271-ebbfhcfegvdcerhy.swedencentral-01.azurewebsites.net/runtime/webhooks/mcp
- Authentication: key-based authentication
- Credential: x-functions-key:********************************************************

This is your task:

You need to ensure that **Agent1** can use all the tools available from the Microsoft Learn MCP Server only, without prompting the user for approval.

**Agent1** must be able to use only the `list_active_incidents` tool from the IncidentsMCP server, and tool use must be approved by the user before use.

Thanks,
<br>
Project Management Team

---

Subject: Monitor and evaluate Agent1

From: projman@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Hello,

We want to monitor the agents in our project and perform scheduled evaluations to ensure that Agent1 continually meets our needs.

This is your task:

You need to ensure that **Agent1** activity is logged to the existing Application Insights instance.

Next, create an evaluation of **Agent1** that uses a synthetic dataset that has 15 rows and uses the following prompt: "Generate queries for a Microsoft Foundry agent that uses the Microsoft Learn MCP Server to answer questions from Microsoft documentation."

Only evaluate ToolSelection. You do not need to wait for the evaluation run to complete.

Thanks,
<br>
Project Management Team

---

Subject: Status - Complete

From: cto@contoso.com
<br>
To: User1@cloudslice.onmicrosoft.com

Thank you for helping our team Integrate model context protocol tools with agents in Microsoft Foundry.

We look forward to working with you again.

Regards,
<br>
Chief Technology Officer (CTO)
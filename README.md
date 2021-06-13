# project_2


<ul>
  <li>Project Objective</li>
<li>App Overview</li>
<li>Treello Board</li>
<li>Database</li>
<li>CI Pipeline</li>
<li>App Design</li>
  <li>Deployment</li>
<li>Testing</li>
  <li>Risk Assessment</li>
<li>Current Issues</li>
<li>Improvements</li>
</ul>

## Project Objective

The requirements of the project are as follows:
<ul>
<li>A TRello board (or similar Kanban board technology) with full task expansion to complete the project.</li>
<li>An application that is fully integrated into a Version Control System using the Feature-Branch architecture, then created using a Continuous Integration server and distributed to a cloud-based virtual machine..</li>
<li>If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application.</li>
<li>The project must follow the Service-oriented architecture that has been asked for.</li>
<li>The project must be deployed using containerisation and an orchestration tool.</li>
<li>As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.</li>
<li>To make your application accessible to the user, you'll need to employ a reverse proxy.</li>
</ul>

## App Overview
I created a DnD Prize generating app.As part of having two implementations, the first one is simpler than the first. here the fisrt app will call upon service 2,3,4. service 2 will bring a ramdom number service 3 will bring a colour and service will generate a prize with combination of service 2,3.
![relation](https://camo.githubusercontent.com/4cbf75cf12104d7c32bb628ad0075e33fdeecab56e208cc4cb199d42d519ba88/68747470733a2f2f696d6775722e636f6d2f324747444f67382e6a7067)

## Trello Board

I utilised an Trello board to keep track of my project and its development. The things required for the Minimum Viable Product are also listed on this board (MVP). This also includes finished user stories, which allow me to see what the user should be able to perform at the very least.

![trello](https://paste.pics/5d958ccf23a61d52c3d84385965d42f4)
https://trello.com/b/0zlAQYwK/core-project

## Database

This application only requires a simple table to store information. Data is saved even after the application is brought down and back up via the use of a volume. The following table is used to store data:
database pic

## CI Pipeline  
This first diagram is what I initially imagined the CI Pipeline to look like. 
pic ci
##
risk assessment
below show the risk assessment for the risks faced in this project
![risk](https://camo.githubusercontent.com/a6b5bdd2b3992baddcc17ef8fbcecf820c550a4ae2de5020fb3aa7590a67fed9/68747470733a2f2f696d6775722e636f6d2f364765394468652e6a7067)
##  App Design 1
pic app1

## app design 2

## app 3 design



## Deployment
The app's deployment is automated and handled via Jenkins, Ansible, and Docker, among other tools. Jenkins will trigger a pipeline job through webhook after I commit to GitHub. My Jenkinsfile outlines the various steps of the pipeline. Each step refers to a script that handles a distinct stage of the pipeline to increase readability. Jenkins will start by inspecting the source code.Then run all my unit tests, and if they pass it will move on to the next stage.Jenkins will use Ansible to configure my computers in this step. Different roles are defined in my Ansible playbook, allowing me to instal different requirements based on what each machine will be accountable for. Ansible will instal Docker on each machine.

stage view is shown here
pic stage view

## Testing 

As part of the project requirement, I also carried out unit testing on both implementations of my application.

Here you can see the coverage of my tests for each service.
pics 4 of them

## issues

<ul>
<li> machine ran out of space
<li> nginx is not configured
 
## improvements

<ul>
<li>I could make the following enhancements in the future:
<li>To avoid downtime, include error handling.
<li>Keep stats in a database so that you have a complete character.
<li>Add a functionality that allows users to query the database at any moment to retrieve a character.
<li>Enhance your appearance




